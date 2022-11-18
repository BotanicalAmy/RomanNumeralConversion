class Solution:

    def romanToInt(self, s: str) -> int:
        self.s = s
        numeral = list(self.s)
        numeral = [roman_numeral_values[k] for k in numeral if k in roman_numeral_values]
        # need to subtract values when the leading numeral value is less than the one that follows, bc Greeks
        for number in range(len(numeral) - 1):
            if numeral[number] < numeral[number + 1]:
                numeral[number] = -abs(numeral[number])
        return sum(numeral)


roman_numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# name my solution class
roman_solve = Solution()

# ask the user to enter their roman numeral
roman_numeral = input("Enter your roman numeral: \n")

# get the value from the conversion method

value_sum = roman_solve.romanToInt(roman_numeral)

print(value_sum)
