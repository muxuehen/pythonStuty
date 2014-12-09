#coding=utf-8
'''
Created on 2014年12月9日

@author: 
日志写入
'''
import logging
import os
LOG ='resource/pythonStudy.log'
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=os.path.join(os.path.pardir,LOG),
                filemode='w')
logging.info('Starting write log...')
