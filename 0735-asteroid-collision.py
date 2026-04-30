class Solution:
    """Solution for simulating asteroid collisions.

    You are given an array `asteroids` representing asteroids in a row.

    - The absolute value represents size
    - The sign represents direction:
        positive = moving right
        negative = moving left

    When two asteroids collide:
    - Smaller one is destroyed
    - If equal size, both are destroyed
    - Same-direction asteroids never collide
    """

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        # pos stack
        # neg value collide
        for a in asteroids:
            append_a = True
            while stack and stack[-1] > 0 and a < 0:
                append_a = stack[-1] < abs(a)
                if stack[-1] == abs(a):
                    stack.pop()
                    break
                # 6, -2
                elif stack[-1] > abs(a):
                    break
                # 6, -8
                elif stack[-1] < abs(a):
                    stack.pop()
            if append_a:
                stack.append(a)
        return stack