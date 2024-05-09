import sys
from collections import Counter

def calculate_group_occurrences(filename, groupsize):
    try:
        with open(filename, 'r') as file:
            text = file.read().replace('\n', '')
            text= text.replace(' ', '')  # Remove newlines and spaces
            groups = [text[i:i+groupsize] for i in range(len(text) - groupsize + 1)]
            group_counts = Counter(groups)
            return group_counts
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: python script.py filename groupsize")
        sys.exit(1)

    filename = sys.argv[1]
    groupsize = int(sys.argv[2])

    group_occurrences = calculate_group_occurrences(filename, groupsize)
    print("Group occurrences for group size {}: ".format(groupsize))
    for group, count in group_occurrences.items():
        print(f"'{group}': {count}")
