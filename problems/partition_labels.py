from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastWord={j: i for i,j in enumerate(s)}
        aux = width = 0
        result=[]
        for i,j in enumerate(s):
            aux = max(aux,lastWord[j])
            if i == aux:
                result.append(i-width+1)
                width =i+1
        return result


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    solution = Solution()
    response = solution.partitionLabels(s)
    print(response)