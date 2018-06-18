
# source url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import pandas as pd

base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/"
meta = pd.read_csv('./metadata_zip_file/metadata_2018.csv')
print(meta.shape)

f_idx = 0
f_nm = meta[meta.columns[0]][f_idx]

# didn't store temporary file
# https://techoverflow.net/2018/01/16/downloading-reading-a-zip-file-in-memory-using-python/
#if not os.path.exists('./temp_zip_file'):
#	os.makedirs('./temp_zip_file')

import requests
import io
import zipfile

res = requests.get(base_url+f_nm)
print(res)


