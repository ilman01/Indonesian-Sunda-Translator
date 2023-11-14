from tqdm import tqdm

def find_matching_words(file_path):
    matching_pairs = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_iterations = len(lines) * len(lines)
    with tqdm(total=total_iterations, desc="Processing", unit="iteration") as pbar:
        for line1 in lines:
            word1 = line1.split('|')[0].strip()

            for line2 in lines:
                word2 = line2.split('|')[1].strip()

                if word1 == word2 and line1 != line2:
                    matching_pairs.append((line1.strip(), line2.strip()))

                pbar.update(1)

    return matching_pairs

# Example usage
file_path = input("file path: ")
result = find_matching_words(file_path)

if result:
    print("Matching pairs found:")
    for pair in result:
        print(pair)
else:
    print("No matching pairs found.")
