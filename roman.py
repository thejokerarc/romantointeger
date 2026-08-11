class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(len(s)):
            # if current value is less than the next one, subtract it
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total


if __name__ == "__main__":
    solution = Solution()
    roman_input = input("Enter a Roman numeral: ").upper()
    result = solution.romanToInt(roman_input)
    print(f"{roman_input} = {result}")
