#Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

#For example,
#[2,3,4], the median is 3

#[2,3], the median is (2 + 3) / 2 = 2.5

#Design a data structure that supports the following two operations:

#void addNum(int num) - Add a integer number from the data stream to the data structure.
#double findMedian() - Return the median of all elements so far.


#Example:

#addNum(1)
#addNum(2)
#findMedian() -> 1.5
#addNum(3)
#findMedian() -> 2


#Follow up:

#If all integer numbers from the stream are between 0 and 100, how would you optimize it?
#If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.small) >= len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.large) < len(self.small):
            return float(self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        return float((self.large[0] + self.small[0]) / 2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()