# date: 18/jun/20
# 274. H-Index
# Medium

# 599

# 1035

# Add to List

# Share
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# Example:

# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        else:
            citations.sort(reverse = True)

            count = 1
            for i in citations:
                if i < count:
                    return count-1
                count = count+1
            return count-1

# Runtime: 20 ms, faster than 94.14% of Python online submissions for H-Index.
# Memory Usage: 12.9 MB, less than 79.84% of Python online submissions for H-Index.