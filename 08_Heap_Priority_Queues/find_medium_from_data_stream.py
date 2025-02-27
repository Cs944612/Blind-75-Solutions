"""
Find Median From Data Stream
Problem: LeetCode 295 - Find Median from Data Stream
Difficulty: Hard

Problem statement:
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.

Example 1:
Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]
Output:
[null, null, 1.0, null, 2.0, null, 2.0]
Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data structure.
"""

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # max heap for lower half
        self.small = []
        # min heap for upper half
        self.large = []

    def addNum(self, num: int) -> None:
        # add to small(max heap) first        
        heappush(self.small, -num)

        # ensure small's top isn't greater than large's top
        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = -heappop(self.small)
            heappush(self.large, value)

        # Balance the heaps: small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heappop(self.large)
            heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # Odd count, median is top of small
            return -self.small[0]
        else:
            # Even count, average of tops
            return (-self.small[0] + self.large[0]) / 2
        
