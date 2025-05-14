def combinationSum2(candidates, target):
    candidates.sort()
    results = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            results.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

    backtrack(0, [], target)
    return results


candidates1 = [2, 5, 2, 1, 2]
target1 = 5
print(combinationSum2(candidates1, target1))

candidates2 = [10, 1, 2, 7, 6, 1, 5]
target2 = 8
print(combinationSum2(candidates2, target2))
