from random import randrange

def rules():
		print("This is a numerical guessing game.")
		print("You will give me two numbers.")
		print("The first number will represent the lower bounds of the range.")
		print("The second will represent the upper bounds of the range.")

def ask_range(a, b):
    a_int = int(a)
    b_int = int(b)
    if a_int > b_int:
        raise Exception("first number must be lower bound!")
    guess_range = []
    count = a_int
    while count < b_int:
        guess_range.append(count)
        count += 1
    guess_range.append(b_int)
    return guess_range

def computers_number(list = list):
		a = list[0]
		b = list[-1]
		pick = randrange(a, b+1)
		return pick

def player_guessing_logic(pick):
		g = pick
		a = input("Enter your guess!")
		a_int = int(a)
		guess = 1
		while a_int != g:
			if a_int < g:
						print("Incorrect your guess is low!")
						a = input("Enter your new guess!")
						a_int = int(a)
						guess += 1
			if a_int > g:
						print("Incorrect your guess is high! ")
						a = input("Enter your new guess!")
						a_int = int(a)
						guess += 1
		print("Correct!")
		print("You took...")
		print(guess)
		print("guesses.")
		return guess
		
def computer_guessing_logic(range):
		r = range
		c = 0 # correct bool
		g = 1 # guesses
		comp_guess = r[len(r)//2]
		print(comp_guess)
		response = input("Was I HIGH, LOW, or CORRECT?")
		low_response = response.lower()
		while c == 0:
				if "high" in low_response:
					r = r[0:r.index(comp_guess)]
					comp_guess = r[len(r)//2]
					print(comp_guess)
					response = input("Was I HIGH, LOW, or CORRECT?")
					low_response = response.lower()
					g += 1
				elif "low" in low_response:
					r = r[r.index(comp_guess)+1:]
					comp_guess = r[len(r)//2]
					print(comp_guess)
					response = input("Was I HIGH, LOW, or CORRECT?")
					low_response = response.lower()
					g += 1
				else:
					c = 1
		print("I took...")
		print(g)
		print("guesses.")
		return (g)
		
	
def main():
		rules()
		a = input("Enter your lower number!")
		b = input("Enter your upper number!")
		g = (computers_number(ask_range(a,b)))
		r = ask_range(a,b)
		player_guesses = player_guessing_logic(g)
		print("My turn!")
		pause = input("Press Enter to continue")
		computer_guesses = computer_guessing_logic(r)
		if player_guesses < computer_guesses:
			print("You win!")
		elif player_guesses > computer_guesses:
			print("You lose")
		else:
			print("You tied!")
		
		






if __name__ == "__main__":
	main()
