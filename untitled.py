# test script
# source url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import requests
from bs4 import BeautifulSoup as bs4bs
from pandas import DataFrame as df

yr4collect = 2018
base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/{}/".format(yr4collect)

res = requests.get(base_url)
soup = bs4bs(res.text, 'html.parser')
print(type(res))

tr_list, records = soup.find_all('tr'), list()
key_list = tr_list[0].get_text(separator='$').split('$')
for tr in tr_list[1:]:
	items = tr.get_text(separator='$').split('$')
	records.append(tuple(items))
data_write = df.from_records(records, columns=key_list)
print(data_write.head())

if not os.path.exists('./metadata_zip_file'):
	os.makedirs('./metadata_zip_file')
data_write.to_csv('./metadata_zip_file/metadata_{}.csv'.format(yr4collect), index=False)
