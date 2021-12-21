# Monty Hall Problem Simulator

This code sample simulates the Monty Hall Problem.

The Monty Hall Problem works as follows. Assume you are on a game show and you are presented with three doors. Behind one door is a car and behind the other two doors is a goat. You don't know which is which. You select one door. The host then reveals one of the unselected doors that contains a goat. You are now presented with a choice, do you want to swap doors with the unselected closed door or keep your original selection?

Mathematically, it's always better to swap. If a player always swaps, their probability of winning is 66%, while
someone who doesn't swap only has a 33% chance of winning. This seems confusing at first as most people likley think there's a 33% chance of winning the car regardless of what they do.

The reason swapping is always better is because during the first choice to pick a door the player has a 66% chance of picking a door with a goat. The player can use this knowledge to their advantage. The host of the game show then reveals one door which contains a goat. Since the player most likely picked a goat during their first selection (66% probability), this means they should swap. The 66% probability of selecting a goat during the player's first selection now becomes the win probability provided they swap when given the choice.

My code demonstrates these probabilities by running a simulated version of the problem thousands of times. Each round of the game, the code swaps or doesn't swap depending on the outcome of a coin flip.

## Prerequisite

You must have the following software installed on your machine:

* [Python](https://www.python.org/) - version 3.7.3 or above

## Execution

To run the simulation with default settings, from the current code's project directly execute the following:

Usage:

```bash
python simulator.py
```

The default number of rounds is 10,000.

Alternative usage:

```bash
python simulator.py NUM_OF_ROUNDS
```

Where `NUM_OF_ROUNDS` is how many rounds you want to simulate.