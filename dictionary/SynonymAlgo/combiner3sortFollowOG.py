from typing import OrderedDict

def process_dictionary(input_file, output_file):
    unique_entries = {}

    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split('|')
            if len(parts) == 2:
                key, value = parts
                if value not in unique_entries:
                    unique_entries[value] = [key]
                else:
                    unique_entries[value].append(key)
                    unique_entries[value].reverse()
                    unique_entries[value] = list(OrderedDict.fromkeys(unique_entries[value]))

    with open(output_file, 'w') as outfile:
        for value, keys in unique_entries.items():
            reversed_keys = ', '.join(keys)
            outfile.write(f"{reversed_keys}|{value}\n")

# Get user input for file paths
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")

# Process the dictionary
process_dictionary(input_file_path, output_file_path)
