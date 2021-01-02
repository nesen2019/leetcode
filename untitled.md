123




## 679. 24 点游戏
```text 
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

```
- python 
```python 
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)
```

## 214. 最短回文串
```text 
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

 

示例 1：

输入：s = "aacecaaa"
输出："aaacecaaa"
示例 2：

输入：s = "abcd"
输出："dcbabcd"
 

提示：

0 <= s.length <= 5 * 104
s 仅由小写英文字母组成
# https://leetcode-cn.com/problems/shortest-palindrome/
```

- python
```python 
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1
        
        best = -1
        for i in range(n - 1, -1, -1):
            while best != -1 and s[best + 1] != s[i]:
                best = fail[best]
            if s[best + 1] == s[i]:
                best += 1

        add = ("" if best == n - 1 else s[best+1:])
        return add[::-1] + s

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shortest-palindrome/solution/zui-duan-hui-wen-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```