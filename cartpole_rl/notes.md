# reinforcement learning

### links

- https://gymnasium.farama.org/index.html (link to the documentation)
- https://stable-baselines3.readthedocs.io/en/master/ (link to stablebaselines3 documentation)

### thoery

<img width="975" height="722" alt="image" src="https://github.com/user-attachments/assets/9efa8b97-2b49-4e49-a0a7-9d39d2c1c90a" />

- this is similar to our bodies, our eyes -> brain -> actions -> hormones

Observation:
- cart position
- cart velocity
- pole angle
- pole angular velocity

- observation for more complex things could be the a frame of pixels (like for a video game)

Reward:
+1 for each time step

Action:
0 - move left
1 - move right

Gymnasium is a library forked from OpenAI Gym - which is the code that acts for the interpreter and environment
- it comes with envrionments like cartpole

StableBaselines 3 is a training algorithm for reinforcement learning

### markov decision process
- a way to model decision making in discrete time slices
- you would consider every moment of time as some type of state
- with computers, you would let states be continuous

<img width="967" height="688" alt="image" src="https://github.com/user-attachments/assets/1e29a2d6-91ac-4bcc-b31c-67bb107cb7ef" />

- the yellow lines are actions , they are possible choices to the agent
- the blue lines are the possible outcomes of an action
- so the agent obsers the state, decides an action, the environment has some sort of transition and you can see the result, then the process repeats

<img width="1094" height="679" alt="image" src="https://github.com/user-attachments/assets/eceafbdc-dff3-43e3-95fa-2004c5995504" />
- the agent would then be rewarded based on the type of action it does
- obviously some models might want to always pick the option with the best reward, but ai also has the ability for delayed gratification

### the bellman equation
