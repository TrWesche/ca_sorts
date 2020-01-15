def radix_sort(to_be_sorted):
    being_sorted = to_be_sorted[:]              # Copys the entire list to a new variable
    maximum_value = max(to_be_sorted)           # Finds the maximum value in the entire list
    max_exponent = len(str(maximum_value))      # Converts that maximum value to a string and finds the length of that string
    # return(max_exponent)

    for exponent in range(max_exponent):        # Looks at the length of the longest string and sets up a for loop which will run that many times
        # position = exponent + 1
        # index = - position
        index = - (exponent + 1)                # Finds the negative index which will be used to pull the LSD of the current loop out of the individual value strings
        digits = [[] for digit in range(10)]    # Creates an empty list of lists which act as buckets for each number to be stored in cylically while sorting (0,1,2,..,9)

        for number in being_sorted:             # Loops through the being sorted list number by number
            number_as_a_string = str(number)    # Converts current number to a string
            try:                                # Trys to find the single character at the negative index of the string.  Since some strings are longer then others this may result in an IndexError which must be handled
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            digit = int(digit)                  # Converts the digit to an integer to be used in placing the number in the appropriate bucket
            digits[digit].append(number)
            
        # return digits
        being_sorted = []                       # Clears the being sorted list for it to be rebuilt again
        for numeral in digits:                  # Rebuilds the entire list cyclically as the sort occurs
            being_sorted.extend(numeral)
    
    return being_sorted


unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

print(radix_sort(unsorted_list))