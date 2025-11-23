# reinforcement-learning

### description:

experimenting with reinforcement learning and mixing with video games

### goals:
[] learn deep reinforcement learning from some tutorials
[] follow jperod ai reinforcement learning paper
[] make my own game + add reinforcement learning bot

### folder structure:

```
reinforcement-learning/
├── README.md
├── notebooks/         
├── models/             # Saved model checkpoints
├── logs/               # Training logs and metrics
├── configs/            # Configuration files
└── data/               # Training data, game recordings, etc.
```

### how to run

conda env create -f environment.yml
conda activate mario-rl
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf

you might have to change the .yml to include a different version of pytorch if you are on windows. im on mac so i downloaded the non-cuda version