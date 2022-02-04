# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined below.
def hello_name(user_name):
   print("hello" + user_name.upper() + "!")
   
hello_name('bob')


# Quetion 2
# Write a python function, first_odds that prints the odd numbers from 0-100 and returns nothing.
def first_odds():
   for i in range(0, 101, 2):
      print(i)
      
 def first_odds2():
   numbers = list(range(0, 101))
   for number in numbers:
      if number % 2 != 0:
         print(number)
         
first_odds()
    

# Question 3
# Please write a python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined below.
def max_num_in_list(a_list):
   max_num = max(a_list)
   return max_num
test = max_num_in_list([5,6,8,12,14])
print(max_num_in_list([5,6,8,12,14])


# Question 4
# Write a function to return if the given year is a leap year. A leap is divisible by by 4, but not divisible by 100, unless it is also divisible by 400. the return should be boolean type (true\false).
def is_leap_year(a_year):
   if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
      print(True)
   else:
      print(False)
      
is_leap_year(2018)
      
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The returns should be boolean type.
def is_consecutive(a_list):
      i = 0
      status = True
      while i < len(a_list) - 1:
         if a_list[i] + 1 == a_list[i + 1]:
            i += 1
         else:
              status = False
              break
print(status)
      

