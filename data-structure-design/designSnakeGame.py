import collections


class SnakeGame:
    def __init__(self, width, height, food):
        self.snake = collections.deque([[0,0]])
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction):
        newHead = [self.snake[0][0] + self.directions[direction][0], self.snake[0][1] + self.directions[direction][1]]

        # terminal conditions
        if ((newHead[0] < 0 or newHead[0] > self.height or
            newHead[1] < 0 or newHead[1] > self.width) or
            (newHead in self.snake and newHead != self.snake[-1])):
            return -1 

        if self.food and self.food[0] == newHead: # eat food
            self.snake.appendleft(newHead) # just make the food be part of snake
            self.food.popleft() # del food thats already eaten
        else:
            self.snake.appendleft(newHead)
            self.snake.pop()

        return len(self.snake) - 1


if __name__ == '__main__':
    snake = SnakeGame(2, 1, [[0, 1]])
    print(snake.move('R'))
    print(snake.move('R'))
