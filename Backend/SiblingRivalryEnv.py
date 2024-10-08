import gymnasium as gym
from gymnasium import spaces
from gymnasium.envs.registration import register
from gymnasium.utils.env_checker import check_env

from sb3_contrib.common.maskable.policies import MaskableActorCriticPolicy
from sb3_contrib.ppo_mask import MaskablePPO
from sb3_contrib.common.wrappers import ActionMasker

import SiblingRivalry as sr
import numpy as np

register(
    id='sibling_rivalry',                     
    entry_point='SiblingRivalryEnv:CustomEnv',
)

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 1}

    def __init__(self, render_mode=None):
        super().__init__()
        self.g1 = sr.Game()
        self.action_space = spaces.Discrete(len(self.g1.action_mapping))
        high = np.array([4000, 4000, 400, 500, 400, 500, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 6, 6, 6, 6, 6, 6])
        self.observation_space = spaces.Box(low=0, high=high, shape=(32, ), dtype=np.int64)

    def step(self, action):
        reward = self.g1.perform_action(action)
        obs =  self.g1.getObservation()
        observation = np.array(obs)
        terminated = False
        if self.g1.actions_taken > 8000:
            terminated = True
        if self.g1.actions_taken < 70:
            print("Action", action)
            self.g1.render()
        truncated = False
        info = {}
        if reward < -10:
            self.g1.render()

        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.g1.reset()
        obs = self.g1.getObservation()
        observation = np.array(obs)

        info = {}
        return observation, info

    def render(self):
        self.g1.render()
    
    def valid_action_mask(self):
        return np.array(self.g1.get_action_mask())

def mask_fn(env: gym.Env) -> np.ndarray:
    return env.valid_action_mask()        

if __name__ == "__main__":
    env = gym.make('sibling_rivalry', render_mode='human')
    # Check environment
    env = ActionMasker(env, mask_fn)
    model = MaskablePPO(MaskableActorCriticPolicy, env, gamma = 0.99999, ent_coef=0.0, verbose=0)
    model.learn(total_timesteps=1)
    # env.reset()
    # check_env(env.unwrapped)
