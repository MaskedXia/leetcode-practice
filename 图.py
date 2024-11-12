#207.课程表
'''你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
'''
from collections import deque
def canFinish( numCourses, prerequisites):
    indegrees = [0 for _ in range(numCourses)] #入度
    adjacency = [[] for _ in range(numCourses)] #入度表
    queue = deque()
    # Get the indegree and adjacency of every course.
    for cur, pre in prerequisites:
        indegrees[cur] += 1
        adjacency[pre].append(cur)
    # Get all the courses with the indegree of 0.
    for i in range(len(indegrees)):
        if not indegrees[i]: queue.append(i) #0进入队列表示可直接学习
    # BFS TopSort.
    while queue:
        pre = queue.popleft() #弹出一个
        numCourses -= 1 #总课程减一
        for cur in adjacency[pre]:
            indegrees[cur] -= 1 #对应的所有后续课程入度减一
            if not indegrees[cur]: queue.append(cur)#0进入队列可学习
    return not numCourses#课程为0表示全部学完

#332.重新安排行程（欧拉回路）
'''给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。
说明:
如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''
def findItinerary(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    res = []
    for x, y in sorted(tickets)[::-1]:
        graph[x].append(y)
    def dfs(tmp):
        while graph[tmp]:
            dfs(graph[tmp].pop())
        res.append(tmp)
    dfs("JFK")
    return res[::-1]
