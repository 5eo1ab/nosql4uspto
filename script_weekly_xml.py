# script for weekly_xml functions
# base url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

import os
import sys

def set_work_dir(f_nm):
	if not os.path.exists('/usr/lib/chromium-browser/chromedriver'):
		print("!!!!!!!!!!!! install chrome-webdriver (for selenium) !!!!!!!!!!!!")
		print("reference: setting_utility.md")
		import sys
		sys.exit()
	if not os.path.exists('./temp_file'): os.makedirs('./temp_file')
	if not os.path.exists('./temp_file/{}'.format(f_nm[:-4])):
		os.makedirs('./temp_file/{}'.format(f_nm[:-4]))
	return None
def get_base_url(f_nm):
	year = '20{}'.format(f_nm[3:5])
	print(year)
	base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/{}/{}".format(year, f_nm)
	return base_url

def weekly_xml_files(f_nm):
	set_work_dir(f_nm)
	# [1] download ZIP file from USPTO
	if os.path.exists('./temp_file/{}'.format(f_nm)):
		print("[1] exists ZIP file: {}".format(f_nm))
	else:
		from selenium import webdriver
		c_options = webdriver.ChromeOptions()
		prefs = {"download.default_directory" : os.getcwd()+'/temp_file'}
		c_options.add_experimental_option("prefs",prefs)
		cd_dir = '/usr/lib/chromium-browser/chromedriver'
		browser = webdriver.Chrome(executable_path=cd_dir, chrome_options=c_options)
		try:
			browser.get(get_base_url(f_nm))
			import time
			while not os.path.exists('./temp_file/{}'.format(f_nm)):
				print('#', end='')
				time.sleep(10)
			browser.close()
		except Exception as e:
			print("Exception Msg.: {}".format(e))
		print("\n[1] download ZIP file: {}".format(f_nm))
	# [2] unzip ZIP file to concatnated XML file
	if os.path.exists('./temp_file/{}.xml'.format(f_nm[:-4])):
		print("[2] exists unziped ZIP file: {}".format(f_nm))
	else:
		import zipfile
		zip_f = zipfile.ZipFile('./temp_file/{}'.format(f_nm), 'r')
		zip_f.extractall('./temp_file')
		zip_f.close()
		print("[2] unzip ZIP file: {}".format(f_nm))
	# [3] split concatnated XML file to separated XML files
	if os.path.exists('./temp_file/{}/0.xml'.format(f_nm[:-4])):
		print("[3] exists splited XML file: {}".format(f_nm))
	else:
		split_sep = '<?xml version="1.0" encoding="UTF-8"?>'
		with open('./temp_file/{}.xml'.format(f_nm[:-4]), 'r') as fr:
			data_read = fr.read()
			doc_list = data_read.split(split_sep)[1:]
			for idx, doc in enumerate(doc_list):
				with open('./temp_file/{}/{}.xml'.format(f_nm[:-4], idx), 'w') as fw:
					fw.write(split_sep)
					fw.write(doc_list[idx])
		print("[3] split XML file: {}".format(f_nm))
	return None

if __name__ == '__main__':

	#YEAR, IDX = 2018, 11
	YEAR, IDX = sys.argv[1], int(sys.argv[2])
	if IDX < 1: sys.exit()

	with open('./metadata_zip_file/metadata_{}.csv'.format(YEAR), 'r') as f:
		meta_read = f.read().split('\n')
	f_nm = meta_read[IDX].split(',')[0]
	print("file name: {}".format(f_nm))
	weekly_xml_files(f_nm)
	