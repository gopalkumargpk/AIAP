def count_lines_in_file(filepath: str) -> int:
    """Return the total number of lines in the given .txt file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

print(count_lines_in_file(r"C:\Users\imgop\OneDrive\Desktop\AIAP\Assignment-4\notes.tex"))
