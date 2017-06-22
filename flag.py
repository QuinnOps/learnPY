# -*- coding: utf-8 -*
password = "test"
logout_flag = False

for i in range (4):
    passwd = raw_input ("Please input password:").strip()
    if len(passwd) == 0 : continue
    if passwd == password :
        while True :
            print  "Welcome to login !"
            user_choice = raw_input('''
            1、你吃饭都是裸考
            2、sdm
            3、exit
            4、退出程序
            ''').strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print ("dfsfdsfdfs")
            if user_choice == 2:
                print ("sdm")
            if user_choice == 3:
                print ("exit")
                break
            if user_choice == 4:
                logout_flag = True
                break
        if logout_flag:
            print ("ending...")
            break
        print ("logout...")









