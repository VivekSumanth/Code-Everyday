class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        count = 0
        flag = True
        while(flag):
            
            if digits[i] % 9 != 0 or digits[i] == 0 :
                digits[i] = digits[i] + 1
                flag = False
                
            elif digits[i] == 9:
                 digits[i] = 0
                 digits.insert(0,0)
                 i = i - 1

            else:
                digits[i] = digits[i]%9
                i = i-1
        
        for i in digits:
            if i == 0:
                count = count + 1
            else:
                break

        return digits[count::]