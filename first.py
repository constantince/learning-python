words = ["cat", "dot", "defenstrate"]
for w in words:
    print(w, len(w))


# new func start
def fib(arg, t="2", c="8"):
    pass
    print("am i dome")
    return arg + "python is good" + t + c

m = fib("go", "bad", "good");

print(m)

from urllib.request import urlopen
with urlopen('https://www.baidu.com') as response:
    for line in response:
        print(line)
