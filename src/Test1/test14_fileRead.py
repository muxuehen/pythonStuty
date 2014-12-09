#coding=utf-8
'''
Created on 2014年12月9日

@author: zxl
读取文件测试
'''
import os
from ConfigParser import ConfigParser
CONFIGFILE ='resource/python.txt'
config = ConfigParser()
#os.path.pardir是父目录，
#os.path.abspath是绝对路径
config.read(os.path.join(os.path.pardir,CONFIGFILE))
print config.get('messages','greeting')
raduis = input(config.get('messages', 'question')+' ')
print config.get('messages','result_msg')
print config.getfloat('numbers','pi') * raduis**2
