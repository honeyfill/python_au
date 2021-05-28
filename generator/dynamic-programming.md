# Dynamic Programming

+ [House Robber](#house-robber)
+ [House Robber II](#house-robber-ii)
## House Robber 

https://leetcode.com/problems/house-robber/

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_ago = max_last = 0
        for value in nums:
            tmp = max_ago
            max_ago = max_last
            max_last = max(tmp + value, max_last)
        return max_last
```
## House Robber II 

https://leetcode.com/problems/house-robber-ii/

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        for i in range(len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            ans = max(ans, dp[i])
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            ans = max(ans, dp[i])
        return ans
```
