# Tutorial followed from https://www.youtube.com/watch?v=AoGRjPt-vms&t=764s

import random
from enum import Enum

class RobotAction(Enum):
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3

class GridTile(Enum):
    _FLOOR = 0
    ROBOT = 1
    TARGET = 2

    def __str__(self):
        return self.name[:1]
    
class WarehouseRobot:

    def __init__(self, grid_rows = 4, grid_cols = 5):
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.reset()

    def reset(self, seed=None):
        self.robot_pos = [0,0]
        random.seed(seed)
        self.target_pos = [
            random.randint(1, self.grid_rows-1),
            random.randint(1, self.grid_cols-1)
        ]

    def perform_action(self, robot_action:RobotAction) -> bool:
        if robot_action == RobotAction.LEFT:
            if self.robot_pos[1] > 0:
                self.robot_pos[1] -= 1
        elif robot_action == RobotAction.RIGHT:
            if self.robot_pos[1] < self.grid_cols - 1:
                self.robot_pos[1] += 1
        elif robot_action == RobotAction.UP:
            if self.robot_pos[0] > 0:
                self.robot_pos[0] -= 1
        elif robot_action == RobotAction.DOWN:
            if self.robot_pos[0] < self.grid_rows - 1:
                self.robot_pos[0] += 1
        
        return self.robot_pos == self.target_pos
            
    def render(self):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                if ([r,c] == self.robot_pos):
                    print(GridTile.ROBOT, end = ' ')
                elif ([r,c] == self.target_pos):
                    print(GridTile.TARGET, end = ' ')
                else:
                    print(GridTile._FLOOR, end = ' ')
            print()
        print()

if __name__ == "__main__":
    warehouseRobot = WarehouseRobot()
    print()
    print("Starting State:")
    print()
    warehouseRobot.render()

    for i in range(25):
        rand_action = random.choice(list(RobotAction))
        print(rand_action)

        warehouseRobot.perform_action(rand_action)
        warehouseRobot.render()