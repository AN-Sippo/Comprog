class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        num_int = num
        while num_int > 0:
            # print(num_int)
            num_int,ans = self.selectNext(num_int,ans)
        return ans
                
  
    def selectNext(self,num_int,ans):
        num_string = str(num_int)
        if num_int >= 1000: 
            # repeat
            repeat = int(num_string[0])
            ans += "M" * repeat
            num_int -= 1000 * repeat
        elif num_int >= 900:
            # substractive
            ans += "CM"
            num_int -= 900
        elif num_int >= 500:# <=999
            # five
            ans += "D"
            num_int -= 500
        elif num_int >= 400:# (400 <= num_int <= 499)
            # substractive
            ans += "CD"
            num_int -= 400
        elif num_int >= 100:
            # repeat
            repeat = int(num_string[0])
            ans += "C" * repeat
            num_int -= 100 * repeat
        elif num_int >= 90:
            # substractive
            ans += "XC"
            num_int -= 90
        elif num_int >= 50:
            # five
            ans += "L"
            num_int -= 50
        elif num_int >= 40:
            #substractive
            ans += "XL"
            num_int -= 40
        elif num_int >= 10:
            # repeat
            repeat = int(num_string[0])
            ans += "X" * repeat
            num_int -= repeat * 10  
        elif num_int >= 9:
            #substractive
            ans += "IX"
            num_int -= 9
        elif num_int >= 5:
            ans += "V"
            num_int -= 5
        elif num_int >= 4:
            ans += "IV"
            num_int -= 4
        else :
            repeat = int(num_string[0])
            ans += "I" * repeat
            num_int -= repeat * 1
        return num_int,ans

        


def main():
    input = 3749
    print(Solution().intToRoman(input))


main()
