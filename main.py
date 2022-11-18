
class Solution:

    def __init__(self):
        self.numeral = []
        self.s = ''
        self.roman_numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        self.s = s
        self.numeral = list(self.s)
        self.numeral = [self.roman_numeral_values[k] for k in self.numeral if k in self.roman_numeral_values]
        return sum(self.numeral)


roman_solve = Solution()

roman_numeral = input("Enter your roman numeral: \n")
roman_numeral_length = len(roman_numeral)

value_sum = roman_solve.romanToInt(roman_numeral)

print(value_sum)
