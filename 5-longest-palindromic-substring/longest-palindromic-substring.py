class Solution:
    def longestPalindrome(self, s: str) -> str:
        new = []
        for letter in s:
            new.append('#')
            new.append(letter)
        new.append('#')
        
        p = [0] * len(new)
        center = 0
        right = 0

        for i in range(1, len(new)):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(p[mirror], right - i)
            while i + p[i] + 1 < len(new) and i - p[i] - 1 >= 0:
                if new[i + p[i] + 1] == new[i - p[i] - 1]:
                    p[i] += 1
                else:
                    break
            if i + p[i] > right:
                center = i
                right = i + p[i]

        maxx = max(p)
        maxx_index = p.index(maxx)
        start = (maxx_index - maxx) // 2
        return s[start: start + maxx]
