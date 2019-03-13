#! -*- coding:utf-8 -*-
import csv

def database_to_file(data,file_name,headline=None):
	'''
	将数据库读出来的文件写入csv文件
	'''
	with open(file_name,'w',newline='') as f:
		if headline == None:
			writer = csv.writer(f)
			writer.writerows(data)
		else:
			writer = csv.writer(f)
			writer.writerow(headline)
			writer.writerows(data)

def data_to_file(data,file_name,mode='w'):
	'''
	将数据库读出来的文件写入txt文件,默认是重新写入数据，
	当mode='a'，则为在之前的基础上新增数据,主要写入单列数据
	'''
	with open(file_name,mode) as f:
		for line in data:
			f.write(line + '\n')
