class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # intervals are sorted and don't overlap, so one pass works:
        # step 1. add the intervals that end before newInterval starts
        # step 2. merge every interval that overlaps newInterval into it
        # step 3. add the merged interval, then the rest (they start after it ends)

        ans = [] # res intervals
        start_nI, end_nI = newInterval
        
        i = 0
        n = len(intervals)

        # step 1
        # add non-overlapping intervals
        # end_I < start_nI
        while i < n and intervals[i][1] < start_nI:
            ans.append(intervals[i])
            i += 1
        # start_nI <= end_I
        
        # step 2
        # the first interval that might overlap
        # find the end of new interval to insert
        # loop till end_nI < start_I...
        while i < n and intervals[i][0] <= end_nI:
            start_nI = min(intervals[i][0], start_nI)
            end_nI = max(end_nI, intervals[i][1]) 
            i += 1

        # now ... end_nI < start_I
        # so ... [start_nI, end_nI] is now a non-overlapping interval
        ans.append([start_nI, end_nI])

        # step 3
        # add the rest of non-overlapping intervals
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans