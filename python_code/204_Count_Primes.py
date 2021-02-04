#Count the number of prime numbers less than a non-negative number, n.



#Example 1:

#Input: n = 10
#Output: 4
#Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#Example 2:

#Input: n = 0
#Output: 0
#Example 3:

#Input: n = 1
#Output: 0


#Constraints:

#0 <= n <= 5 * 106

class Solution:
    def countPrimes(self, n: int) -> int:
        tmp = [1 for _ in range(n)]
        i = 2
        while i*i < n:
            if tmp[i]:
                for j in range(2*i, n, i):
                    tmp[j] = 0
            i += 1
        cnt = 0
        for m in range(2, n):
            if tmp[m]:
                cnt += 1
        return cnt