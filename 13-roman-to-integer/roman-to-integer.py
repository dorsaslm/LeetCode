class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = { 'I':            1,
                    'V' :           5,
                    'X'  :          10,
                    'L'  :          50,
                    'C'  :          100,
                    'D'  :          500,
                    'M'  :          1000}
        num = 0
        previous = 0  

        for char in s:
            current = mapping[char]
            
            if previous < current:
                num += current - (2 * previous) 
            else:
                num += current
                
            previous = current  
            
        return num