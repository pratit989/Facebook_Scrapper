"""
# Read this to understand the code after this comment below better.

for alphabet in character_list:
    # outer for loop - denoted by higher function index in the code below. In this case 1
    output = output + alphabet
    for alphabet in character_list:
    # inner for loop - denoted by lower function index in the code below. In this case 0
        output = output + alphabet
        # do something with the acquired string of alphabets
        output = output[:-1]
    output = output[:-1]

# The number of for loops above signify the string length. Ex: Above are 2 loops. Therefore output range is aa - zz
# Only a single fixed output length can be printed depending on the number of for loops.
# Below is the same code automated using recursion. having a range from a - max string length
# The hierarchy of the for loops is denoted by the function index in the below code.

"""

character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

output = ''


def generator_function(function_index, output_string):
    # if the function index is larger that means the function does the job of for loop is on the outside
    # if it is smaller then that means the function does the job of for loop that's inside
    for character in character_list:
        output_string += character
        if function_index != 0:
            function_index -= 1
            function_index, output_string = generator_function(function_index, output_string)
        else:
            # Do something with the acquired string of character
            print(output_string)
        output_string = output_string[:-1]
    function_index += 1
    return function_index, output_string


if __name__ == '__main__':
    string_length = int(input("Enter the max string length you want: "))
    for num in range(string_length):
        generator_function(num, output)
