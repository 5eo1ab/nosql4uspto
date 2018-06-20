# untility functions for insert_mongo

# $ pip install xmljson
# reference url: https://pypi.org/project/xmljson/
from xmljson import abdera
from xml.etree.ElementTree import fromstring
def convert_XML2Json(f_path):
	with open(f_path) as f:
		data_read = f.read()
	data_json = abdera.data(fromstring(data_read))
	return data_json

"""client = MongoClient('mongodb://35.229.249.155:27017/')
#client = MongoClient('mongodb://localhost:27017/')
db = client['uspto']
collection = db['patent']"""
from pymongo import MongoClient
class MONGO_MANAGER:  # DB manage class
	def __init__(self, db_type, db_name):	
		try:
			client = MongoClient('mongodb://localhost:27017/')
			self.db_connect = client[db_name]
			self.db_type = "mongo"
		except ConnectionRefusedError:
			self.db_connect = None
			self.db_state = False
			print(db_type, "[" + db_name + "] connect Fail")
		else:
			print(db_type, "[" + db_name + "] connect success")	

	def insert(self, target, doc):
		if self.db_connect is not None:
			doc_list = self.db_connect[target]
			doc_list.insert(doc)
			print("DB insert a instance success!")
		else:
			print("DB connect error occur!")

	def insert_many(self, target, docs):
		if self.db_connect is not None:
			doc_list = self.db_connect[target]
			doc_list.insert_many(docs)
			print("DB insert bulk instances success!")
		else:
			print("DB connect error occur!")

def insert_mongo(fpath_list):
	json_list = [convert_XML2Json(fpath) for fpath in fpath_list]
	manager = MONGO_MANAGER(db_type="mongo", db_name="uspto")
	manager.insert_many('patent', json_list)
	return None

