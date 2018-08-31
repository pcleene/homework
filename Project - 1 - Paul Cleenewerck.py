
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# # Project 1: Python Coding Exercises
# 
# _Authors: Joseph Nelson (DC) _
# 
# ---

# The following code challenges are drawn from common exercises used in technical interviews.
# 
# Please note that there may be several ways to approach each challenge. If you get stuck, try mapping out your approach in pseudocode first. Finally, while solutions to problems like these may be found online, remember that if you copy/paste code that you can't explain, you'll be missing out on the point of the project. The only way to truly learn a new skill is through practice, trial, and error - we can only help you improve by understanding where you are having trouble.

# ### Challenge 1: Largest Palindrome
# A palindromic number reads the same both ways. For example, 1234321 is a palindrome. The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two three-digit numbers. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[92]:


# determines whether or not an integer is a palindrome;
# that is, if it reads the same from both ways

def is_palindrome(n):
    s = str(n)
    letters = list(n)    
    is_palindrome = True
    i = 0

    while len(letters) > 0 and is_palindrome:       
        if letters[0] != letters[(len(letters) - 1)]:
            is_palindrome = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))

    return is_palindrome

# returns largest palindrome that is a multiple of two 3 digit numbers
# and returns -1 if no such palindrome exists

def findLargestPalindrome():
    palindrome = -1
    
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            
            # if product is palindrome and is greater than last recorded palindrome
            if isPalindrome(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome;

print (findLargestPalindrome())


# 
# ### Challenge 2: Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below 2,000. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[72]:


# Define the upper and the lower values as well as an empty list
prime_num_list = []
upper_num = 1999
lower_num = 2

# write a for loop to find all prime numbers in the range from that 

for prime_num in range(lower_num, upper_num):

#let's first assume that all numbers included in the range are Prime

    isPrime = True
    
# Using the Modulo, we then gonna check if this assumption was true. 
# We divide the first iterator by a second iterator - Each iterators go through the same list

    for t in range(2, prime_num):
            if prime_num % t == 0:
                
# As soon as the remainder of the division of the two iterators amount to 0, we mark the number as false as it is non prime

                isPrime = False
                break
                
    if isPrime:              
        prime_num_list.append(prime_num)

# create a list of unique items

unique_prime_list = set(prime_num_list)

# count the items in the list

print("There are", len(unique_prime_list), "prime numbers below 2000")
print("The sum of the primes below 2000 is equal to", sum(unique_prime_list))


# ### Challenge 3: Multiples of 3 and 5
# 
# If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1,000. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[70]:


list_1 = []

for num1 in range(3, 999):
    if num1 % 3 == 0:
        list_1.append(num1)

for num2 in range(3, 999):
    if num2 % 5 == 0:
        list_1.append(num2)

list_1 = set(list_1)

# count the items in the list

print("There are", len(list_1), "multiple of 3 and 5 below 1000")
print("The sum of the multiples of 3 and 5 below 1000 is equal to", sum(list_1))


# ### Challenge 4: String Compressor
# Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "aabcccccaaa" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[91]:


#building a function with a string as an input

def string_compression(input):

#Making sure that we return 0 in case there are no characters in the string
    if len(input) == 0:
        return ""

#setting up a counter that will increase once we notice that a character is present more than once in the string

    counter = 1
    output = ''

#define the rule to identify if a character is similar to the next one
#if the character is similar to the next one, the counter increases

    for i in range(1, len(input)):
        if input[i] == input[i-1]:
            counter += 1

#if the next character after i is not similar, we add the letter and the counter of characters as string
        
        else: 
            output += input[i-1] + str(counter) 
            counter = 1

#add the last character to the variable Output

    output  += input[-1] + str(counter)
    
    return output

string_compression("aaaaggggffff")



# ### *BONUS* Challenge: FizzBuzz
# Write a program that prints all of the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz;" for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz." Afterward, write a brief explanation walking through your code's logic in markdown.
