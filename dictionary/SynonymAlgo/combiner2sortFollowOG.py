from typing import OrderedDict

def process_dictionary(input_file, output_file):
    unique_entries = {}

    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split('|')
            if len(parts) == 2:
                key, value = parts
                if key not in unique_entries:
                    unique_entries[key] = [value]
                else:
                    unique_entries[key].append(value)
                    unique_entries[key].reverse()
                    unique_entries[key] = list(OrderedDict.fromkeys(unique_entries[key]))

    with open(output_file, 'w') as outfile:
        for key, values in unique_entries.items():
            common_values = ', '.join(values)
            outfile.write(f"{key}|{common_values}\n")

# Get user input for file paths
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")

# Process the dictionary
process_dictionary(input_file_path, output_file_path)
