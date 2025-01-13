class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        lengths= []

        for i,first in enumerate(s):
            serries = []
            serries.append(first)
            if i != len(s)-1:
                for second in s[i+1:]:
                    if second in serries:
                        break
                    else:
                        serries.append(second)
            lengths.append(len(serries))
            
        return max(lengths) if lengths else 0



