# script for metadata_zip_files
"""
# source url: https://bulkdata.uspto.gov/#rsrch
Patent Grant Full Text Data (No Images) (JAN 1976 - PRESENT)
Contains the full text of each patent grant issued weekly (Tuesdays) from January 1, 1976 to present (excludes images/drawings). Subset of the Patent Grant Full Text Data with Embedded TIFF Images.
"""
# base url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import requests
from bs4 import BeautifulSoup as bs4bs
from pandas import DataFrame as df

if not os.path.exists('./metadata_zip_file'):
	os.makedirs('./metadata_zip_file')

def get_url_from_year(yr4collect):
	base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/{}/".format(yr4collect)
	return base_url

def get_df_from_url(base_url):
	res = requests.get(base_url)
	soup = bs4bs(res.text, 'html.parser')
	
	tr_list, records = soup.find_all('tr'), list()
	key_list = tr_list[0].get_text(separator='$').split('$')
	for tr in tr_list[1:]:
		items = tr.get_text(separator='$').split('$')
		records.append(tuple(items))
	data_write = df.from_records(records, columns=key_list)
	#print(data_write.head())
	return data_write

if __name__ == '__main__':
	for yr in range(2002, 2018+1):
		print("collect metadata for zip files @ {}".format(yr))
		url = get_url_from_year(yr)
		data = get_df_from_url(url)
		data.to_csv('./metadata_zip_file/metadata_{}.csv'.format(yr), index=False)
	print("End.")