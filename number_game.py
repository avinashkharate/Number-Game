import random
n=random.randint(1,100)
guess=0
print('Enter a number from 1 to 100\n')
    
while (guess<10):
    a=int(input())
    if(a==n):
        print(f'you won in {guess} guesses')
        print("Congratulations..!")
        break
    elif (a>n):
        print('you entered greater number')
    else:
        print("you entered smaller number")
    print(f"number of guesses reamaining {10-(guess+1)}")
    guess = guess+1

if if(guess==5):
    print("You ran out of chances")