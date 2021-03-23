#Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

#As the answer can be very large, return it modulo 109 + 7.



#Example 1:

#Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
#Output: 20
#Explanation:
#Enumerating by the values (arr[i], arr[j], arr[k]):
#(1, 2, 5) occurs 8 times;
#(1, 3, 4) occurs 8 times;
#(2, 2, 4) occurs 2 times;
#(2, 3, 3) occurs 2 times.
#Example 2:

#Input: arr = [1,1,2,2,2,2], target = 5
#Output: 12
#Explanation:
#arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
#We choose one 1 from [1,1] in 2 ways,
#and two 2s from [2,2,2,2] in 6 ways.


#Constraints:

#3 <= arr.length <= 3000
#0 <= arr[i] <= 100
#0 <= target <= 300

from typing import List
from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts = Counter(arr)

        res = 0
        constant = 10 ** 9 + 7

        for i in range(100):
            if counts[i] == 0:
                continue

            j, k = i, 100

            while j <= k:
                if j + k > target - i:
                    k -= 1
                elif j + k < target - i:
                    j += 1
                else:
                    if i == j == k:
                        res += counts[i] * (counts[i]-1) * (counts[i]-2) // 6
                    elif i == j:
                        res += counts[i] * (counts[i]-1) * counts[k] // 2
                    elif j == k:
                        res += counts[i] * counts[j] * (counts[j]-1) // 2
                    else:
                        res += counts[i] * counts[j] * counts[k]
                    j += 1
                    k -= 1
        return res % constant