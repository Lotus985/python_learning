#file = open('example.txt','r',encoding='utf-8')

# content = file.read()
# file.seek(0)
# line = file.readline()
# file.seek(0)
# lines = file.readlines()
# lines = [line.strip() for line in lines]
# print(content)
# print(line)
# print(lines)
# i = 1
# while True:
#     text1 = file.readline().strip()
#     if text1:
#         print("这是第%s行的内容"%i)
#         #print(f"这是第{i}行的内容")
#         i +=1
#         print(text1)
#     else:
#         break
# file.close()
# for i in file.readlines():
#     print(i.strip())
#
# file.close()

# content = input("请输入今天的文档：")
# file.write(content + "\n")
# print("文档已保存！")
# file.close()
# file.write(file.read()+"\n")  #如果这样的话每天都得改代码。
# file.write(input("请输入今天的文档信息：")+"\n") #这样无需每日更改。
# print("文档已保存！")

# with open('example.txt','r') as file:
#     content = file.read()

# source = 'example.txt'
# destination = 'b.txt'
#
# with open(source,'r',encoding='utf-8') as src:
#     content = src.read()
#
# with open(destination,'w',encoding='utf-8') as dest:
#     dest.write(content)
#
# print(f"备份成功！'{source}'的内容已复制到'{destination}'")

# import os
#
# with open('example.txt',encoding='utf-8') as read_f,open('example.txt', 'w', encoding='utf-8') as write_f:
#     data = read_f.read()
#     data = data.replace('Hello','nihao')
#     write_f.write(data)
#
# os.remove('example.txt')
# os.rename('example.txt', 'example.txt')

# products = []
#
# with open('a.txt', 'r') as file:
#     for line in file:
#         parts = line.strip().split()
#         if len(parts) == 3:
#             product = {
#                 'name': parts[0],
#                 'price': int(parts[1]),
#                 'amount': int(parts[2])
#             }
#             products.append(product)
#
# print("商品列表", products)
#
# total_price = 0
#
# for i in products:
#     total_price += i['price'] * i['amount']
#
# print("总价:",total_price)

# db = {}
# with open('db.txt', 'r',encoding="utf-8") as f:
#     data = f.readlines()
#     for i in data:
#         ret = i.strip().split("|")
#         # ret = ["张三","123"]
#         db[ret[0]] = ret[1] # 指定键值对
#         # db["张三"] = "123"]
#
# while True:
#     username = input("请输入用户名：")
#
#     if username in db:
#         password = input("请输入密码:")
#         if password == db[username]:
#             print("登录成功")
#             break
#         else:
#             print("密码错误，登录失败")
#     else:
#         print("用户不存在")

