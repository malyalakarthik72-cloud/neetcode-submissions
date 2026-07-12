class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total=[]
        for i in operations:
                match i:
                    case '+':
                        s=total[-1]+total[-2]
                        total.append(s)
                    case 'C':
                        total.pop()
                    case 'D':
                        double = total[-1] * 2
                        total.append(double)
                    case _:
                        total.append(int(i))
        return sum(total)
        




                
                

