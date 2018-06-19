# parallel running for collect weekly_xml files

import sys
import multiprocessing
from multiprocessing import Pool
from script_weekly_xml import weekly_xml_files, get_base_url

if __name__ == '__main__':

	YEAR = sys.argv[1]
	with open('./metadata_zip_file/metadata_{}.csv'.format(YEAR), 'r') as f:
		meta_read = f.read().split('\n')
	f_nm_list = [line.split(',')[0] for line in meta_read[1:] if len(line.split(',')[0])>0]
	print(len(f_nm_list), f_nm_list)

	num_core = multiprocessing.cpu_count()
	multi_proc = Pool(num_core)
	multi_proc.map(weekly_xml_files, f_nm_list)
	
