def process_line(line):
    words = line.strip().split('|')
    left_synonyms = [left.split(',') for left in words[0].split('|')]
    right_synonyms = [right.split(',') for right in words[1].split('|')]
    
    result = []
    for left_group in left_synonyms:
        for right_group in right_synonyms:
            for left in left_group:
                for right in right_group:
                    if left[0] == " ":
                        left = left[1:]
                    
                    if right[0] == " ":
                        right = right[1:]

                    result.append(f"{left}|{right}")
    
    return result

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            results = process_line(line)
            for result in results:
                outfile.write(result + '\n')

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    process_file(input_file, output_file)

    print(f"Conversion complete. Results written to {output_file}")
