# -*- coding: utf-8 -*-

import os

os.system("ipconfig")


from os import system,popen
#from os import *    不建议使用这种方法
system("dir")#上下两种使用os的方法都可以，下面的更具体
res1 = popen("dir").read()
print (">>"),res1


import commands
res = commands.getoutput("ipconfig")#获取输出并打印
print (">>>>"),res