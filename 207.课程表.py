#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 51/51 cases passed (48 ms)
        # Your runtime beats 26.6 % of python3 submissions
        # Your memory usage beats 38.59 % of python3 submissions (17.2 MB)
        """
        生成有向图，遍历判断是否有环
        """
        graph = self.buildGraph(numCourses, prerequisites)

        # 记录一次 traverse 递归经过的节点
        self.onPath = {}
        # 记录遍历过的节点，防止走回头路
        self.visited = {}
        # 记录图中是否有环
        self.hasCycle = False

        for i in range(numCourses):
            self.traverse(graph, i)

        return not self.hasCycle


    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        return graph

    
    def traverse(self, graph, s):
        # 判断节点s是否在当前路径上
        if s in self.onPath:
            self.hasCycle = True

        if s in self.visited:
            return 

        # 将节点s标记为已遍历
        self.visited[s] = True

        # 开始遍历节点s
        self.onPath[s] = True
        for n in graph[s]:
            self.traverse(graph, n)
        # 节点s遍历完成
        self.onPath.pop(s)

# @lc code=end

