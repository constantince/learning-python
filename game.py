import random
rules = ["rock", "scissor", "paper"]
computer = rules[random.randint(0, 2)]
print(computer)
me = input("出拳吧，侠士:")
counts = rules.count(me)
if(counts == 0):
    print("你耍赖")
    exit();

if computer == me:
    print("平局")
elif computer == "rock" and me == "paper":
    print("赢了")
elif computer == "scissor" and me == "rock":
    print("赢了")
elif computer == "paper" and me == "scissor":
    print("赢了")
else:
    print("输了")
