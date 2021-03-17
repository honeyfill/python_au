Array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
## Max Consecutive Ones 

https://leetcode.com/problems/max-consecutive-ones/

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        now = 0
        for i in range(0, len(nums)):
            if (nums[i] == 1):
                now += 1
            else:
                if (max < now):
                    max = now
                now = 0
        if (now > max):
            max = now
        return (max)
```
## Reshape the Matrix 

https://leetcode.com/problems/reshape-the-matrix/

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        out = [[0] * c for i in range(r)]
        if (r*c != len(nums)*len(nums[0]) or len(nums) == 0 or len(nums[0]) == 0):
            return nums
        column = 0
        line = 0
        for i in range (len(nums)):
            for j in range (len(nums[0])):
                out[line][column] = nums[i][j]
                column += 1
                if (column  == c):
                    line += 1
                    column = 0
        return out
```
## Image Smoother 

https://leetcode.com/problems/image-smoother/submissions/

```python
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        out = [[0]*len(M[0]) for i in range (0, len(M))]
        for line in range(len(M)):
            for column in range(len(M[0])):
                round = 0
                for nowline in (line-1, line, line + 1):
                    for nowcolumn in (column -1, column, column + 1):
                        if 0 <= nowline < len(M) and 0 <= nowcolumn < len(M[0]):
                            out[line][column] += M[nowline][nowcolumn]
                            round += 1
                out[line][column] = floor(out[line][column]/round)
        return out
```
## Flipping an Image 

https://leetcode.com/problems/flipping-an-image/submissions/

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        mid = floor(len(A[0])/2)
        for i in range (len(A)):
            for j in range(mid):
                A[i][j], A[i][len(A[0]) - j - 1] = A[i][len(A[0]) - j - 1], A[i][j]
            for j in range(len(A[0])):
                A[i][j] = (A[i][j] + 1)%2
        return A
```
## Transpose Matrix 

https://leetcode.com/problems/transpose-matrix/

```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        out = [[0]*len(A) for i in range (len(A[0]))]
        for i in range (len(A[0])):
            for j in range (len(A)):
                out[i][j] = A[j][i]
        return out
```
## Move Zeroes 

https://leetcode.com/problems/move-zeroes/

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size = len(nums)
        i = 0
        while (i < size):
            if (nums[i] == 0):
                del nums[i]
                nums.append(0)
                size += -1
            else:
                i += 1
```
## Squares of a Sorted Array 

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0 for i in range(len(A))]
        first = 0
        last = len(A) - 1
        count = last
        while (first != last):
            if (abs(A[first]) > abs(A[last])):
                ans[count] = A[first]**2
                first += 1
            else:
                ans[count] = A[last]**2
                last -= 1
            count -= 1
        ans[0] = A[first]**2
        return ans
```
