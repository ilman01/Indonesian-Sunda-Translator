input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

with open(input_file, 'r') as file:
    lines = file.readlines()

updated_lines = []

for line in lines:
    left_side, right_side = line.strip().split('|')
    reversed_left_side = ', '.join(reversed([s.strip() for s in left_side.split(',')]))
    updated_line = f"{reversed_left_side}|{right_side}\n"
    updated_lines.append(updated_line)

with open(output_file, 'w') as file:
    file.writelines(updated_lines)

print(f"Reversed the left side using s.strip() and left the right side unchanged. Saved the result in {output_file}.")
