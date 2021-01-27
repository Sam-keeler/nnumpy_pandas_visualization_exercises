import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# How many negative numbers are there?
len(a[a < 0])

# How many positive numbers are there?
len(a[a > 0])

# How many even positive numbers are there?
b = [a > 0]
c = a[b]
d = [c % 2 == 0]
len(c[d])

# If you were to add 3 to each data point, how many positive numbers would there be?
plus_three = a + 3
len(plus_three[plus_three > 0])

# If you squared each number, what would the new mean and standard deviation be?
a_sq = a**2
print(a_sq.mean())
print(a_sq.std())

# Center the data set.
mn = a.mean()
cent_a = a - mn
cent_a.mean()

# Calculate the z-score for each data point.
st_d = a.std()
mn = a.mean()
alter1 = a - mn
z = alter1 / st_d
z

# More exercises
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = a.sum()
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()
max_of_a

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean()
mean_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the 
# numbers in the above list together
product_of_a = a.prod()
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared 
# like [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = np.extract(a % 2 != 0, a)
odds_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = np.extract(a % 2 == 0, a)
evens_in_a

# Exercises w/o numpy

# sum
sum(a)

# min
min(a)

# max
max(a)

# mean
sum(a)/len(a)

# product
c = 1
for x in a:
    c = x * c
print(c)

# squares
b = []
for x in a:
    b.append(x**2)
print(b)

# odds
b = []
for x in a:
    if x % 2 != 0:
        b.append(x)
print(b)

# evens
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
print(b)


b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
b = np.array(b)
sum_of_b = np.sum(b)
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = np.min(b)
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = np.max(b)
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = np.mean(b)
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = np.prod(b)
product_of_b

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = np.square(b)
squares_of_b

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = np.extract(b % 2 != 0, b)
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = np.extract(b % 2 == 0, b)
evens_in_b

# Exercise 9 - print out the shape of the array b.
shape_of_b = np.shape(b)
shape_of_b

# Exercise 10 - transpose the array b.
trans_of_b = np.transpose(b)
trans_of_b

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
resh_of_b = np.reshape(b, (1, 6))
resh_of_b = resh_of_b.tolist()
resh_of_b

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
resh_of_b2 = np.reshape(b, (6, 1))
resh_of_b2 = resh_of_b2.tolist()
resh_of_b2


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.
print(np.min(c))
print(np.max(C))
print(np.sum(c))
print(np.prod(c))

# Exercise 2 - Determine the standard deviation of c.
print(np.std(c))

# Exercise 3 - Determine the variance of c.
print(np.var(c))

# Exercise 4 - Print out the shape of the array c
print(np.shape(c))

# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))

# Exercise 6 - Get the dot product of the array c with c. 
print(np.dot(c, c))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261
print(np.sum(c * np.transpose(c)))

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.
print(np.prod(c * np.transpose(c)))

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))

# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))

# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))

# Exercise 4 - Find all the negative numbers in d
negat_in_d = np.extract(d < 0, d)
negat_in_d

# Exercise 5 - Find all the positive numbers in d
pos_in_d = np.extract(d > 0, d)
pos_in_d

# Exercise 6 - Return an array of only the unique numbers in d.
uni_in_d = np.unique(d)
uni_in_d

# Exercise 7 - Determine how many unique numbers there are in d.
uni_in_d = np.unique(d)
len(uni_in_d)

# Exercise 8 - Print out the shape of d.
np.shape(d)

# Exercise 9 - Transpose and then print out the shape of d.
np.transpose(d)

# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9, 2))



