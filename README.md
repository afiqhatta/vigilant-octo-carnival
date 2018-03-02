# vigilant-octo-carnival
Reinforcement learning python package by Afiq Hatta. Based of exercises and theory outlined in Sutton's "Introduction to Reinforcement Learning"

## Learning strategies
<b>Epsilon-Greedy with Incremental Sample Average</b>
Currently, the package contains a test-bed and with an epsilon-greedy learner using the sample average technique. This test-bed consists of a k-armed slot machine where each arm carries a normally distributed reward function, with different means. The learner's estimates of these reward means update incrementally with each step, and most of the time seeks to maximise reward. 

## Usage: 
Users should edit the main file to conduct tests, where I use Seaborn to track the 
