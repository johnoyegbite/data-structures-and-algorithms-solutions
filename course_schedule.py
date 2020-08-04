# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:16:10 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    There are a total of numCourses courses you have to take, labeled from 0 to
    numCourses-1.

    Some courses may have prerequisites, for example to take course 0 you have
    to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it
    possible for you to finish all courses?


Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0.
                 So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0, and to
                 take course 0 you should also have finished course 1.
                 So it is impossible.

Constraints:
    The input prerequisites is a graph represented by a list of edges, not
    adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5
"""


class Solution:
    def dfs(self, node, visited, graph):
        # This node doesn't have a prerequisite
        if node not in graph:
            return True

        # There is a cycle
        if node in visited:
            return False

        visited.add(node)

        for child in graph[node]:
            if not self.dfs(child, visited, graph):
                return False

        # We are done with the prerequisite of this node,
        # so, remove for other node to use as a prerequisite
        visited.remove(node)

        # This node's prerequisite has been completed and
        # it doesn't have a cycle.
        return True

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        """
        tupe numCourses: int
        type prerequisites: List[List[int]]
        rype: bool
        """
        # Use the idea of Topological Sort.
        graph = {}
        for course, prereq in prerequisites:
            if course in graph:
                graph[course].append(prereq)
            else:
                graph[course] = [prereq]

        for course in range(numCourses):
            visited = set()
            if not self.dfs(course, visited, graph):
                return False

        return True
