#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """广义优先搜索：BFS -- 迭代"""
        if target == "0000":
            return 0
        if target in deadends or "0000" in deadends:
            return -1
        seen = {"0000"}
        depth = 0
        queue = [["0000"]]
        while queue:
            q = queue.pop()
            tmp = []
            for node in q:
                if node == target:
                    return depth
                res, seen = self.nextNode(node, seen, deadends)
                tmp += res
            if tmp:
                queue.append(tmp)
            depth += 1
        return -1

    def nextNode(self, node, seen, deadends):
        res = []
        for i in range(4):
            up = node[:i] + str((int(node[i]) + 1) % 10) + node[i+1:]
            if node[i] == "0":
                down = node[:i] + "9" + node[i+1:]
            else:
                down = node[:i] + str(int(node[i]) - 1) + node[i+1:]
            if up not in seen and up not in deadends:
                seen.add(up)
                res.append(up)
            if down not in seen and down not in deadends:
                seen.add(down)
                res.append(down)
        return res, seen
# @lc code=end

