def reorder_lines(input_filename, output_filename):
    lines_with_space = []
    lines_without_space = []

    with open(input_filename, 'r') as file:
        for line in file:
            if ' ' in line.split('|')[0]:
                lines_with_space.append(line)
            else:
                lines_without_space.append(line)

    reordered_lines = lines_with_space + lines_without_space

    with open(output_filename, 'w') as output_file:
        for line in reordered_lines:
            output_file.write(line)

# Take user input for input and output filenames
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

reorder_lines(input_file, output_file)
