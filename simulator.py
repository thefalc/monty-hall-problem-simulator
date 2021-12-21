import random
import sys

# simulator constants
HEADS = 0
WIN_STATE = 'car'
LOSE_STATE = 'goat'

# default setting for number of rounds
num_of_rounds = 10000

def main():
	if len(sys.argv) > 1:
		num_of_rounds = int(sys.argv[1])

	# dictionary to keep track of overall stats through simulation
	swap_stats = { 'total': 0, 'wins': 0}
	no_swap_stats = { 'total': 0, 'wins': 0}

	for i in range(num_of_rounds):
		# initialize lists representings doors and state of doors
		doors = [WIN_STATE, LOSE_STATE, LOSE_STATE]
		door_open_state = [False, False, False]

		# randomly configure the doors
		random.shuffle(doors)

		# player picks a random door
		selected_door = random.randint(0, 2)
		door_open_state[selected_door] = True

		# a door containing a goat is revealed
		revealed_door = get_revealed_door(door_open_state, doors)
		door_open_state[revealed_door] = True

		coin_flip = random.randint(0, 1)

		# swap doors if coin flip is heads
		if coin_flip == HEADS:
			selected_door = get_swapped_door(door_open_state, doors)
			print('Player swapped doors')
			update_stats(swap_stats, doors[selected_door])
		else:
			print('Player didn\'t swap')
			update_stats(no_swap_stats, doors[selected_door])

	print('\nALWAYS SWAP RESULT:')
	print_results(swap_stats)
	print('\nNEVER SWAP RESULT:')
	print_results(no_swap_stats)

def update_stats(stats, selected_state):
	stats['total'] += 1

	if selected_state == WIN_STATE:
		print('Player won a car')
		stats['wins'] += 1
	else:
		print('Player lost')

def print_results(stats):
	if stats['total'] > 0:
		probability_of_wins = stats['wins'] / stats['total']

		print(f'Probability of winning a car: {probability_of_wins:.4f}')
	else:
		print('No stats found, so probability could not be calculated.')
		print('Trying increasing the number of simulated rounds.')

def get_revealed_door(door_open_state, doors):
	for i in range(len(doors)):
		if door_open_state[i] == False and doors[i] == LOSE_STATE:
			return i

	return False

def get_swapped_door(door_open_state, doors):
	for i in range(len(doors)):
		if door_open_state[i] == False:
			return i

	return False

if __name__ == '__main__':
    main()