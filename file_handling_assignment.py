def create_file():
    try:
        # Create a new file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is my first line.\n")
            file.write("This is the second line with a number: 42\n")
            file.write("Finally, here's the third line!\n")
        print("File created and written successfully.")
    except PermissionError:
        print("Error: You do not have permission to create this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        # Read the contents of "my_file.txt"
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text
            file.write("Appending a new line: Python is great!\n")
            file.write("Adding another line: 100 is a nice number.\n")
            file.write("One last line to wrap things up.\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_file()  # Create and write to the file
    read_file()    # Read and display the file contents
    append_to_file()  # Append additional lines to the file
    read_file()    # Read and display the updated file contents

if __name__ == "__main__":
    main()
