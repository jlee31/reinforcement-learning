# reinforcement learning

## links

- https://gymnasium.farama.org/index.html (link to the documentation)
- https://stable-baselines3.readthedocs.io/en/master/ (link to stablebaselines3 documentation)

## thoery

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

## markov decision process
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

## the bellman equation

<img width="1248" height="422" alt="image" src="https://github.com/user-attachments/assets/e0b7dc08-da52-437c-8947-5df3aaa6fbf4" />

- the policy is function used to select an action given a particular state (denoted by the function above)
- it could be random, a lookup table or even a neural network

<img width="1290" height="683" alt="image" src="https://github.com/user-attachments/assets/47e3a77e-06b7-438d-a94e-3d145076a452" />

- the equation above is recursive and known as the bellman equation for the state-value function
- it can quickly become complicated

<img width="1308" height="695" alt="image" src="https://github.com/user-attachments/assets/8302505a-6c73-4eae-b412-2268045d3f90" />

## why is this important???

- they form the basis of almost all reinforcement learning stuff
- most rl agorithms main goal is to find a policy such that it maximizes v(s) or q(s, a)
- with the policy that forms the maximized state/state action pair, you can make decisions to find the most valuable prediction at every state (making the most optimal move)

<img width="641" height="621" alt="image" src="https://github.com/user-attachments/assets/3fb7681b-9d0a-4097-b829-a443fdf73642" />

## exploitation vs exploration

<img width="1289" height="654" alt="image" src="https://github.com/user-attachments/assets/13a329bc-d743-4a51-a6f3-c72313859b71" />

- think of a restaurant, do you pick something you like the most, or pick something new in hopes to find a new favourite

### reccomended textbook given from the video

Reinforcement Learning An Introduction by Richard S. Suttin and Andrew G. Barto

http://incompleteideas.net/ > Reinforcement Learning: An Introduction (textbook) > Full PDF

^ It is a heavy read and takes a long time, but known as the Bible of RL

# Model-based vs. Model-free algorithms

Model-Based Algorithms:

- most early based algorithms were model based
- they attempted to learn the transition dynamics and awards of the markov decision process, then they find the best policy
- it was good, but didnt scale well

Model-Free Algorithm:
- you don't learn the dynamics or the rewards
- instead agents performs actions, recieves awards and updates based on the rewards it gets
- it is update policy by trial and error
- most modern reinforcement algorithms are like this

# On-policy vs. off-policy algorithms

- it is mostly a way to classify how algorithms work
- sometimes seen in literature

On-policy

- look at the next state and following the same policy

Off-policy

- if you use a different policy when estimating the return


# Discrete vs. continuous action space

Discrete:
- action possibilities are discrete
- set amount of steps
  
<img width="1125" height="385" alt="image" src="https://github.com/user-attachments/assets/bafccf3a-5dfc-4754-954b-f6de41c2dfd3" />


Continuous:
- you can specify fractional actions
- unlimited number of possible steps

<img width="1093" height="359" alt="image" src="https://github.com/user-attachments/assets/86c58fbd-0451-4180-b65a-aaa6c1a95960" />

# Discrete vs. continuous observation space

<img width="1135" height="690" alt="image" src="https://github.com/user-attachments/assets/a44c61e9-cd43-4ab5-a84a-f1d0fac49571" />

- picking the right observations and rewards are so important
- too many observation pixels / dimensions will make training a lot harder

# Overview of modern reinforcement learning algorithms

<img width="1260" height="666" alt="image" src="https://github.com/user-attachments/assets/c1516f99-fd8c-4fef-9f29-5902943dcb27" />

- usually picking based on the action space and observation space is the most important
- chatgpt is apparently really good at pixking the type reinforcement algorithm

# Q-learning

- you learn the q value of each state-action pair
- you would do this with something like a q-table

<img width="971" height="593" alt="image" src="https://github.com/user-attachments/assets/f5e5f64f-5e9d-411b-94fc-832d614af6ed" />

- as you recieve rewards, you would change the table to show the estimates of the state action returns
- it will eventually converge
- at that point, it would have an understanding of each action at each state

<img width="943" height="603" alt="image" src="https://github.com/user-attachments/assets/a6359c78-20b1-4f48-9b4d-81433f29d879" />
- so at a certain state, you might choose to the greedy action or the exploration actions (this ties back to exploitation and exploration
- this is only good for discrete action spaces
- also you have to consider state, the more states, the more state-action pairs

# Deep Q-network (DQN)

- to solve those issues, DQN is a neural network that acts as a function approximator

<img width="1070" height="663" alt="image" src="https://github.com/user-attachments/assets/20aa4310-2343-496d-b7ed-3265f704ecf1" />

- eventually it should be able to predict the q-values

### RL Terminology

- model: indicate the environment dynamics
- supervised learning: "model" = reinforcement learning: "function approximator"

### usefulness of reinforcement learning

- rl can be tough, and it still needs a lot of improvements
