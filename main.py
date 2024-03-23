import gymnasium
import rubixcube
import numpy as np
from gymnasium.envs.registration import register
import gymnasium
from stable_baselines3 import PPO


register(
     id="gym_examples/Cube-v0",
     entry_point="rubixcube_environment:RubixCubeEnv",
     max_episode_steps=1,
)


if __name__ == '__main__':
    env = gymnasium.make('gym_examples/Cube-v0', render_mode='human')

    model = PPO("MultiInputPolicy", env, verbose=1)
    model.learn(total_timesteps=20_000)

    vec_env = model.get_env()
    obs = vec_env.reset()
    for i in range(1000):
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = vec_env.step(action)
        vec_env.render()

    env.close()




