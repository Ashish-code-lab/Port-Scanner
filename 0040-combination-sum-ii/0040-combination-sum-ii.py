class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])

                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result