class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freqNumber = {}
        maxCount = 0
        sum=0
        for num in nums:
            freqNumber[num] = freqNumber.get(num,0)+1
            if freqNumber[num] % k == 0:
                sum += num*freqNumber[num]
                freqNumber[num]= 0
        # for key,d in freqNumber.items():
        #     if d%k==0:
        #         sum+=key*d
        return sum
sol = Solution()
print(sol.sumDivisibleByK([1,2,2,3,3,3,3,3,5], 2))