import os

def count_lines(path: str, extension: str) -> int:
    total_lines = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extension):
                file_path = os.path.join(root, name)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = sum(1 for _ in f)
                        total_lines += lines
                        print(f"{file_path}: {lines} strings")
                except Exception as ex:
                    print(f"error {file_path}: {ex}")
    print(f"\total strings: {total_lines}")
    return total_lines

count_lines("D:/Files/Texts", ".txt")