from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> str:
        dque_list = deque()
        max_len = 0
        for char in s:
            if char in dque_list:
                pop = None
                while pop !=char:
                    pop = dque_list.popleft()  
            dque_list.append(char)
            max_len = max(max_len,len(dque_list))
        return max_len

if __name__ == '__main__':
    s = 'pwwkew'
    solution  = Solution()
    reponse = solution.lengthOfLongestSubstring(s)
    print(reponse)

    
