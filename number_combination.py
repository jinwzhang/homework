import copy

"""
数字组合
author: zhangjinwei

"""
def growth(n):
    knowleage = {2: [[1, 1]]}  # 知识库

    def study(x):
        knowleage_key = set(knowleage.keys())
        last_knowleage = copy.deepcopy(knowleage[x - 1])
        [i.append(1) for i in last_knowleage] # 取之前的知识，加后缀1
        new_knowleage = [[x-1, 1]]
        for i in knowleage_key:
            if x % i != 1:
                combine = [i] * (x//i)
                if x % i != 0:
                    combine.append(x % i)
                new_knowleage.append(combine)

        new_knowleage.extend(last_knowleage)
        new_knowleage.sort(reverse=True)
        knowleage[x] = new_knowleage

    for i in range(n + 1):
        knowleage_key = set(knowleage.keys())
        if i not in knowleage_key and i > 2:
            study(i)  # 学习
    print(knowleage[n])


if __name__ == '__main__':
    while True:
        a = int(input('键入数字: '))
        growth(a)
