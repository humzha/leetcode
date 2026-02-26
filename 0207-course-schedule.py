from typing import List, Dict
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determine if you can finish all courses given prerequisite pairs.
        Courses are labeled from 0 to numCourses-1. Each prerequisite
        pair [a, b] means you must take course b before course a. Return
        True if scheduling is possible (i.e., no cycle), otherwise False.

        Args:
            numCourses (int): The total number of courses.
            prerequisites (List[List[int]]): List of prerequisite pairs.

        Returns:
            bool: True if all courses can be finished, False otherwise.
        """
        # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        class_to_prereqs: Dict[str, list[int]] = collections.defaultdict(list)
        for course, prereq in prerequisites:
            class_to_prereqs[course].append(prereq)

        def dfs(c: int) -> bool:
            if class_to_state[c] == COMPLETE:
                return True
            elif class_to_state[c] == IN_PROGRESS:
                return False
            class_to_state[c] = IN_PROGRESS
            for prereq in class_to_prereqs[c]:
                if not dfs(prereq):
                    return False
            class_to_state[c] = COMPLETE
            return True

        # DFS Topological Sort
        # 3 states for a class
        # NOT_STARTED
        # IN_PROGRESS
        # COMPLETE
        NOT_STARTED, IN_PROGRESS, COMPLETE = range(3)
        class_to_state = [NOT_STARTED for _ in range(numCourses)]
        for i in range(numCourses):
            if not dfs(i):
                return False

        return all([x == COMPLETE for x in class_to_state])
