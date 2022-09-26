class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add=0
        prod=1
        while(n>0):
            a = n%10
            n= n//10
            add=add+a
            prod = prod*a
        return prod - add 
