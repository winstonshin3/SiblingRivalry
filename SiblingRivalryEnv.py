import gymnasium as gym

from gymnasium import spaces
from gymnasium.envs.registration import register
from stable_baselines3.common.env_checker import check_env

import SiblingRivalry as sr
import numpy as np

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, arg1, arg2, render_mode=None):
        super().__init__()

        g1 = sr.Game()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(len(g1.action_mapping))
        # Example for using image as input (channel-first; channel-last also works):
        high = np.array([])
        self.observation_space = spaces.Box(low=0, high=high,
                                            shape=(24, ), dtype=np.uint8)

    def step(self, action):
        ...
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        ...
        return observation, info

    def render(self):
        ...


# Example for the CartPole environment
register(
    # unique identifier for the env `name-version`
    id="CartPole-v1",
    # path to the class for creating the env
    # Note: entry_point also accept a class as input (and not only a string)
    entry_point="gym.envs.classic_control:CartPoleEnv",
    # Max number of steps per episode, using a `TimeLimitWrapper`
    max_episode_steps=500,
)

if __name__ == "__main__":
    pass