def main():
    while True:
        user_input=input("r注册，l登录，q退出")

        if user_input=='r':
            username = input("用户名")
            password = input("密码")
            print("注册成功")
        elif user_input == 'l':
            login_username = input("用户名")
            login_password = input("密码") 
            if login_username == username and login_password == password:
                print("登录成功")   
            else:
                print("登录失败")
        elif user_input == 'q':
            print("退出程序")
            break
        else:
            print("输入错误")
if __name__ == "__main__":
    main()
