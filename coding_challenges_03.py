import string

ans = []
for num in range(100, 201):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        ans.append(num)

print(ans)


l = [1,4,2,5,3,6,7,3,5,9,0,2,1]
l = sorted(l)
print(l)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(0, 12):
    print(fib(i))

n = [i for i in range(10)]
print(n)

def reverse_list(list):
    return list[::-1]

print(reverse_list(n))


listt = [1,2,3,1,"mama", "tata", "mama"]
listt1 = set([i for i in listt if listt.count(i)>1])
print(listt1)

# You own a Goal Parser that can interpret a string command. 
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", 
# and "(al)" as the string "al". The interpreted strings are then concatenated 
# in the original order.
def interpret(command):
    if "()" in command:
        command = command.replace("()","o")
    if "(al)" in command:
        command = command.replace("(al)", "al")
    return command

print(interpret("G()()()()(al)"))

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
def isValid(s):
#         while (len(s)!=0):
#             s = s.replace('()','')
#             s = s.replace('{}','')
#             s = s.replace('[]','')
            
#         if (len(s)==0):
#             return True
#         else:
#             return False
        
    while True:
        if "()" in s:
            s=s.replace("()", '')
        elif "{}" in s:
            s=s.replace("{}", '')
        elif "[]" in s:
            s=s.replace("[]", '')
        else:
            return not s

print(isValid("()[]{}"))
print(isValid("()[]{)}"))

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

def balancedStringSplit(s):
    ans = []
    r_count = 0
    l_count = 0
    substring = ""
    for letter in s:
        
        if letter == "R":
            r_count += 1
            substring += "R"
        if letter == "L":
            l_count += 1
            substring += "L"
        while r_count == l_count and r_count!= 0:
            ans.append(substring)
            r_count = 0
            l_count = 0
            substring = ""
    return ans

print(balancedStringSplit("RLRRLLRLRLRRLL"))

# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
def decodeMessage(key, message):
        
        
    key = key.replace(" ", "")
    key= ''.join([j for i,j in enumerate(key) if j not in key[:i]])
    
    letter_count = dict(zip(string.ascii_lowercase, key))
    print(letter_count)
    ans = []
        
    for letter in message:
        if letter == " ":
            ans.append(" ")
        else:
            for key_in_dict, value in letter_count.items():
                if value == letter:
                    ans.append(key_in_dict)
    return "".join(ans)

print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))

def sortSentence(s):
    ans = s.split(" ")
    ans.sort(key=lambda x: x[-1])
    ans = [word[0:-1] for word in ans]
    return " ".join(ans)
    # s= s.split(" ")
    # ans = [""] * len(s)
    # for item in range(len(s)):
    #     item = ''.join([i for i in item if not i.isdigit()])
    #     ans[item[-1] -1 ] = item
    # return ans





s = "is2 sentence4 This1 a3"
print(sortSentence(s))

# A string is a valid parentheses string (denoted VPS) if it meets one of the following:

# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

# Given a VPS represented as string s, return the nesting depth of s.
def maxDepth(s):
        """
        :type s: str
        :rtype: int
        """
        opening_count = 0
        maxi = 0
        
        for item in s:
            if item == "(":
                opening_count+= 1
                maxi = max(opening_count, maxi)
                
            elif item == ")":
                opening_count -=1
                maxi = max(opening_count, maxi)
                
        return maxi

print(maxDepth("(1+(2*3)+(((8))/4))+1"))


# You are given a string allowed consisting of distinct characters and an 
# array of strings words. A string is consistent if all characters in the string 
# appear in the string allowed.
# Return the number of consistent strings in the array words.

def countConsistentStrings(allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        not_matched = 0
        
        for string in words:
            for char in string:
                if char not in allowed:
                    not_matched +=1
                    break
        return len(words) - not_matched

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))


# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.
def truncateSentence(s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.split(" ")
        s = s[: k]
        return " ".join(s)


abc = string.ascii_lowercase
# print(abc)

def checkIfPangram(sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        return len(set(sentence))==26

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
