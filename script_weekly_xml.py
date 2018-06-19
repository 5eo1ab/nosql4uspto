# source url: https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2018/

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

def weekly_xml_files(f_nm, base_url):
	set_work_dir(f_nm)
	# [1] download ZIP file from USPTO
	if os.path.exists('./temp_file/{}'.format(f_nm)):
		print("[1] exists ZIP file: {}".format(f_nm))
	else:
		# $ pip install selenium
		from selenium import webdriver
		c_options = webdriver.ChromeOptions()
		prefs = {"download.default_directory" : os.getcwd()+'/temp_file'}
		#c_options.add_argument("--headless")
		c_options.add_experimental_option("prefs",prefs)
		cd_dir = '/usr/lib/chromium-browser/chromedriver'
		browser = webdriver.Chrome(executable_path=cd_dir, chrome_options=c_options)
		""" # setting for firefox (didn't work terminal env.)
		fp = webdriver.FirefoxProfile()
		fp.set_preference("browser.download.folderList",2)
		fp.set_preference("browser.download.manager.showWhenStarting",False)
		fp.set_preference("browser.download.dir", os.getcwd()+'/temp_file')
		fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip, application/x-zip, application/x-zip-compressed, application/download")
		fp.set_preference("browser.download.panel.shown", False)
		browser = webdriver.Firefox(firefox_profile=fp)
		#browser.set_page_load_timeout(500) # default : 300
		"""
		try:
			browser.get(base_url+f_nm)
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
	base_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/{}/".format(YEAR)
	weekly_xml_files(f_nm, base_url)
	