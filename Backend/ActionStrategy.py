from abc import ABC, abstractmethod

class ActionStrategy():
    @abstractmethod
    def perform_action(self, game):
        pass

    @abstractmethod
    def get_reward(self, game):
        pass

    @abstractmethod
    def is_action_valid(self, game):
        pass

class ActionAttackMuskeeteer(ActionStrategy):
    def perform_action(self, game):
        print(game.furances)

    def get_reward(self, game):
        pass

    def is_action_valid(self, game):
        pass
