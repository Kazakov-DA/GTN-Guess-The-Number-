import random
Guesses_Count=0
Random_Number=random.randint(1,100)
print("The computer randomly generated the number between 1 and 100. Take your first guess")

def check(Player_Guess):
    try:
        return int(Player_Guess)
    except ValueError:
        print('Your guess must be a number!')
        return None



def hints(guess, secret):

    if guess > secret:
        print('The secret number is lower than your guess. Take another guess')
    elif guess < secret:
        print('The secret number is higher than your guess. Take another guess')
    else:

        return True

    return False



while True:
    Player_Guess = input()
    guess = check(Player_Guess)
    if guess is not None:
        Guesses_Count += 1
        if hints(guess, Random_Number):
            break


print("You won! The generated number was:", Random_Number)
print("Your total attempts:", Guesses_Count)

# # исправления:
# 1 добавлена строка после подсказки, которая призывает сделать следующий ход
# 2 В финале добавлено само загадонное число
# 3 замена 0 и 1 в выводе функции
# 5 убран звездочный импорт
# 6 пeределанно с smaller на lower и с bigger на higher


