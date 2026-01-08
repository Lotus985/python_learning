db = {}
with open("file_message.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    # print(data)
    for i in data:
        ret = i.strip().split("|")
        # ret = ["张三", "123"]
        # print(ret)
        db[ret[0]] = ret[1]
        # db["张三"] = "123"
        # print(db)

i = 0
while True:
    username = input("请输入用户名：")

    if username in db:

        password = input("请输入密码：")

        if password == db[username]:
            print("登录成功!")
            break
        if i <= 2:
            i += 1
            print(f"第{i}次密码输入错误,登录失败!")
        else:
            print("账户已被冻结！")
            break

    else:
        print("用户名不存在")

        file = open('file_message.txt', 'a', encoding='utf-8')

        new_username = input("请创建新的用户名：")
        initial_password = input("请设置初始密码：")

        new_message = new_username + "|" + initial_password
        file.write(new_message)

        print("用户创建完成！")
        # 关闭文件
        file.close()
        break
    break
# 可以通过定义全局变量，在内层循环中通过改变其值控制外层循环。eg.全局变量：flag = 1,内层循环：flag = 0。