import gym
import time
from gym.envs.registration import register

register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False},
    max_episode_steps=100,
    reward_threshold=0.78, # optimum = .8196
)

env = gym.make("FrozenLakeNotSlippery-v0")

# env = gym.make("Pong-v0")

env.reset()

for _ in range(200):
    time.sleep(0.05)
    env.render()
    env.step(env.action_space.sample())


