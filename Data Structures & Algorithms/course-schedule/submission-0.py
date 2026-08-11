class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for course in range(numCourses):
            prereq[course] = []
        for course,prerequisite in prerequisites:
            prereq[course].append(prerequisite)
        visiting = set()
        completed = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in completed:
                return True
            visiting.add(course)
            for prerequisite in prereq[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            completed.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        