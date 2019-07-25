# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(nums, temp):
            if len(temp) == len(nums):
                self.res.append(temp[:])

            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()

        dfs(nums, [])
        return self.res

# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())

# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        if n % 2 == 1:
            return x*self.myPow(x, n-1)

# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, bottom):
                res.append(matrix[i][right])
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
        elif top == bottom:
            for i in range(left, right + 1):
                res.append(matrix[bottom][i])
        return res
