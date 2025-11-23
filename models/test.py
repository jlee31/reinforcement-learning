import warnings
warnings.filterwarnings('ignore')

import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Monkey-patch the TimeLimit wrapper to handle old Mario env
import gym
original_step = gym.wrappers.TimeLimit.step

def patched_step(self, action):
    observation, reward, done, info = self.env.step(action)
    self._elapsed_steps += 1
    if self._elapsed_steps >= self._max_episode_steps:
        info["TimeLimit.truncated"] = not done
        done = True
    return observation, reward, done, False, info

gym.wrappers.TimeLimit.step = patched_step

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

state = env.reset()
for step in range(100):
    action = env.action_space.sample()
    state, reward, done, truncated, info = env.step(action)
    env.render()
    if done:
        break

env.close()
print("✅ Test complete!")