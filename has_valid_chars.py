def is_valid_string(input_string, valid_chars):
    # Check if all characters in the input string are in the valid characters list
    for char in input_string:
        if char not in valid_chars:
            return False
    return True

def main():
    valid_chars = ['0', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'c', 'd', 'e', 
                   'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 
                   'u', 'v', 'w', 'x', 'y', 'z']
    
    user_input = input("Please enter a string: ")
    
    if is_valid_string(user_input, valid_chars):
        print("The string is valid.")
    else:
        print("The string contains invalid characters.")
        print(f"Valid chars: {valid_chars}")

if __name__ == "__main__":
    main()
