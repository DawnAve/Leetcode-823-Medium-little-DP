class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        count = {}
        for i in arr:
            count[i] = 1
            for j in arr:
                if j>=i:
                    break
                else:
                    if i % j == 0 and i//j in arr:
                        count[i] += count[j] * count[i//j]

        total = sum(count.values())
        return total % (10**9 +7)
