Individual or pair (long) assignment.

(1) should be done by tomorrow, (2) and (3) by Monday.

1. Write a Python program to solve pathfinding and switch-and-door puzzles with one of the heuristic search algorithms described during the lecture. Try it on the provided sample puzzles; if some puzzles give your algorithm trouble, try to explain why that happens.
2. Once you have this working, write an agent which finds a policy for a "blind" puzzle using MCTS. "Blind" puzzles are just like the puzzles above, only (a) you don't get to see the whole puzzle or know the goal states in advance, and (b) some nodes are trap doors with a chance of dropping the player into a bottomless pit! Try different policies for deciding between exploit/explore and for doing rollouts and compare them.
3. Do (2) but with reinforcement learning. Compare various approaches and parameters against your MCTS agents in terms of iterations required to reach certain levels of performance. Read as much as you care to of Sutton & Barto---[section 2](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node39.html) is especially useful.

Eager students could implement more algorithms, select an appropriate algorithm on the fly, generate mazes on the fly, or visualize the path-finding algorithms.
