class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            # Only need to resolve collisions when:
            # - stack is not empty
            # - current asteroid is -ve
            # - Top of stack is +ve
            while len(stack) and asteroid < 0 and stack[-1] > 0:
                # Both asteroids are equal, destory both
                continue
        return stack


if __name__ == '__main__':
    asteroids = [10, 2, -5, 8, -11]
    s = Solution()
    print(s.asteroidCollision(asteroids))