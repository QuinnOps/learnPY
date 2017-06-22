# -*- coding: utf-8 -*

#读文件
# f = file("test.txt")
# #print f.readlines()
# for line in f.readlines():
#     print line,
'''
#写文件
f = file("test1.txt", "w")
f.write("这是第一行\n")
f.write("这是第二行\n")
f.close()

#追加
f = file("test1.txt","a")
f.write("这是第三行,追加\n")
f.close()'''

#修改（read and write :r+ 读写  w+ 写读）
f = file("test1.txt", "r+")
print 'first line:',f.readline()
print 'second line:',f.readline()
f.write("change third line")
f.close()







