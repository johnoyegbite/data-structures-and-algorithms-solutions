# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:06:03 2019

@author: USER
"""
# SOLVED!
"""
Problem:
    There are 2N people a company is planning to interview.
    The cost of flying the i-th person to city A is costs[i][0],
    and the cost of flying the i-th person to the city B is costs[i][1]

Return the minimum cost to fly every person to a city
       such that exactly N people arrive in each city.

Example:
    Input: [[10, 20], [30, 200], [400, 50], [30, 20]]
    Output: 110

    Explanation:
        The first person goes to city A for a cost of 10.
        The second person goes to city A for a cost of 30.
        The third person goes to city B for a cost of 50.
        The fourth person goes to city B for a cost of 20.

        The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the
        people interviewing in each city.
    PS:
        1. 1 <= costs.length <= 100
        2. It is guaranteed that costs.length is even
        3. 1 <= costs[i][0], costs[i][1] <= 1000
"""


# SOLUTION
"""
The company need to send half of the people to city A and the remaining half
to city B, hence I need to FOCUS on how to send the first half people to city A


-- Calculate how much the company would save or loose, in relation to a city
  (in this case, city A). This is done by subtracting cost to A from cost to B
  i.e. Profit or loss = costB - costA
  (a negative value means loss while a positive value means profit)

            +10        +170      -350       -10
costs = [ [10, 20], [30, 200], [400, 50], [30, 20]] (original costs)

if company send the 1st person to city A instead of city B, they would save +10
if company send the 2nd person to city A instead of city B, they would save +170
if company send the 3rd person to city A instead of city B, they would loose -350
if company send the 4th person to city A instead of city B, they would loose -10

-- Sort the costs according to the maximum profit (or minimum loss),
i.e. the company wants to know how many of these people won't incure
     them much loss

             +170      +10       -10      -350
costs = [ [30, 200], [10, 20], [30, 20] [400, 50]] (sorted costs)

2nd person would save the company +170
1st person would save the company +10
4th person make the company loose -10
3rd person make the company loose -350

This means that the 1st person would incure no loss while the 3rd person would
incure the maximum loss.

Now we send the first half people that made a save for the company
(or incured lesser loss) to city A, then we send the rest to city B. | Q.E.D

From the example above, the means that send the 2nd and 1st persons to city
A, then 4th and 3rd persons to city B.

          A   |  B
     2nd (30) | (20) 4th
     1st (10) | (50)  3rd
    -----------------------
        40  +  70 = 110 (maximum profit)



ANOTHER EXAMPLE to clear your DOUBTs -->
The company need to send half of the people to city A and the remaining half
to city B, hence I need to FOCUS on how to send the first half people to city A


-- Calculate how much the company would save or loose, in relation to a city
  (in this case, city A). This is done by subtracting cost to A from cost to B
  i.e. Profit or loss = costB - costA
  (a negative value means loss while a positive value means profit)

(original costs)

           +511        -394       -259        -45         -772        -108
costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]

if company send the 1st person to city A instead of city B, they would save +511
if company send the 2nd person to city A instead of city B, they would loose -394
if company send the 3rd person to city A instead of city B, they would loose -259
if company send the 4th person to city A instead of city B, they would loose -45
if company send the 5th person to city A instead of city B, they would loose -772
if company send the 6th person to city A instead of city B, they would loose -108

-- Sort the costs according to the maximum profit (or minimum loss),
i.e. the company wants to know how many of these people won't incure
     them much loss

(sorted costs)
           +511        -45         -108        -259       -394        -772
costs = [[259, 770], [184, 139], [577, 469], [926, 667], [448, 54], [840, 118]]

1st person would save the company +511
4th person make the company loose -45
6th person make the company loose -108
3rd person make the company loose -259
2nd person make the company loose -394
5th person make the company loose -772

This means that the 1st person would incure no loss while the 5th person would
incure the maximum loss. Furthermore, the 4th person incures lesser loss than
the 6th person.

Now we send the first half people that made a save for the company
(or incured lesser loss), to city A then we send the rest to city B. | Q.E.D

From the example above, the means that send the 1st, 4th and 6th person to city
A, then 3rd, 2nd and 5th person to city B.

          A   |  B
    1st (259) | (667) 3rd
    4th (184) | (54)  2nd
    6th (577) | (118) 5th
    -----------------------
        1020  +  139 = 1859 (maximum profit)

"""


def two_city_schedule_cost(costs):
    """
    type cost: List[List[int, int]]
    rtype: int
    """
    # Sort based on the difference between the cost of both cities.
    # Reverse to make sure the positive difference (or profit) comes first.
    costs.sort(key=lambda person: person[1] - person[0], reverse=True)

    half = len(costs) // 2
    A_idx = 0  # position of cost for city A
    B_idx = 1  # position of cost for city B
    minimum_cost = 0

    # Loop through the half of the list,
    # Picking cost A from beginning to half of list,
    # and simutaneously pick cost B from half of the list to the end
    for i in range(half):
        #     i=0                 i+half=2
        # [ [30, 200], [10, 20], [30, 20] [400, 50]]
        # minimum_cost += costs[0][0] + costs[0+2][1]
        # => minimum_cost += 30 + 20
        minimum_cost += costs[i][A_idx] + costs[i+half][B_idx]

    return minimum_cost


if __name__ == "__main__":
    # costs = [ [10, 20], [30, 200], [400, 50], [30, 20], [30, 50], [50, 80],
    #     [120, 130], [50, 50]
    # ]
    # costs = [[259,770], [448,54], [926,667], [184,139], [840,118], [577,469]]
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    print(two_city_schedule_cost(costs))


"""
           A            B
p1 -> Kaduna (448) | Oyo (54)  [394]

p2 -> Kaduna (259) | Oyo (770) [511]
    394     >     -511
p1[0] - p1[1] > p2[0] - p2[1]

p1[0] + p2[1] > p2[0] + p1[1]

  448 + 770   > 259  + 54


  p1 = 448 - 54 = 394

  p2 = 259 - 770 = 511



  [926, 667], [184, 139]

  p2[0] - p2[1] < p1[0] - p1[1]
   184 - 139 <

"""
