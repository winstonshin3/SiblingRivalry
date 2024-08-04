import gymnasium as gym

from gymnasium import spaces
from gymnasium.envs.registration import register
from gymnasium.utils.env_checker import check_env

import SiblingRivalry as sr
import numpy as np

register(
    id='sibling_rivalry',                                # call it whatever you want
    entry_point='SiblingRivalryEnv:CustomEnv', # module_name:class_name
)


class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, render_mode=None):
        super().__init__()

        self.g1 = sr.Game()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(len(self.g1.action_mapping))
        # Example for using image as input (channel-first; channel-last also works):
        high = np.array([400, 400, 40, 50, 40, 50, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])
        self.observation_space = spaces.Box(low=0, 
                                            high=high,
                                            shape=(17, ), 
                                            dtype=np.int64)

    def step(self, action):
        reward = self.g1.perform_action(action)
        obs =  self.g1.getObservation()
        observation = np.array(obs)
        terminated = False
        if self.g1.actions_taken > 8640:
            terminated = True
        truncated = False
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.g1.reset()
        obs =  self.g1.getObservation()
        observation = np.array(obs)
        info = {}
        return observation, info

    def render(self):
        self.g1.render()

if __name__ == "__main__":
    env = gym.make('sibling_rivalry', render_mode='human')
    # It will check your custom environment and output additional warnings if needed
    check_env(env.unwrapped)