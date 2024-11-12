#29.两数相除：给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符
def divide(dividend, divisor):
    sign = (dividend > 0) ^ (divisor > 0)  # 异或
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    # 把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1  # 几进位
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count
            # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
            dividend -= divisor
    if sign: result = -result
    return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1

#50．Pow（X, n）
def myPow(x, n) -> float:
    a = abs(n)
    final = 1
    while a > 0:
        if a % 2 == 0:
            x *= x
            a /= 2
        final *= x
        a -= 1
    return final if n > 0 else 1 / final



