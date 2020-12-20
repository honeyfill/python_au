# String

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)
## Valid Anagram 

https://leetcode.com/problems/valid-anagram/

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        symbols = {}
        for sym in s:
            if sym in symbols:
                symbols[sym] += 1
            else:
                symbols[sym] = 1
        for sym in t:
            if sym in symbols:
                symbols[sym] -= 1
            else:
                return False
        for sym in symbols:
            if symbols[sym] != 0:
                return False
        return True
```
## Reverse String 

https://leetcode.com/problems/reverse-string/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range (floor(len(s)/2)):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
```
## Reverse Vowels of a String 

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a':1, 'e':1, 'o':1, 'i':1, 'u':1, 'A':1, 'E':1, 'O':1, 'I':1, 'U':1}
        s = [sym for sym in s]
        first = 0
        last = len(s) - 1
        while (first < last):
            if (s[first] in vowels):
                if (s[last] in vowels):
                    s[first], s[last] = s[last], s[first]
                    first += 1
                    last -= 1
                else:
                    last -= 1
            else:
                first += 1
        return ''.join(s)
```
## Reverse Words in a String III 

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range (len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)
```
## To Lower Case 

https://leetcode.com/problems/to-lower-case/

```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
```
