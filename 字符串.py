#3.无重复最长字串：给定字符串，找出不含重复字符的最长子串长度(滑动窗口)
def lengthOfLongestSubstring(s):
    if not s: return 0  # 空集返回0
    left = 0  # 字串最左边元素，不断的弹出左边元素直到满足要求
    lookup = set()
    max_len = 0
    cur_len = 0
    for i in range(len(s)):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len: max_len = cur_len
        lookup.add(s[i])  # 集合的remove和add操作
    return max_len
#print(lengthOfLongestSubstring("asdasdaaa"))

#76.最小覆盖字串：给两个字符串S、T，在S中找出包含T所有字符最小子串
from collections import Counter
def minWindow(s, t):
    if not t or not s:
        return ""
    dict_t = Counter(t)#生成计数字典
    dict_tlen = len(dict_t)
    filter_s = []
    for i, c in enumerate(s):
        if c in dict_t:
            filter_s.append((i, c))
    window = {}
    cur_len = 0
    ans = float('inf'),None,None
    l = r = 0
    while r < len(filter_s):
        charactor = filter_s[r][1]
        window[charactor] = window.get(charactor,0) + 1
        if window[charactor] == dict_t[charactor]:
            cur_len += 1
        while l <= r and cur_len == dict_tlen:
            charact = filter_s[l][1]
            start = filter_s[l][0]
            end = filter_s[r][0]
            if end-start+1 < ans[0]:
                ans = (end - start + 1, start, end)
            window[charact] -= 1
            l += 1
            if window[charact] < dict_t[charact]:
                cur_len -= 1
        r += 1
    return "" if ans[0] == float('inf') else s[ans[1] : ans[2]+1]
#print(minWindow("ADOBECODEBANK", "ABC"))

#165.比较版本号:比较两个版本号 version1 和 version2。
# 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
def compareVersion(version1, version2):
    nums1 = version1.split('.')
    nums2 = version2.split('.')
    n1, n2 = len(nums1), len(nums2)
    # compare versions
    for i in range(max(n1, n2)):
        i1 = int(nums1[i]) if i < n1 else 0  # 补0
        i2 = int(nums2[i]) if i < n2 else 0
        if i1 != i2:
            return 1 if i1 > i2 else -1
    # the versions are equal
    return 0
#print(compareVersion("2.5.1", "2.5.2"))


