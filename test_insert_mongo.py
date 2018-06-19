# convert xml to json, then insert to mongodb for test.

import os
from lib_insert_mongo import convert_XML2Json
from lib_insert_mongo import MONGO_MANAGER

if __name__ == '__main__':

	path_list = list()
	list_dir = os.listdir('./sample_file')
	for dir_sm in list_dir:
		for xml_sm in os.listdir('./sample_file/{}'.format(dir_sm)):
			path_list.append('./sample_file/{}/{}'.format(dir_sm, xml_sm))
	print(len(path_list))
	json_list = [convert_XML2Json(path) for path in path_list]
	#print(json_list[0])

	manager = MONGO_MANAGER(db_type="mongo", db_name="uspto")
	manager.insert('patent', json_list[0])
	manager.insert_many('patent', json_list[1:])

