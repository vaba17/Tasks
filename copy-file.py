#!/usr/bin/python3

def copy_lines_with_common_word(source_file, destination_file, common_word):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()

        matching_lines = [line for line in lines if common_word in line]

        with open(destination_file, 'w') as dest:
            dest.writelines(matching_lines)

        print(f"Lines containing the word '{common_word}' have been copied from {source_file} to {destination_file}.")

    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# User input
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")
common_word = input("Enter the common word:")

# Call the function
copy_lines_with_common_word(source_file, destination_file, common_word)
