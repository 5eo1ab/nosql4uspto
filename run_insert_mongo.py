# parallel running for run insert_mongo

import os, sys
import multiprocessing
from multiprocessing import Pool
from lib_insert_mongo import insert_mongo, convert_XML2Json

if __name__ == '__main__':

	YEAR = sys.argv[1]
	with open('./metadata_zip_file/metadata_{}.csv'.format(YEAR), 'r') as f:
		meta_read = f.read().split('\n')
	header_list = [line.split(',')[0].split('.')[0] for line in meta_read[1:] if len(line.split(',')[0])>0]
	print(len(header_list), header_list)

	param_list = list()
	for i, header in enumerate(header_list):
		json_list = [convert_XML2Json(path) for path in os.listdir('./temp_file/{}'.format(header))]
		param_list.append(json_list)
		print("{}/{}\tCount: {}".format(i+1, len(header_list), len(json_list)))
		
	num_core = multiprocessing.cpu_count()
	multi_proc = Pool(num_core)
	multi_proc.map(insert_mongo, param_list)

