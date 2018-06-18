# source url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import pandas as pd

base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/"
meta = pd.read_csv('./metadata_zip_file/metadata_2018.csv')
print(meta.shape)

f_idx = 1
f_nm = meta[meta.columns[0]][f_idx]

"""
if not os.path.exists('./temp_zip_file'):
	os.makedirs('./temp_zip_file')
	install_geckodriver('./temp_zip_file')
"""

# $ pip install selenium
# $ chmod +x geckodriver-install.sh
from selenium import webdriver
browser = webdriver.Firefox()
browser.get(base_url+f_nm)


