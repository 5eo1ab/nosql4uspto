# script for summary of files
# collect 2017.1 ~ 2018.6. (until 2018.6.19.)

import os
from pandas import DataFrame as df

list_dir = os.listdir('./temp_file')
#print(len(list_dir))

res_list = list()
for item in list_dir:
	item_path = './temp_file/{}'.format(item)
	if os.path.isfile(item_path):
		f_format, f_size = item.split('.')[-1], os.path.getsize(item_path)
		res_list.append((f_format, item, f_size, 1))
	else: 
		f_size = sum(os.path.getsize('{}/{}'.format(item_path,f)) for f in os.listdir(item_path))
		res_list.append(('dir', item, f_size, len(os.listdir(item_path))))

res_df = df(res_list, columns=['TYPE', 'NAME', 'SIZE(bytes)', 'COUNT_FILES'])
res_df.to_csv('./metadata_zip_file/summary_collect_data.csv', index=False)
print(res_df.head())

