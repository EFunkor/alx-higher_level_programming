def remove_char_at(input_str, n):
    # Check if the index n is valid
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if the index is out of bounds
    
    # Create a new string by slicing the input string before and after the character at index n
    result_str = input_str[:n] + input_str[n+1:]
    
    return result_str

# Test the function
original_str = "Hello, World!"
n = 5  # Remove the character at index 5 (C-style index)
new_str = remove_char_at(original_str, n)
print(new_str)

