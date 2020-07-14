# 1344. Angle Between Hands of a Clock
# Medium

# 227

# 59

# Add to List

# Share
# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

# Example 1:



# Input: hour = 12, minutes = 30
# Output: 165
# Example 2:



# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:



# Input: hour = 3, minutes = 15
# Output: 7.5
# Example 4:

# Input: hour = 4, minutes = 50
# Output: 155
# Example 5:

# Input: hour = 12, minutes = 0
# Output: 0
 

# Constraints:

# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.


class Solution(object):
    def angleClock(self, hour, minu):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        if hour > 12:
            hour = hour-12
        
        if minu == 60:
            hour = hour +1
        
        if minu > 60:
            hour = hour + 1
            minu = 60 - minu
        
        hourangle = (hour*60+minu)*0.5
        minangle = minu*6
        
        angle = abs(hourangle-minangle)
        angle = min(360-angle,angle)
        
        return (angle)
    
# How to calculate the two angles with respect to 12:00?
# The minute hand moves 360 degree in 60 minute(or 6 degree in one minute) and hour hand moves 360 degree in 12 hours(or 0.5 degree in 1 minute). 
# In h hours and m minutes, the minute hand would move (h*60 + m)*6 and hour hand would move (h*60 + m)*0.5.