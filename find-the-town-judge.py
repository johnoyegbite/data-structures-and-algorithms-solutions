# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:30:37 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    In a town, there are N people labelled from 1 to N.
    There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:
        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given trust, an array of pairs trust[i] = [a, b] representing
        that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the
    town judge.  Otherwise, return -1.

Example 1:
    Input: N = 2, trust = [[1,2]]
    Output: 2

Example 2:
    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

Example 3:
    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Example 4:
    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

Example 5:
    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
                     1: -2
                     2: -2
                     3: 3
                     4: 0

    Output: 3
Note:
    1 <= N <= 1000
    trust.length <= 10000
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N
"""


class Solution:
    def findJudge(self, N, trust):
        """
        type N: int
        type trust: List[List[int]]
        rtype: int
        """
        if not len(trust):
            return N
        town_people = set()
        town_judge = set()

        # keep track of town people (also non-judges)
        for person, _ in trust:
            town_people.add(person)
        print("Town people:", town_people)

        # get the number of real judges in town (judges that trust nobody)
        for _, judge in trust:
            if judge not in town_people:
                town_judge.add(judge)

        # we must have just one judge
        if len(town_judge) != 1:
            return -1

        # count the number of people that trust the judge we have
        valid_trustee = 0
        judge = town_judge.pop()
        for person, curr_judge in trust:
            if judge == curr_judge:
                valid_trustee += 1
        print("Valid trustee:", valid_trustee)

        # make sure all people in the town trust the judge we have
        if valid_trustee != len(town_people):
            judge = -1
        print("Final Judge:", judge)

        return judge


# 2nd Solution
def findJudge(self, N, trust):
    """
    type N: int
    type trust: List[List[int]]
    rtype: int
    """
    if not len(trust):
        return N  # if N = 1 and trust = []

    # For a person in a town, store the number of people that the person
    # trust and simultaneously the number of people that trust the person
    person_net_trust = {}

    for truster, trustee in trust:
        # Truster
        person_net_trust[truster] = person_net_trust.get(truster, 0) - 1

        # Trustee
        person_net_trust[trustee] = person_net_trust.get(trustee, 0) + 1

    for person in person_net_trust:
        if person_net_trust[person] == N-1:  # N-1 => judge not included
            return person

        return -1


"""
Thought process of 2nd solution:
    You know that trust[i][0] is a truster and trust[i][1] is a trustee.
    If you trust someone (truster), you are at risk,
    if someone trust you (trustee) you are at an advantage.
    Also remember that a judge trust no one and all persons must trust that
    judge.
    If we have a judge that not everyone trust the that's a stupid judge.

    Example:
     Let person_net_trust rep pnt

    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]

    Say we haven't started the poll of trust, our

    pnt = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
    }

    trust[0] => [1, 3]
    => pnt{
             1: -1,
             2: 0,
             3: 1,
             4: 0
           }
    This means that 1 trusted 3 and 3 was trusted by 1


    trust[1] => [1, 4]
    => pnt{
             1: -2,
             2: 0,
             3: 1,
             4: 1
           }
    This means that 1 trusted 4 and 4 was trusted by 1.
    So 1 has trusted 2 people


    trust[2] => [2, 3]
    => pnt{
             1: -2,
             2: -1,
             3: 2,
             4: 1
           }
    This means that 2 trusted 3 and 3 was trusted by 2.
    Now 3 is trusted by two persons.


    trust[3] => [2, 4]
    => pnt{
             1: -2,
             2: -2,
             3: 2,
             4: 2
           }
    This means that 2 trusted 4 and 4 was trusted by 2.
    Now 4 is trusted by two persons.


    trust[4] => [4, 3]
    => pnt{
             1: -2,
             2: -2,
             3: 3,
             4: 1
           }
    This means that 4 trusted 3 and 3 was trusted by 4.
    Now 3 is trusted by three persons. Also note 4's net trust



    Since N = 4, then we look for the person that is trusted by everyone apart
    from itself (N-1) and doesn't trust anybody which can only be the person
    that has its value as N-1

    Hence 3 is the winner.


    Summary:
    1 trusted two people
    2 trusted two people
    3 is trusted by three people (all)
    4 is trusted by two people but trusted one person

"""
