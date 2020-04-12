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

#def two_city_schedule_cost(costs):
#    """
#    Solution: 1. Find the absolute difference between the cost of the two cities
#              2. store the following (position of cost,
#                                      position of minimum cost between the two cities,
#                                      minimum cost between the two cities,
#                                      absolute difference between the cost of the two cities
#                                      )
#              3. Sort (2) above based on (1)
#              4. keep adding the minimum cost between the two cities.
#                 when one of the cities is full (full = half of length of costs),
#                 add the cost of the other city.
#    """
#    A_index = 0
#    B_index = 1
#    min_index = -1
#    costs_info = []
#    
#    for index, cost in enumerate(costs):
#        if cost[A_index] < cost[B_index]:
#            min_index = A_index
#        elif cost[B_index] < cost[A_index]:
#            min_index = B_index
#        min_val = cost[min_index]
#        diff_AB = abs(costs[index][A_index] - costs[index][B_index])
#        costs_info.append((index, min_index, min_val, diff_AB))
#        
#    total_min, count_A, count_B = 0, 0, 0 
#    half_N = (len(costs) // 2)
#    
#    # sort "costs_info" based on the absolute difference between the cost of the two cities
#    # which is at index/position "3" in "costs_info".
#    sorted_costs_info = sorted(costs_info, key=lambda x: x[3], reverse=True)
#    for cost_info in sorted_costs_info: 
#        index = cost_info[0]
#        min_index = cost_info[1]
#        min_val = cost_info[2]
#        cost = costs[index]
#        if min_index == A_index and count_A != half_N:
##            print(min_val, "A != half", "A")
#            total_min += min_val
#            count_A += 1
#        elif min_index == B_index and count_B != half_N:
##            print(min_val, "B != half", "B")
#            total_min += min_val
#            count_B += 1  
#        elif count_A == half_N: # city A is full, so add cost of city B
##            print(cost[B_index], "A == half", "B")
#            total_min += cost[B_index]
#        elif count_B == half_N: # city B is full, so add cost of city A
##            print(cost[A_index], "B == half", "A")
#            total_min += cost[A_index]
#
#    return total_min

# Two City_Schedule Cost improved
def two_city_schedule_cost(costs):
    """
    type cost: List[List[int, int]]
    Solution: 1. Sort "costs" by the absolute difference between the cost of the two cities
              2. keep adding the minimum cost between the two cities.
                 when one of the cities is full (full = half of length of costs),
                 add the cost of the other city.
    """
    A_index = 0
    B_index = 1

    total_min = 0
    count_A = 0
    count_B = 0
    
    half_cost = len(costs) // 2
    
    costs_sorted = sorted(costs, key=lambda cost: abs(cost[A_index] - cost[B_index]), reverse = True)
    for cost in costs_sorted:
        A_cost = cost[A_index]
        B_cost = cost[B_index]
        min_cost = min(A_cost, B_cost)
        
        if min_cost == A_cost and count_A != half_cost:
            count_A += 1
            total_min += A_cost
        elif min_cost == B_cost and count_B != half_cost:
            count_B += 1
            total_min += B_cost
        elif count_A == half_cost:
            total_min += B_cost
        elif count_B == half_cost:
            total_min += A_cost
        
    return total_min
    

if __name__ == "__main__":
    #costs = [
    #            [10, 20], [30, 200]
    #            ,[400, 50], [30, 20]
    #            ,[30, 50], [50, 80]
    #            ,[120, 130], [50, 50]
    #        ]
    #costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]

print(two_city_schedule_cost(costs))


