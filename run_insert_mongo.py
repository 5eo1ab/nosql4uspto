# parallel running for run insert_mongo

import os, sys, random
import multiprocessing
from multiprocessing import Pool
import shutil
from lib_insert_mongo import insert_mongo

if __name__ == '__main__':

	YEAR, LOOP_SIZE = sys.argv[1], 5
	with open('./metadata_zip_file/metadata_{}.csv'.format(YEAR), 'r') as f:
		meta_read = f.read().split('\n')
	tailer_list = [line.split(',')[0].split('.')[0] for line in meta_read[1:] if len(line.split(',')[0])>0]
	print(len(tailer_list))

	while len(tailer_list) > 0:
		if len(tailer_list) < LOOP_SIZE:
			header_list, tailer_list = tailer_list, list()
		else:
			header_list, tailer_list = tailer_list[:LOOP_SIZE], tailer_list[LOOP_SIZE:]
		#print(len(header_list), len(tailer_list))

		param_list = list()
		for header in header_list:
			header_dir = './temp_file/{}'.format(header)
			fpath_list = ['{}/{}'.format(header_dir, xmlf) for xmlf in os.listdir(header_dir)]
			param_list.append(fpath_list)
			print("loop: {}\theader: {}\t count: {}".format(LOOP_SIZE, header, len(fpath_list)))			
		try:
			num_core = multiprocessing.cpu_count()
			multi_proc = Pool(num_core)
			print("parallel proc.: {}".format(header_list))
			multi_proc.map(insert_mongo, param_list)
			for header in header_list:
				header_dir = './temp_file/{}'.format(header)
				shutil.rmtree(header_dir, ignore_errors=True)
			print("parallel rm.: {}".format(header_list))
		except Exception as ex:
			print("Exception Msg.: {}".format(ex))	

