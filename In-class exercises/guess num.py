import random
i = 0
while True:
    num = random.randint(1, 100)
    while i<5:
        guess = int(input("请输入你要猜的数字:"))
        i+= 1
        if guess < num:
            print("猜小了")
            print(f"你已经猜了{i}次")
        elif guess > num:
            print("猜大了")
            print(f"你已经猜了{i}次")
        elif guess == num:
            print("猜对了")
            print(f"你已经猜了{i}次")
            break
    if i == 5:
        print("请重新输入你要猜的数")
        i = 0
    continue