from typing import Optional

class ListNode:

    def __init__(self,val=0,next_val=None):
        self.val = val
        self.next = next_val

class Solution:

    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode])->Optional[ListNode]:
        list_1,list_2 =[],[]
        number_1,number_2,result = '','',''

        while l1:
            list_1.append(l1.val)
            l1 = l1.next

        while l2:
            list_2.append(l2.val)
            l2 = l2.next

        for i in list_1[::-1]:
            number_1+=str(i)
        for i in list_2[::-1]:
            number_2+=str(i)

        result= str(int(number_1)+int(number_2))[::-1]

        response = ListNode(int(result[0]))
        response_tail = response
        for i in range(1,len(result)):
            response_tail.next = ListNode(result[i])
            response_tail = response_tail.next
        
        return response

        


if __name__ == '__main__':
    
    # l1 - List Node (243)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # l2 - List Node (465)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    response = solution.addTwoNumbers(l1,l2)

    while response:
        print(response.val)
        response = response.next