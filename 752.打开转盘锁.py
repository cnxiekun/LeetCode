#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # """广义优先搜索：BFS -- 迭代"""
        # # 48/48 cases passed (1108 ms)
        # # Your runtime beats 22.01 % of python3 submissions
        # # Your memory usage beats 23.17 % of python3 submissions (16.2 MB)
        # if target == "0000":
        #     return 0
        # if target in deadends or "0000" in deadends:
        #     return -1
        # seen = {"0000"}
        # depth = 0
        # queue = [["0000"]]
        # while queue:
        #     q = queue.pop()
        #     tmp = []
        #     for node in q:
        #         if node == target:
        #             return depth
        #         res, seen = self.nextNode(node, seen, deadends)
        #         tmp += res
        #     if tmp:
        #         queue.append(tmp)
        #     depth += 1
        # return -1
        """双向广义优先搜索：双向BFS -- 迭代"""
        # 48/48 cases passed (332 ms)
        # Your runtime beats 82.47 % of python3 submissions
        # Your memory usage beats 91.67 % of python3 submissions (15.5 MB)
        if target == "0000":
            return 0
        if target in deadends or "0000" in deadends:
            return -1
        seen_start, seen_end = {"0000"}, {target}
        depth = 0
        queue_start, queue_end = [["0000"]], [[target]]
        while queue_start and queue_end:
            q_s = queue_start.pop()
            q_e = queue_end.pop()
            tmp_s = []
            tmp_e = []
            for node in q_s:
                if node in q_e:
                    return 2*depth
                res, seen_start = self.nextNode(node, seen_start, deadends)
                tmp_s += res
            if tmp_s:
                queue_start.append(tmp_s)

            for node in q_e:
                if node in tmp_s:
                    return 2*depth + 1
                res, seen_end = self.nextNode(node, seen_end, deadends)
                tmp_e += res
            if tmp_e:
                queue_end.append(tmp_e)
            
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

