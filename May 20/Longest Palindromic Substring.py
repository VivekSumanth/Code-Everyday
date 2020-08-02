# date: 30/05/20
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_parlindrome = []
        
        def parlindrome_right(rightstring):
            if(rightstring == rightstring[::-1]):
                final_parlindrome.append("".join(rightstring))
            else:
                return edit_right(rightstring)

        def edit_right(rightstring):
            k = len(rightstring)
            lis = []
            for i in range(k-1):
               lis.append(rightstring[i])
 
            return parlindrome_right(lis)
        
        def parlindrome_left(leftstring):
            if(leftstring == leftstring[::-1]):
                final_parlindrome.append("".join(leftstring))
            else:
                return edit_left(leftstring) 
        
        def edit_left(leftstring):
            lise=[]
            for i in range(1,len(leftstring)):
                lise.append(leftstring[i])
            return parlindrome_left(lise)  
            
        def parlindrome_both(bothstring):
            if (bothstring == bothstring[::-1]):
                final_parlindrome.append("".join(bothstring))
            else:
                return edit_both(bothstring)     
         
        def edit_both(bothstring):
            l = len(bothstring)
            lisd=[]
            for p in range(1,l-1):
                lisd.append(bothstring[p])
            parlindrome_right(lisd)
            parlindrome_left(lisd)
            parlindrome_both(lisd)
            
        parlindrome_right(s)
        parlindrome_left(s)
        parlindrome_both(s)
        
        print(final_parlindrome)
        x =  max(final_parlindrome ,key = len)
        print(x)
        return x

# time limit exceed.
# testcase: 41 / 103
# "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"