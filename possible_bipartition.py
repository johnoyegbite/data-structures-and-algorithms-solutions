# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:43:49 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a set of N people (numbered 1, 2, ..., N), we would like to split
    everyone into two groups of any size.

    Each person may dislike some other people, and they should not go into the
    same group.

    Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
    people numbered a and b into the same group.

    Return true if and only if it is possible to split everyone into two groups
    in this way.


Example 1:
    Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4], group2 [2,3]

Example 2:
    Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false

Example 3:
    Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false

Note:
    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].
"""

"""
Since we have just two groups, I decide to give one of the groups color
True and the other color False.
(you can decide to use red and blue or 0 and 1, or whatever)

The idea is that we color all the people a person dislikes with her
opposite color. Now if we are performing the coloration and accidentally,
a person who is already colored wants to be colored and this new color
doens't match his/her color then there is a conflict and they can't be
grouped else they can be grouped into two.

Example 1:
    N = 3, dislikes = [[1, 3], [2, 3], [1, 2]]
    1 dislikes 2 and 3
    2 dislikes 1 and 3
    3 dislikes 1 and 2
    Graph would look like graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    colors = {}

              1
            /   \
           2  __ 3
    Now if I choose my colors as Blue(B) and Red(R)

       colors = {1: 'B', 2: 'R', 3: 'R'}
    => 1 is colored a 'B', then 2 and 3 must be of opposite color 'R'

       colors = {1: 'B', 2: 'R', 3: 'B'}
    => since 2 has 'R' (from 1), then 1 and 3 must be of 'B'

       There is a confict of colors with 3 from transition (see above colors[3])
    => Now 1 still maintains his color but 3 doesn't since it had a
       color of 'R' from 1. There is a conflict here and can't be grouped
       Hence we return False.

Example 2:
    N = 4, dislikes = [[1, 2],[1, 3],[2, 4]]
    1 dislikes 2 and 3
    2 dislikes 1 and 4
    3 dislikes 1
    4 dislikes 2
    graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
              1
            /   \
           2     3
          /
         4
    Now if I choose my colors as Blue(B) and Red(R)

       colors = {1: 'B', 2: 'R', 3: 'R'}
    => 1 is colored a 'B', then 2 and 3 must be of the opposite color (R)

       colors = {1: 'B', 2: 'R', 3: 'R', 4: 'B'}
    => since 2 has 'R' (from 1) then 1 and 4 must be of 'B'
       Now 1 still maintains his color and 4 was given his color

      colors = {1: 'B', 2: 'R', 3: 'R', 4: 'B'}
    => since 4 has 'B' (from 2) then 2 must have opposite color 'R'
       Now 2 still maintains his color

    colors = {1: 'B', 2: 'R', 3: 'R', 4: 'B'}
    => since 3 has 'R' (from 1) then 1 must have opposite color 'B'
       Now 1 still maintains his color.

     We are done with the DFS and there is no conflict hence they can
     be grouped.
"""


class Solution:
    def dfs(self, node, color, colors, graph):
        # Now, this node might be a child of the previous node,
        # which won't have a child, hence return True
        if node not in graph:
            return True

        # if we encountered this node before, then to confirm its
        # grouping, the new color must be equal to the old color.
        # if it's not, then it can't be grouped
        if node in colors:
            return colors[node] == color

        # Color a node
        colors[node] = color

        # All the chidren of this node must have opposite color.
        for child in graph[node]:
            # if we see a child that its color is not opposite of its parent,
            # and it's children color is not also opposite of then we can't
            # group.
            if not self.dfs(child, not color, colors, graph):
                return False

        # reaching this point means all the children of this current node
        # has it color opposite its parent, hence can be grouped
        return True

    def possibleBipartition(self, N: int, dislikes) -> bool:
        """
        type N: int
        type dislikes: List[List[int]]
        rtype: bool
        """
        if not dislikes:
            return True
        graph = {}
        for u, v in dislikes:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]

        colors = {}
        bipart_possible = True
        # We have to go through all the node so as to take care of
        # disjoint in the graph.
        # example of disjoint in the graph is when graph is of:
        # graph = {1: [2], 2: [1], 3: [4, 5], 4: [3, 5], 5: [3, 4]}
        for node in range(1, N+1):
            # if we haven't colored a node, then color it and also see if
            # its descendant can be grouped.
            if node not in colors and not self.dfs(node, True,
                                                   colors, graph):
                bipart_possible = False
                return bipart_possible  # same as returning False Instantly

        # same as return True if False failed in the loop
        return bipart_possible
