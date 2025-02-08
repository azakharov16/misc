import os
from itertools import chain, cycle
import numpy as np
import pandas as pd
global path
global filename
path = os.getcwd()
filename = 'Durbin_Watson_tables'


def get_stats(page_num, nvals_ls, kvals_ls):
    nrows = len(nvals_ls)
    ncols = len(kvals_ls) * 2
    kvals_long = sorted([*kvals_ls, *kvals_ls])
    with open(path + '/' + filename + f'_page_{page_num}.txt', 'r') as f:
        text = f.read()
        f.close()
    while True:
        pos = text.find('dU')
        if pos < 0:
            break
        else:
            text = text[pos + 2:]
    text = text.strip()
    df = pd.DataFrame(columns=pd.MultiIndex.from_product([kvals_ls, ('dL', 'dU')]), index=nvals_ls)
    for r in range(nrows):
        ndigits = len(str(nvals_ls[r]))
        nsymbols = ncols * 5
        row = text[ndigits:ndigits + nsymbols]
        switch = cycle(('dL', 'dU'))
        for c in range(ncols):
            val = row[c * 5:(c + 1) * 5]
            print(r, val)
            if val == '-----':
                num = np.nan
            else:
                num = float(val)
            df.at[nvals_ls[r], (kvals_long[c], next(switch))] = num
        text = text[ndigits + nsymbols:]
    return df


### Parsing page 4 (99% critical values, part 1) ###
vals = chain(range(6, 41, 1), range(45, 105, 5), [150, 200])
nvals_ls = [*vals]
kvals_ls = list(range(1, 11))
df1 = get_stats(page_num=4, nvals_ls=nvals_ls, kvals_ls=kvals_ls)

### Parsing page 5 (99% critical values, part 2) ###
vals = chain(range(16, 41, 1), range(45, 105, 5), [150, 200])
nvals_ls = [*vals]
kvals_ls = list(range(11, 21))
df2 = get_stats(page_num=5, nvals_ls=nvals_ls, kvals_ls=kvals_ls)
df_foo = pd.DataFrame(np.nan, index=range(6, 16), columns=df2.columns)
df2 = pd.concat([df_foo, df2], axis=0)

### Merging results and exporting ###
df_conf99 = pd.concat([df1, df2], axis=1)
df_conf99.to_hdf('DW_crit_values.hd5', key='level_99', mode='w', format='fixed')

### Parsing page 6 (95% critical values, part 1) ###
vals = chain(range(6, 41, 1), range(45, 105, 5), [150, 200])
nvals_ls = [*vals]
kvals_ls = list(range(1, 11))
df1 = get_stats(page_num=6, nvals_ls=nvals_ls, kvals_ls=kvals_ls)

### Parsing page 7 (95% critical values, part 2) ###
vals = chain(range(16, 41, 1), range(45, 105, 5), [150, 200])
nvals_ls = [*vals]
kvals_ls = list(range(11, 21))
df2 = get_stats(page_num=7, nvals_ls=nvals_ls, kvals_ls=kvals_ls)
df_foo = pd.DataFrame(np.nan, index=range(6, 16), columns=df2.columns)
df2 = pd.concat([df_foo, df2], axis=0)

### Merging results and exporting ###
df_conf95 = pd.concat([df1, df2], axis=1)
df_conf95.to_hdf('DW_crit_values.hd5', key='level_95', mode='a', format='fixed')

