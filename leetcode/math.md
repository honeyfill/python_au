#Math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)
## Reverse Integer 

https://leetcode.com/problems/reverse-integer/

```python
class Solution:
    def reverse(self, x: int) -> int:
        upper = (2**31) - 1
        lower = -(2**31)
        if x >= upper or x <= lower:
            return 0
        sign = ''
        if (x < 0):
            sign = '-'
        line = str(abs(x))
        line = sign + line[::-1]
        ans = int(line)
        if ans >= upper or ans <= lower:
            return 0
        return ans

```
## Palindrome Number 

https://leetcode.com/problems/palindrome-number/

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numerals = []
        old = x
        numerals.append(x%10)
        count = 0
        while x:
            x = x//10
            if x:
                numerals.append(x%10)
                count += 1
        for i in range(count + 1):
            x += numerals[i]*(10**count)
            count -= 1
        if (old == x):
            return True
        return False

```
## Fizz Buzz 

https://leetcode.com/problems/fizz-buzz/

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            else:
                if i % 3 == 0:
                    ans.append('Fizz')
                else:
                    if i % 5 == 0:
                        ans.append('Buzz')
                    else:
                        ans.append(str(i))
        return ans

```
## Base 7 

https://leetcode.com/problems/base-7/

```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        nums = ''
        sign = ''
        if num < 0:
            sign = '-'
        value = abs(num)
        while (value > 0):
            nums = str(value%7) + nums
            value = value//7
        ans = "".join(nums)
        return sign + ans

```
## Fibonacci Number 

https://leetcode.com/problems/fibonacci-number/

```python
class Solution:
    def fib(self, N: int) -> int:
        const = (1 + 5**0.5)/2
        ans = int((const ** N + 1)/5 ** 0.5)
        return ans

```
## Largest Perimeter Triangle 

https://leetcode.com/problems/largest-perimeter-triangle/

```python
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        i = len(A) - 1
        while (i > 1):
            if (A[i] < A[i-1] + A[i-2]):
                return A[i]+A[i-1]+A[i-2]
            i -= 1
        return 0

```
## Sqrt(x) 

https://leetcode.com/problems/sqrtx/

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = x
        mid = 0
        while (right - left > 1):
            mid = (left + right)//2
            if x > mid**2:
                left = mid
            else:
                if x < mid**2:
                    right = mid
                else:
                    return mid
        return left

```
