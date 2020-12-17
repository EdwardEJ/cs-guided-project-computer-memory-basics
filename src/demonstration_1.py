"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string: str) -> str:
    # Your code here
    # look up Python `ord`
    # ord() converts letter to integer representation
    # chr() converts integer converts back to letter
    # 1 bit integer difference between lowercase and uppercase
    # if 3rd digit is 0 it's uppercase, if 1 it's lowercase
    
    ## Alternative:
    #
    
    # encoded_chars = []
    # for char in string:
    #   encoded_chars.append(ord(char))
    # This code does the same thing:
    encoded_chars = [ord(char) for char in string]

    # for i in range(len(encoded_chars)):
    #   if encoded_chars[i] >= 65 and encoded_chars[i] <= 90:
    #     encoded_chars[i] += 32

    for i, v in enumerate(encoded_chars):
      if v >= 65 and v <= 90:
        encoded_chars[i] += 32

    # decoded_chars = []
    # for n in encoded_chars:
    #   decoded_chars.append(chr(n))
    #This code does the same thing:
    decoded_chars = [chr(n) for n in encoded_chars]

    return ''.join(decoded_chars)

print(to_lower_case('LLAMA'))
print(to_lower_case('LambdaSchool'))