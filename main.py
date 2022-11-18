class Solution:

    def __init__(self):
        self.numeral = []
        self.s = ''
        self.roman_numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        self.s = s
        self.numeral = list(self.s)
        self.numeral = [self.roman_numeral_values[k] for k in self.numeral if k in self.roman_numeral_values]
        # need to subtract values when the leading numeral value is less than the one that follows, bc Greeks
        for number in range(len(self.numeral) - 1):
            if self.numeral[number] < self.numeral[number + 1]:
                self.numeral[number] = -abs(self.numeral[number])
        return sum(self.numeral)


# name my solution class
roman_solve = Solution()

# ask the user to enter their roman numeral
roman_numeral = input("Enter your roman numeral: \n")

# get the value from the conversion method

value_sum = roman_solve.romanToInt(roman_numeral)

print(value_sum)
