# 例子1：字符串abcabcbb，当前无重复最长字串  bbbbb
def getlens(s):
    if len(s) == 0:
        return 0
    lens = len(s)
    start = 0
    cur_len = 0
    max_len = 0
    t = set()
    for i in range(lens):
        cur_len += 1
        while s[i] in t:
            t.remove(s[start])
            start += 1
            cur_len -= 1
        t.add(s[i])
        max_len = max(max_len, cur_len)
    return max_len
print(getlens("bbbbb"))



