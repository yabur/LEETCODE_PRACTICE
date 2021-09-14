# Given a list of meetings intervals where each interval consist od start and end time,
# Check if a person can attend all the given meeting such that only one metting can be attended at a time.


# Input = [[1, 5],[5,8],[10,15]
# Output = 1
import collections


def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(0, len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return 0
    return 1
