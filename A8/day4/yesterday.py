nelson = [10, 20, 30, 40, 50]
print(nelson)


for ram in range(2, 11, 2):
    print(ram)


lst = [1, 2, 3, 4]
total = 0
for i in lst:
    total += i
print("Sum:", total)

# lst = [1, 2, 3, 4]
# product = 1
# for i in lst:
#     product *= i
# print("Product:", product)

# lst = []
# if not lst:
#     print("List is empty")
# else:
#     print("List is not empty")


#     lst = [1, 2, 3, 4, 5, 6]
# result = [x for x in lst if x % 2 != 0]
# print(result)


# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# result = [lst[i] for i in range(len(lst)) if i not in (0, 4, 5)]
# print(result)


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# lst = [3, 4, 7, 10, 13, 15]
# primes = [x for x in lst if is_prime(x)]
# if primes:
#     print("Prime numbers:", primes)
# else:
#     print("No prime numbers")

#     lst = [1, 2, 2, 3, 4, 4]
# result = list(set(lst))
# print(result)


# lst1 = [1, 2, 3]
# lst2 = [3, 4, 5]
# combined = list(set(lst1 + lst2))
# print(combined)



# lst = [1, 2, 3, 4]
# print(lst[::-1])



# lst = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# nums = [int(x) for x in lst]
# nums.sort()
# print(nums)



# lst = [5, 3, 8]
# lst.append(10)
# lst.remove(3)
# popped = lst.pop()
# lst.insert(1, 6)
# lst.sort()
# print("List:", lst)
# print("Max:", max(lst))
# print("Min:", min(lst))



# nelson = [1, 2, 3]
# a = nelson.copy()
# print(a)



# a = [[1, 3], [3, 2], [2, 1]]
# a.sort(key=lambda x: x[1])
# print(a)



# squares = [x**2 for x in range(1, 16)]
# print("First 5:", squares[:5])
# print("Last 5:", squares[-5:])



# lst = [1, 2, 3, 4]
# result = ['emp' + str(i) for i in lst]
# print(result)




# How many values do you want to insert? 5
# Enter value 1: 10
# Enter value 2: 3
# Enter value 3: 15
# Enter value 4: 6
# Enter value 5: 20
# Enter a number to compare: 8
# Values greater than 8 are: [10, 15, 20]






















