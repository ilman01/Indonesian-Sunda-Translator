def flip_dictionary_entries(input_file_path, output_file_path):
    flipped_entries = []

    # Read the input dictionary file
    with open(input_file_path, 'r') as file:
        for line in file:
            # Split each line using '|' as the delimiter
            entries = line.strip().split('|')

            # Flip the left and right sides
            flipped_entry = f"{entries[1]}|{entries[0]}"

            # Add the flipped entry to the list
            flipped_entries.append(flipped_entry)

    # Write the flipped entries to the output file
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(flipped_entries))

# Get user input for input and output file paths
input_file_path = input("Enter the path to the input dictionary file: ")
output_file_path = input("Enter the path to the output file: ")

# Call the function with user-provided file paths
flip_dictionary_entries(input_file_path, output_file_path)

print("Flipping complete. Check the output file for the results.")
