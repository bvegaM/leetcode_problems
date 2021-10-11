import time
class Solution:
     def convert(self, s: str, numRows: int) -> str:
        counter,explore,max_counter = 0,0,0
        flag    = True
        response = ''
        if numRows==0:
            return s
        elif numRows==1:
            return s
        else:
            while len(response)<len(s):
                if explore == len(s):
                    explore=0
                    counter =0
                    max_counter+=1

                if counter == max_counter:
                    response+=s[explore]
                    aux=counter
                
                if counter == numRows-1:
                    flag = False
                elif counter == 0:
                    flag = True

                if flag == True:
                    aux = counter
                    counter+=1
                    explore+=1
                else:
                    aux = counter
                    counter-=1
                    explore+=1
                    
            return response
        
if __name__ == '__main__':
    s = "PAYPALISHIRING"
    num_rows = 4
    solution = Solution()
    result = solution.convert(s,num_rows)
    print(result)