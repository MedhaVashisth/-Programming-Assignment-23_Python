#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_symmetrical_num(n):
  return str(n) == str(n)[::-1]
print(is_symmetrical_num(121))
print(is_symmetrical_num(0))
print(is_symmetrical_num(122))
print(is_symmetrical_num(990099))


# In[6]:


# Python program to take a comma
# separated string as input


# Taking input when the numbers
# of input are known and storing
# in different variables

# Taking 2 inputs
a, b = [int(x) for x in input("Enter two values\n").split(', ')]
print("\nThe value of a is {} and b is {}".format(a, b))

# Taking 3 inputs
a, b, c = [int(x) for x in input("Enter three values\n").split(', ')]
print("\nThe value of a is {}, b is {} and c is {}".format(a, b, c))

# Taking multiple inputs
L = [int(x) for x in input("Enter multiple values\n").split(', ')]
print("\nThe values of input are", L)


# In[7]:


# Python3 implementation of the approach

# Function to return the sum
# of the digits of num ^ 2
def squareDigitSum(num):

	summ = 0
	num = int(num)
	
	# Store the square of num
	squareNum = num * num

	# Find the sum of its digits
	while squareNum > 0:
		summ = summ + (squareNum % 10)
		squareNum = squareNum//10

	return summ
	
# Driver code
if __name__ == "__main__":

	N = "1111"
	print(squareDigitSum(N))


# In[8]:


# Python 3 code to demonstrate
# removing duplicate elements from the list
l = [1, 2, 4, 2, 1, 4, 5]
print("Original List: ", l)
res = [*set(l)]
print("List after removing duplicate elements: ", res)


# In[9]:


# Python program to demonstrate mean()
# function from the statistics module

# Importing the statistics module
import statistics

# list of positive integer numbers
data1 = [1, 3, 4, 5, 7, 9, 2]

x = statistics.mean(data1)

# Printing the mean
print("Mean is :", x)


# In[ ]:




