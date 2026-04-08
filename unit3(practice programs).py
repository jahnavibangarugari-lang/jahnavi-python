#1.lambda function to add two numbers
add=lambda a,b:a+b
print(add(20,39))
#2.lambda function to find the square of a number
sqrt=lambda n:n*n
print(sqrt(4))
#3.lambda function to find the cube of a number
cube=lambda n:n*n*n
print(cube(10))
#4.lambda function to check whether a number is even or odd
is_even_odd = lambda n: "even" if n % 2 == 0 else "odd"
print(is_even_odd(4))  # Output: even
print(is_even_odd(7))  # Output: odd
#5.lambda function to find the maximum of two numbers
max_of_two = lambda a, b: a if a > b else b
print(max_of_two(10, 7))   # 10
print(max_of_two(3, 15))   # 15
#6.lambda with map() to add 5 to each element in a list    
list1=[1,2,3,4,5]
print(list(map(lambda a:a+5,list1)))
#7.lambda with map() to multiply corresponding elements of two lists
list1=[1,2,3,4,5]
list2=[4,5,3,2,1]
print(list(map(lambda a,b:a*b,list1,list2)))
#8.lambda with filter() to extract even numbers from a list
nums=[2,3,4,5,6,7,8]
print(list(filter(lambda a:a%2==0,nums)))
#9.lambda with filter() to extract odd numbers from a list
nums=[2,3,4,5,6,7,8]
print(list(filter(lambda a:a%2!=0,nums)))
