from typing import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        stack = [asteroids.pop(0)]
        while asteroids:
            asteroid = asteroids.pop(0)
            if stack:
                if asteroid * stack[-1] > 0:
                    stack.append(asteroid)
                else:
                    if stack[-1] > 0 and asteroid < 0:
                        if abs(asteroid) == abs(stack[-1]):
                            stack.pop()
                        elif abs(asteroid) > abs(stack[-1]):
                            stack.pop()
                            asteroids.insert(0, asteroid)
                        else:
                            continue
                    else:
                        stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack

s = Solution()
# print(s.asteroidCollision([8, -8]))
print(s.asteroidCollision([-2, -1, 1, 2]))