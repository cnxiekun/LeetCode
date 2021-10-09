#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        多叉树遍历框架
        """
        # 30/30 cases passed (52 ms)
        # Your runtime beats 20.08 % of python3 submissions
        # Your memory usage beats 66.14 % of python3 submissions (16.1 MB)
        self.res = []
        path = []
        self.traverse(graph, 0, path)
        return self.res


    def traverse(self, graph, s, path):
        # 路径添加当前节点 s
        path.append(s)

        if s == len(graph) - 1:
            # 到达尾结点 len(graph) - 1
            self.res.append(path[:])
            path.pop()
            return
        
        # 递归
        for v in graph[s]:
            self.traverse(graph, v, path)
        
        # 从路径中移除当前节点 s
        path.pop()
# @lc code=end

