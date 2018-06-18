# source url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import pandas as pd

base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/"

def set_work_dir(f_nm):
	if not os.path.exists('./utility'):
		print("!!!!!!!!!!!! install geckodriver (for selenium) !!!!!!!!!!!!")
		print("reference: setting_utility.md")
		import sys
		sys.exit()
	if not os.path.exists('./temp_zip_file'): os.makedirs('./temp_zip_file')
	if not os.path.exists('./temp_xml_file'): os.makedirs('./temp_xml_file')
	if not os.path.exists('./temp_xml_file/{}'.format(f_nm[:-4])):
		os.makedirs('./temp_xml_file/{}'.format(f_nm[:-4]))
	return None

def weekly_xml_files(f_nm):
	set_work_dir(f_nm)
	# $ pip install selenium
	from selenium import webdriver
	fp = webdriver.FirefoxProfile()
	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("browser.download.manager.showWhenStarting",False)
	fp.set_preference("browser.download.dir", os.getcwd()+'/temp_zip_file')
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip, application/x-zip, application/x-zip-compressed, application/download")
	fp.set_preference("browser.download.panel.shown", False)

	browser = webdriver.Firefox(firefox_profile=fp)
	browser.get(base_url+f_nm)
	browser.find_element_by_css_selector('a[title="Click to Download"]').click()
	browser.close()
	print("download ZIP file: {}".format(f_nm))

	import zipfile
	zip_f = zipfile.ZipFile('./temp_zip_file/{}'.format(f_nm), 'r')
	zip_f.extractall('./temp_zip_file')
	zip_f.close()
	print("unzip ZIP file: {}".format(f_nm))

	split_sep = '<?xml version="1.0" encoding="UTF-8"?>'
	with open('./temp_zip_file/{}.xml'.format(f_nm[:-4]), 'r') as fr:
		data_read = fr.read()
		doc_list = data_read.split(split_sep)[1:]
		for idx, doc in enumerate(doc_list):
			with open('./temp_xml_file/{}/{}.xml'.format(f_nm[:-4], idx), 'w') as fw:
				fw.write(split_sep)
				fw.write(doc_list[idx])
	print("split XML file: {}".format(f_nm))
	return None

if __name__ == '__main__':
	meta = pd.read_csv('./metadata_zip_file/metadata_2018.csv')
	print(meta.shape)

	f_idx = 2
	f_nm = meta[meta.columns[0]][f_idx]

