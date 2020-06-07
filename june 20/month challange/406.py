# date:6/jun/20
# 406. Queue Reconstruction by Height
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

 
# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        print(people)
        temp = people
        l = [None]*(len(temp))
        for each in temp:
            if l[each[1]] == None:
                l[each[1]] = each
            else:
                l.insert(each[1],each)
                l.remove(None)

        return l  