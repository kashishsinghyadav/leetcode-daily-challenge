class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]

        lst=[0,1]


        for i in range(2,n+1):
            num=list(bin(i))
            c=num.count("1")
            lst.append(c)

        return lst

