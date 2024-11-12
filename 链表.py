class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

#2.两数相加
'''
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
'''
def addTwoNumbers(l1, l2):
    # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
    start = p = ListNode(None)
    carry = 0  # 初始化进位 s 为 0
    while l1 or l2 or carry:
        # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
        carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        p.next = ListNode(carry % 10)  # p.next 指向新链表, 用来创建一个新的链表
        p = p.next  # p 向后遍历
        carry //= 10  # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
        l1 = l1.next if l1 else None  # 如果l1存在, 则向后遍历, 否则为 None
        l2 = l2.next if l2 else None  # 如果l2存在, 则向后遍历, 否则为 None
    return start.next  # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点
# l1 = ListNode(7)
# l1.next = ListNode(4)
# l1.next.next = ListNode(8)
# l2 = ListNode(7)
# l2.next = ListNode(4)
# l2.next.next = ListNode(8)
# print(addTwoNumbers(l1,l2).next.val)

