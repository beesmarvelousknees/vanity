def count_attempts(file_path):
    try:
        with open(file_path, "r") as file:
            # Read the whole file content
            content = file.read()
            # Count the number of 'x' characters
            num_attempts = content.count("x")
            return num_attempts
    except FileNotFoundError:
        print("Log file not found.")
        return 0

if __name__ == "__main__":
    file_path = "count.txt"
    total_attempts = count_attempts(file_path)
    print(f"Total keys attempted: {total_attempts * 1000}")
