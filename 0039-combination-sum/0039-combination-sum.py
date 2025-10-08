class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        stack=[(0,[],0)]
        while stack:
            i, curr, total = stack.pop()
            if total == target:
                res.append(curr)
                continue
            if i >= len(candidates) or total > target:
                continue
            stack.append((i, curr + [candidates[i]], total + candidates[i]))
            stack.append((i + 1, curr, total))
        return res