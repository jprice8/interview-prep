def isRobotBounded(instructions) -> bool:
    pass 


def isRobotBoundedLC(instructions: str) -> bool:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # Initial position in the center
    x = y = 0

    # facing north
    idx = 0

if __name__ == '__main__':
    instructions = "GGLLGG"
    print(isRobotBounded(instructions))