# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# nums = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]


nums = [ 1,2,3,4,-2,-4,-6,-8]
[ 4, -20]

def  solution ( nums):
    if not  nums:
        return []
    count= 0
    total =0
    for num in nums :

        if  num>0 :
            count += 1
        else :
            total += num
    return  [ count, total ]

# def solution(nums):
#     if not nums:
#         return []

#     count = 0
#     total = 0
#     for i in nums:
#         if i > 0:
#             count += i
#         else:
#             total += i
#     return [count, total]        

def solution(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

   

# for i in numbers:
#     if i > 0:
#         positive = i + array

# print(positive)


# for i in numbers:
#     if i > 0:
#         positive = i + array

# print(positive)





