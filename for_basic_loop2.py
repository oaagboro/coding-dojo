#1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(alist):
    for num in range(len(alist)):
        if alist[num] > 0:
          alist[num] = "big"
    return alist

#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(alist):
    sum = 0
    for num in range(len(alist)):
        if alist[num] > 0:
            sum +=
        alist[len(alist)-1] = sum
        return alist

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(alist):
    for num in alist:
     return sum(alist)

# 4. Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(alist):
  return sum(alist)/len(alist)

print(average([1,2,3,4])

# 5. Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(astring):
  count = 0
  for i in astring:
    count+=1
  return count

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(alist):
  current_min = alist[0]
  for num in alist:
    if num < current_min:
      current_min = num
    return current_min
print(minimum([1,2,3,4])


# 7.Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(alist):
  max_num = alist[0]
  for num in alist:
    if max_num < num:
      max_num = num
    return max_num


# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse(alist):
    new_list = []
    for x in range(len(alist)-1,-1,-1):
        new_list += alist[x]
    return new_list
