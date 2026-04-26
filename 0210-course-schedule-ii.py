from collections import defaultdict

class Solution:
    """Solution for returning a valid order of courses to finish all prerequisites.

    You are given `numCourses` labeled from 0 to numCourses - 1 and a list of
    prerequisite pairs where [a, b] means you must take course `b` before `a`.

    Return any valid ordering of courses that allows you to complete all courses.
    If it is impossible (due to cycles), return an empty list.
    """

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """Finds a valid course order given prerequisite constraints.

        Args:
            numCourses (int): Total number of courses.
            prerequisites (list[list[int]]): List of prerequisite pairs [a, b].

        Returns:
            list[int]: A valid ordering of courses, or an empty list if impossible.
        """

        # Topological sort
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
            
        topological_sorted = []
        visited = [False for _ in range(numCourses)]
        completed = [False for _ in range(numCourses)]
        def dfs(course: int) -> bool:
            if completed[course]:
                return True
            if visited[course]:
                return False

            visited[course] = True
            for prereq in adj_list[course]:
                # cyclic
                if not dfs(prereq):
                    return False

            completed[course] = True
            topological_sorted.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return topological_sorted