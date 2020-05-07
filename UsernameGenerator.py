"""
# Read this to understand the code after this comment below better.

for alphabet in alphabet_list:
    # outer for loop - denoted by higher function index in the code below. In this case 1
    output = output + alphabet
    for alphabet in alphabet_list:
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

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

output = ''


def generator_function(function_index, output_string):
    # if the function index is larger that means the function does the job of for loop is on the outside
    # if it is smaller then that means the function does the job of for loop that's inside
    for alphabet in alphabet_list:
        output_string += alphabet
        if function_index != 0:
            function_index -= 1
            function_index, output_string = generator_function(function_index, output_string)
        else:
            # Do something with the acquired string of alphabet
            print(output_string)
        output_string = output_string[:-1]
    function_index += 1
    return function_index, output_string


if __name__ == '__main__':
    string_length = int(input("Enter the max string length you want: "))
    for num in range(string_length):
        generator_function(num, output)
