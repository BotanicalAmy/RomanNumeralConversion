
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

# I placed before V or X indicates one less,
# so four is IV (one less than five) and nine is IX (one less than ten)
# X placed before L or C indicates ten less,
# so forty is XL (ten less than fifty) and ninety is XC (ten less than a hundred)
# C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred)
# and nine hundred is CM (a hundred less than a thousand)

# name my solution class
roman_solve = Solution()

# ask the user to enter their roman numeral
roman_numeral = input("Enter your roman numeral: \n")

# get the value from the conversion method

value_sum = roman_solve.romanToInt(roman_numeral)

print(value_sum)
