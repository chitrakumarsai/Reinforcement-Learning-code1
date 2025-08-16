import gymnasium as gym

env = gym.make("LunarLander-v3")

sample_action = env.action_space.sample()
print("Sample action:",sample_action)

sample_observation = env.observation_space.sample()
print("Sample observation:",sample_observation)
