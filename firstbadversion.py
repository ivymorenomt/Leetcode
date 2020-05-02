def isBadVersion(version):
    if version >= first_bad:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start < end:

            mid = (start + end) //2
            if isBadVersion(mid):
                end = mid
            else: 
                start = mid + 1
        return start

badver = Solution()
first_bad = 5
op = badver.firstBadVersion(4)
print(op)