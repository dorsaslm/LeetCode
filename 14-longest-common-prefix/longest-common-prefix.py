class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            first = strs[0]
            for i in range(len(first)):
                target = first[:i+1]
                num = 0
                for word in strs[1:]:
                    if not word.startswith(target):
                        return first[:i]

            return first




        