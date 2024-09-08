
# TODO
# Add user input along with adding comments

# A
def sum_two_numbers(a, b):
    return a + b

# B
def seconds_to_hms_format(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

# C
def print_even_index_from_string(string):
    output = ""
    for i in range(len(string)):
        if i % 2 == 0:
            output+=string[i]
    print(output)

# D
def remove_duplicates_from_list(arr):
    output_arr = []
    hash_set = set([])
    for element in arr:
        if element not in hash_set:
            output_arr.append(element)
            hash_set.add(element)
    return output_arr

# E
def fibonacci(n):
    fib = [0] * (n+3)
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    for i in range(3,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

        

if __name__ == '__main__':
    # A Tests
    assert sum_two_numbers(1,2) == 3, "Test A1 Failed"
    assert sum_two_numbers(-1,2) == 1, "Test A2 Failed"
    assert sum_two_numbers(10,11) == 21, "Test A3 Failed"
    assert sum_two_numbers(-2,-2) == -4, "Test A4 Failed"

    # B Tests
    assert seconds_to_hms_format(1) == "00:00:01", "Test B1 Failed"
    assert seconds_to_hms_format(60) == "00:01:00", "Test B2 Failed"
    assert seconds_to_hms_format(3660) == "01:01:00", "Test B3 Failed"
    assert seconds_to_hms_format(3661) == "01:01:01", "Test B4 Failed"

    # C Tests
    print_even_index_from_string("Hello")
    print_even_index_from_string("World")
    print_even_index_from_string("Big Dog")    

    # D Tests
    assert remove_duplicates_from_list(["a", "a", "ab", "b", "c", "c", "c"]) == ["a", "ab", "b", "c"], "Test D1 Failed"
    assert remove_duplicates_from_list([]) == [], "Test D2 Failed"
    assert remove_duplicates_from_list([1]) == [1], "Test D3 Failed"


    # E Tests
    assert fibonacci(0) == 0, "Test E1 Failed"
    assert fibonacci(1) == 1, "Test E2 Failed"
    assert fibonacci(6) == 8, "Test E3 Failed"
    assert fibonacci(13) == 233, "Test E4 Failed"
    assert fibonacci(35) == 9227465, "Test E5 Failed"

    # Get User input and enter them into the previously tested functions
    input("Enter in 2 numbers")