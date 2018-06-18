
# source url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import pandas as pd

meta = pd.read_csv('./metadata_zip_file/metadata_2018.csv')
print(meta.shape)

f_idx = 0
f_nm = meta[meta.columns[0]][f_idx]




