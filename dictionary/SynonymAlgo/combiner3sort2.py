def process_dictionary(input_file, output_file):
    unique_entries = {}

    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split('|')
            if len(parts) == 2:
                key, value = parts
                if value not in unique_entries:
                    unique_entries[value] = set([key])
                else:
                    unique_entries[value].add(key)

    with open(output_file, 'w') as outfile:
        for value, keys in unique_entries.items():
            outfile.write(f"{', '.join(keys)}|{value}\n")

# Get user input for file paths
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")

# Process the dictionary
process_dictionary(input_file_path, output_file_path)
