import random
# random产生随机值或者从给定值中随机选择

# 可选择的选项
options = ["石头", "剪子", "布"]
j = 0
result_list = []

print("欢迎来到石头剪子布游戏！")
print("请从以下选项中选择：")
while True:
    if j <= 2:
        j += 1
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        # 玩家选择
        player_choice = int(input("请输入你的选择（1-3）：")) - 1

        # 计算机随机选择
        computer_choice = random.randint(0, 2)

        print(f"\n你选择了：{options[player_choice]}")
        print(f"计算机选择了：{options[computer_choice]}")

        # 判断胜负
        if player_choice == computer_choice:
            print("平局！")
            result_list.append("平局!")
        elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
            print("你赢了！🎉")
            result_list.append("你赢了!")
        else:
            result_list.append("你输了！")

    if j > 2:
        print("猜拳结束！")
        j=0
        break
    continue
# print(result_list)
from collections import Counter
counter = Counter(result_list)
frequency_list = counter.most_common() # 默认按频次降序排列
print(frequency_list)

# 1. 显示所有结果
# print(f"全部对局记录: {result_list}")
# print(f"胜负统计: {frequency_list}")

# 2. 判断最终胜负
win_count = result_list.count("你赢了!")
lose_count = result_list.count("你输了!")
draw_count = result_list.count("平局!")

print("\n最终胜负判定:")
if win_count > lose_count:
    print("🎉 恭喜！你赢得了本次比赛！")
elif win_count < lose_count:
    print("💻 计算机赢得了本次比赛！")
else:
    print("🤝 本次比赛平局！")

print(f"（战绩：{win_count}胜 {lose_count}负 {draw_count}平）")
