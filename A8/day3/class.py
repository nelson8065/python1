# my_list = [1,2,3,4,5]
# for item in my_list:
#     print(item)


# for i in range(1,11):
    
#         print(i)

#  i=(1,2,3,4,5,6,7,8,9,10,11)
# a = i % 2== 0
# print(a)

nums = [10,3,5,1,8]
largest = nums[0]
smallest= nums[0]

for num in nums:
    if num > largest:
    largest = num
    if num < smallest:
        smallest = num
        print("largest:",largest)
        print("")