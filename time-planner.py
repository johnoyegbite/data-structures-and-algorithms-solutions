# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:50:31 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Time Planner
    Implement a function meetingPlanner that given the availability,
    slotsA and slotsB, of two people and a meeting duration dur,
    returns the earliest time slot that works for both of them and is of
    duration dur. If there is no common time slot that satisfies the duration
    requirement, return an empty array.

    Time is given in a Unix format called Epoch, which is a nonnegative integer
    holding the number of seconds that have elapsed since 00:00:00 UTC,
    Thursday, 1 January 1970.

    Each person’s availability is represented by an array of pairs.
    Each pair is an epoch array of size two.
    The first epoch in a pair represents the start time of a slot.
    The second epoch is the end time of that slot.
    The input variable dur is a positive integer that represents the duration
    of a meeting in seconds.
    The output is also a pair represented by an epoch array of size two.

    In your implementation assume that the time slots in a person’s
    availability are disjointed, i.e, time slots in a person’s availability
    don’t overlap.
    Further assume that the slots are sorted by slots’ start time.

    Implement an efficient solution and analyze its time and space
    complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12

Constraints:

[time limit] 5000ms

[input] array.array.integer slotsA

1 ≤ slotsA.length ≤ 100
slotsA[i].length = 2
[input] array.array.integer slotsB

1 ≤ slotsB.length ≤ 100
slotsB[i].length = 2
[input] integer

[output] array.integer
"""


def meeting_planner(slotsA, slotsB, dur):
    a, b = 0, 0
    while a < len(slotsA) and b < len(slotsB):
        a_interval = slotsA[a]  # get interval for A
        b_interval = slotsB[b]  # get interval for B

        # A = [2, 8], B = [3, 5]
        # 1. If A arrives at 2pm and B arrives at 3pm,
        # then their meeting can start nothing earlier than 3pm, which is the
        # max of the arriving time of A and B (start time)
        # 2. Likewise, if A plans to leave by 8pm and B plans to leave by 5pm
        # then their meeting cannot exceed 5pm which is the minimum of the
        # leaving time of A and B (end time)
        # 3. if start time is greater than end time, then cannot have the
        # meeting.
        start_time = max(a_interval[0], b_interval[0])
        end_time = min(a_interval[1], b_interval[1])

        if start_time >= end_time:
            if a_interval[0] <= b_interval[0]:
                a += 1  # move to another slot in slotsA
            else:
                b += 1  # move to another slot in slotsB
        else:
            time_diff = end_time - start_time
            if time_diff >= dur:
                return [start_time, start_time + dur]
            else:
                if a_interval[1] >= b_interval[1]:
                    b += 1  # move to another slot in slotsB
                elif b_interval[1] > a_interval[1]:
                    a += 1  # move to another slot in slotsA
    return []

# [10, 60] -> A
# [10, 50] -> B
#
# (10,  50)
# max   min

# [ 0, 60] -> 60
# [10, 50] -> 40
# (10,  50)

# [10, 50] -> 40
# [0, 15] -> 15
# (10,  15)

# [10, 60] -> 50
# [60, 100] -> 40
# (60,  60)

# [10, 60] -> 50
# [80, 110] -> 30
# (80,  60)

# [10, 60] -> 50
# [45, 110] -> 65
# (45,  60)

# [10, 120] -> 110
# [45, 110] -> 65
# (45,  110)

# dur = 10


"""
slotsA = [
  [10, 50], # 40
  [60, 120], # 60
  [140, 210] # 70
]
slotsB = [
  [0, 15], # 15
  [60, 70] # 10
  [150, 200]
]

[10, 50]
[60, 70]

start = max(10,60) = 60
end = min(50,70)= 50
[start,end]

"""
