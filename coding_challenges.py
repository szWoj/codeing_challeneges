# I.
import random
# from string import uppercase
import numpy
def return_given_items(list, number):
    how_many = number // len(list)
    reminder = number % len(list)
    
    if number <= len(list):
        return list[:number]
    else:
        
        ans = []
        # for i in range(how_many):
        #     for element in list:
        #         ans.append(element)
        ans = how_many*list        
        ans.extend(list[:reminder])
        return ans
        
print(return_given_items(["apple", "pear", "lemon", "orange", "mango"], 2))
print(return_given_items(["apple", "pear", "lemon", "orange"], 9))



# II. Simple operations of lists

myList = [1, 2, 3, 'EduCBA', 'makes learning fun!']
yourList = [4, 5, 'Python', 'is fun!']

# print(myList+yourList) 
# print(myList)
# # print(yourList)
# myList.extend(yourList)
# print(myList)
# print(yourList*3)


# III.
# Write a function named capital_indexes. The function takes a single parameter,
#  which is a string. Your function should return a list of all the indexes in 
# the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(word):
    # return [i for i in range(len(word)) if word[i].isupper()]
    ans = []
    for letter in word:
        if letter.isupper():
            ans.append(word.index(letter))
    return ans

print(capital_indexes("HeLlO"))


# IV.
# Write a function named mid that takes a string as its parameter. 
# Your function should extract and return the middle letter. 
# If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

# def mid(word):
#     listt = list(word)
#     if len(listt) % 2 == 0:
#         return ""
#     else:
#         while len(listt) != 1:
#             listt.pop(0)
#             listt.pop(-1)
#         return listt[0]

def mid(word):
    if len(word)%2 == 0:
        return ""
    else:
        while len(word)>1:
            word = word[1:]
            word = word[:-1]
        return word


print(mid("abc"))
print(mid("abcc"))
print(mid("abcde"))


# V.
# The aim of this challenge is, given a dictionary of people's online status,
#  to count the number of people who are online.

# Write a function named online_count that takes one parameter. 
# The parameter is a dictionary that maps from strings of names to the string 
# "online" or "offline".

# For example, consider the following dictionary:
def online_count(statuses):
    count = 0
    for key in statuses:
        if statuses[key] == 'online':
            count += 1
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))


# VI.
# Define a function, random_number, that takes no parameters. 
# The function must generate a random integer between 1 and 100, both inclusive, 
# and return it.

# Calling the function multiple times should (usually) return different numbers.

def random_number():
    return random.randint(1, 101)

print(random_number())
print(random_number())
print(random_number())


# VII.
# Write a function named only_ints that takes two parameters. 
# Your function should return True if both parameters are integers, 
# and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling 
# only_ints("a", 1) should return False

def only_ints(one, two):
    return type(one) == int and type(two)== int

# print(only_ints(1, 2))
# print(only_ints("a", 2))


# VIII.
# The goal of this challenge is to analyze a string to check if it contains 
# two of the same letter in a row. For example, the string "hello" has l twice
#  in a row, while the string "nono" does not have two identical letters in a 
# row.
# Define a function named double_letters that takes a single parameter. 
# The parameter is a string. Your function must return True if there are 
# two identical letters in a row in the string, and False otherwise.

def double_letters(word):
    for letter in range(1, len(word)):
        if word[letter] == word[letter - 1]:
            return True
    return False

print(double_letters("Hello"))
print(double_letters("papapapapapp"))
print(double_letters("NoNo"))


# IX.
# Write a function named add_dots that takes a string and adds "." 
# in between each letter. For example, calling add_dots("test") should 
# return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots 
# that removes all dots from a string. For example, calling 
# remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) 
# should return back the original string for any string.
def add_dots(word):
    ans = []
    word = list(word)
    for letter in word:
        ans.append(letter)
        ans.append(".")
    ans.pop(-1)
    return "".join(ans)

# def add_dots(word):
#     listt = list(word)
#     ans = []
#     for element in listt:
#         ans.append(element)
#         ans.append(".")
#     ans.pop(-1)
#     return "".join(ans)

print(add_dots("test"))


# X.
# Define a function named count that takes a single parameter. 
# The parameter is a string. The string will contain a single word divided 
# into syllables by hyphens, such as these:

# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
def count(word):
    counter = 1
    for element in word:
        if element == "-":
            counter += 1
    return counter

print(count("ho-tel"))
print(count("cat"))
print(count("ter-min-a-tor"))


# XI.
# Two strings are anagrams if you can make one from the other by rearranging 
# the letters.

# Write a function named is_anagram that takes two strings as its parameters. 
# Your function should return True if the strings are anagrams, 
# and False otherwise.

def is_anagram(word1, word2):
    # return word1.sort() == word2.sort() #sort() doesnt work on strings 
    return sorted(word1) == sorted(word2)

print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))



# XII.
# Write a function that takes a list of lists and flattens it into a 
# one-dimensional list.
# Name your function flatten. It should take a single parameter and return 
# a list.
# For example, calling:
# flatten([[1, 2], [3, 4]])
# Should return the list:

# [1, 2, 3, 4]

def flatten(elements):
    ans = []
    for element in elements:
        ans.extend(element)
    return ans

print(flatten([[1, 2], [3, 4]]))


# XIII.
# The goal of this challenge is to analyze a binary string consisting of 
# only zeros and ones. Your code should find the biggest number of 
# consecutive zeros in the string. For example, given the string:

# "1001101000110"
# The biggest number of consecutive zeros is 3.

# Define a function named consecutive_zeros that takes a single parameter, 
# which is the string of zeros and ones. Your function should return 
# the number described above.

def consecutive_zeros(string_number):
    result = 0
    streak = 0
    for number in string_number:
        if number == "0":
            streak+=1
        else:
            result = max(result, streak)
            streak = 0
    return result

print(consecutive_zeros("10011000001000000110"))



# XIV.
# Define a function named all_equal that takes a list and checks whether 
# all elements in the list are the same.

# For example, calling all_equal([1, 1, 1]) should return True.
def all_equal(list):
    return len(set(list)) <= 1

print(all_equal([1, 1, 1]))


# XV.
# Define a function named triple_and that takes three parameters and 
# returns True only if they are all True and False otherwise
def triple_and(one, two, three):
    return one==True and two==True and three==True
    # return one and two and three

print(triple_and(True, False, True))


# XVI.
# Define a function named convert that takes a list of numbers as its only 
# parameter and returns a list of each number converted to a string.
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
def convert(list):
    return [str(item) for item in list]

print(convert([1, 2, 3]))


# XVII.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.
def zap(a, b):
    ans = []
    for i in range(len(a)):
        ans.append((a[i], b[i]))
    return ans

print(zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
))


# XVIII.
# Your function must return whether n is exclusively in list1 or list2.
# In other words, if n is in both lists or in none of the lists, return False. 
# If n is in only one of the lists, return True.

def list_xor(n, list1, list2):
    if (n in list1 and n not in list2) or (n in list2 and n not in list1):
        return True
    else:
        return False

print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))


# XIX.
# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
# def solution(x):
#     string = str(x)

#     if string[0] == "-":
#         return int('-'+string[:0:-1])
#     else:
#         return int(string[::-1])
def revers_int(number):
    string = str(number)
    if string[0] == "-":
        string = string[:0:-1]
        return int("-"+string)
    else:
        string = string[::-1]
        return int(string)

print(revers_int(-231))
print(revers_int(345))
