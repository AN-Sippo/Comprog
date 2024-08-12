class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        symbolValue = [("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]
        for symbol,value in symbolValue:
            while num >= value:
                num -= value 
                ans += symbol
        
        print(ans)

Solution().intToRoman(3749)