import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

path = "/home/andrey/Downloads/"
filename = 'Durbin_Watson_tables.pdf'


def extract_text_by_page(full_path):
    with open(full_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(pdf_path, filename):
    i = 0
    for page in extract_text_by_page(pdf_path + filename):
        i += 1
        with open(f'{filename[:-4]}_page_{i}.txt', 'w') as f:
            print(page, file=f)
            f.close()


if __name__ == '__main__':
    extract_text(path, filename)
