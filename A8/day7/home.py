def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers(n)}")
    else:
        print("Please enter a positive integer.")
        for i in range(n):
            print(i ** 2)


# 1. Sum of n natural numbers
n = int(input("1. Enter a number: "))
total = n * (n + 1) // 2
print("Sum of first", n, "natural numbers is:", total)

# 2. Squares of non-negative integers less than n
n = int(input("\n2. Enter a number: "))
print("Squares of numbers less than", n)
for i in range(n):
    print(i**2)

# 3. Numbers from 0 to 6 except 3 and 6
print("\n3. Numbers from 0 to 6 except 3 and 6:")
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=' ')
print()

# 4. Fibonacci series up to n terms
n = int(input("\n4. Enter number of Fibonacci terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()

# 5. Numbers divisible by 7 and multiples of 5 between 1500 and 2700
print("\n5. Numbers divisible by 7 and multiple of 5 (1500–2700):")
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=' ')
print()

# 6. Guess the number between 1 and 9
import random
number = random.randint(1, 9)
print("\n6. Guess the number game!")
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number:
        print("Well guessed!")
        break

# 7. Count even and odd numbers until user enters 0
even_count = 0
odd_count = 0
print("\n7. Enter numbers (0 to stop):")
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

# 8. Count digits and letters in a string
text = input("\n8. Enter a string: ")
letters = digits = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("Letters", letters)
print("Digits", digits)

# 9. Rock Paper Scissors game
print("\n9. Rock Paper Scissors Game:")
while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    comp = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chose:", comp)

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break

# 10. Multiplication table of a number
num = int(input("\n10. Input a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 11. Reverse a word
word = input("\n11. Enter a word to reverse: ")
print("Reversed word is:", word[::-1])

# 12. Star pattern
print("\n12. Star Pattern:")
# Increasing part
for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()
# Decreasing part
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()
