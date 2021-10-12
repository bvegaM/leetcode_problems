class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        aux = romans[s[0]]
        result = 0
        for i in s:
            if romans[i] > aux:
                result = result + (romans[i] - aux*2)
            else:
                result+=romans[i]
                aux = romans[i]
        return result

if __name__ == '__main__':
    s = "LVIII"
    solution = Solution()
    response = solution.romanToInt(s)
    print(response)