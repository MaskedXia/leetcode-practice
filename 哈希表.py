#166. 分数到小数：给定两个整数，分别表示分数的分子 numerator 和分母 denominator，
# 以字符串形式返回小数。如果小数部分为循环小数，则将循环的部分括在括号内
def fractionToDecimal(numerator, denominator):
    if numerator == 0: return "0"
    res = []
    # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
    if (numerator > 0) ^ (denominator > 0):
        res.append("-")
    numerator, denominator = abs(numerator), abs(denominator)
    # 判读到底有没有小数
    a, b = divmod(numerator, denominator)
    res.append(str(a))
    # 无小数
    if b == 0:
        return "".join(res)
    res.append(".")
    # 处理余数
    # 把所有出现过的余数记录下来
    loc = {b: len(res)}
    while b:
        b *= 10
        a, b = divmod(b, denominator)
        res.append(str(a))
        # 余数前面出现过,说明开始循环了,加括号
        if b in loc:
            res.insert(loc[b], "(")
            res.append(")")
            break
        # 在把该位置的记录下来
        loc[b] = len(res)
    return "".join(res)
#print(fractionToDecimal(2,3))

#202.快乐数:编写一个算法来判断一个数 n 是不是快乐数。
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为1，
# 也可能是无限循环但始终变不到 1。如果可以变为1，那么这个数就是快乐数。
def isHappy(n):
    def next_value(x):
        value = 0
        while x:
            x, cur = divmod(x, 10)
            value += cur ** 2
        return value
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = next_value(n)
    return n == 1
#print(isHappy(19))

