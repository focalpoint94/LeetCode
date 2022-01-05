class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        ret_list = []
        x = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]
        
        def save_comb(digits, string):
            if not digits:
                ret_list.append(string)
                return
            char_list = x[int(digits[0])]
            for char in char_list:
                save_comb(digits[1:], string+char)
            
        save_comb(digits, '')
        return ret_list
        
