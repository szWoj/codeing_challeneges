# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

import numbers
import time


def solution(number):
    string = str(number)

    if string[0] == "-":
        return int("-"+string[:0:-1])
    else:
        return int(string[::-1])

print(solution(-231))
print(solution(345))


# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

# def average_length(string):
#     for item in "!?,.;":
#         string = string.replace(item, ' ')
#     print(string)
#     words = string.split()

#     return round(sum(len(word) for word in words)/len(words),2)



def average_length(sentance):
    for item in ',.?!:;':
        sentance = sentance.replace(item, " ")
    sentance = sentance.split()

    average = sum(len(word) for word in sentance) / len(sentance)

    return round(average, 2)

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
print(average_length(sentence1))


# Given a string, find the first non-repeating character in it and 
# return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are 
# already lowercase.
def non_repeating(string):
    frequency = {}
    for letter in string:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    for index in range(len(string)):
        if frequency[string[index]] == 1:
            return index
    else:
        return -1
# print(non_repeating('alphabet'))
# print(non_repeating('barbados'))
# print(non_repeating('crunchy'))

# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def palindrome(string):

    for index in range(len(string)):
        word = string[:index] + string[index+1 :]
        if word == word[::-1]:
            return True
    return string==string[::-1]

# print(palindrome('radkar'))
# print(palindrome('kayak'))
# print(palindrome('kayakk'))
# print(palindrome('kkkayak'))

# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def monotonic(list_of_numbers):
    return all(list_of_numbers[i] <= list_of_numbers[i-1] for i in range(1,len(list_of_numbers))) or all(list_of_numbers[i] >= list_of_numbers[i-1] for i in range(1,len(list_of_numbers)))

print(monotonic(A))
print(monotonic(B))
print(monotonic(C))

#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,0,10,12,0,4]

def remove_zeros(list_of_numbers):
    # for index in range(len(list_of_numbers)):
    #     if list_of_numbers[index] == 0:
            
    #         list_of_numbers.append(0)
    #         list_of_numbers.remove(0)
    # return list_of_numbers

    for number in list_of_numbers:
        if number == 0:
            list_of_numbers.append(number)
            list_of_numbers.remove(number)
            # list_of_numbers.append(0)
            # list_of_numbers.remove(0)
    return list_of_numbers

    # for number in list_of_numbers:
    #     if 0 in list_of_numbers:
    #         list_of_numbers.remove(0)
    #         list_of_numbers.append(0)
    # return list_of_numbers
print(remove_zeros(array1))
print(remove_zeros(array2))

# Given an array containing None values fill in the None values with most recent 
# non None value in the array 
array1 = [1,None,2,3,None,None,5,None]

start_time = time.time()
def most_recent(list):
    current = list[0]
    for i in range(1, len(list)):
        if list[i] is not None:
            current = list[i]
        else:
            list[i] = current
    return list

    # current = 0
    # ans = []
    # for number in list:
    #     if number is not None:
    #         current = number
    #         ans.append(current)
    #     else:
    #         ans.append(current)
    # return ans

print(most_recent(array1))
print("--- %s seconds ---" % (time.time() - start_time))

# Matched & Mismatched Words
#Given two sentences, return an array that has the words that appear 
# in one sentence and not
#the other and an array with the words in common.
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    return sorted(list(set1^set2)), sorted(list(set1&set2))

print(solution(sentence1, sentence2))

# PRIME NUMBERS 
# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive 
# divisors other than 1 and itself.
def prime(number):
    ans = []
    for num in range(number):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                ans.append(num)
    return ans

print(prime(10))