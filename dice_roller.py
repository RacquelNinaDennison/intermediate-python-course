import random


def main():
	dice_roll = 2
	dice_roll_sum =0
	for i in range(0,dice_roll):
		roll =  random.randint(1,6)
		dice_roll_sum += roll
		print(f'You rolled a {roll}')
	print(f'You have rolled a total of {dice_roll_sum}')

if __name__== "__main__":
  main()
