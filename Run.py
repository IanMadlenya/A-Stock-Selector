'''
Created on Jan, 13, 2016

@author: Hanjie
'''

#from utils.pathtool import *


from dataSpider import * 

import os.path

if __name__ == '__main__':
    if(not os.path.exists("./conf.ini")):
        print("Conf.int file is missing, exiting...")
        exit
    else:
        print ("Start to read the configuration file from ./conf.ini ...")
        dataSpiderConfig = dataSpider("conf.ini")
        print(dataSpiderConfig._configDic)
        print(dataSpiderConfig._configDic['sina']['url'])
        
          
        
       
