# SOLVED!
"""
    Given a list of 24-hour clock time points in "Hour:Minutes" format,
    find the minimum minutes difference between any two time points in the list.


["00:00", "14:38", "23:59"] -> [1440, 878, 1439]
['22:00','09:00'] [1320, 540] = > 780
['09:00', "14:38", '22:00'] -> [540, 878, 1320]
                                        22 - 9 = 13, 22(24) - 9(24) = 11   22:00 -> 00:00 -> 09:00    23:59 00:00 -> 24:00              ^
9 + 24-22																				10:00 -> 34:001`
["10:11","22:00","14:38","23:00"] -> []
60
[00:00,23:00]
# sort the list (since it's 24hr)
# traverse through and store in say "min_" variable
"""

def min_min(time_points):
    time_points_new = []
    for point in time_points:
        point_split = point.split(":")
        hrs, mins = int(point_split[0]), int(point_split[1])
        hrs = hrs * 60
        total_min = hrs + mins
        time_points_new.append(total_min)
    time_points_new.sort()
    new_min = float("+inf")
    for i in range(len(time_points_new)-1):
        min_ = time_points_new[i+1] - time_points_new[i]
        new_min = min(min_, new_min)
    first, last = time_points_new[0] + 24*60, time_points_new[-1]
    new_min = min(new_min, (first-last))
    return new_min


if __name__ == "__main__":
    time_points = ["00:00", "14:38", "23:59"]
    # time_points = ['22:00','09:00']
    print(min_min(time_points))

