import random

print("In this game you will have to guess a number between 0 and 20.")
print("If you guess it correct, you win.")

try:
      x = random.randint(0, 20)
      y = int(input("Enter a guess: "))

      if x == y :
          print("You've guessed it correct.")
      elif x < y :
          print("Your guess is too high. The number was " + str(x))
      else :
          print("Your guess is too low. The number was " + str(x))

except ValueError :
      print("Please enter a number.")
      y = int(input("Enter a guess: "))
      while y != int() :
          y = int(input("Enter a guess: "))












