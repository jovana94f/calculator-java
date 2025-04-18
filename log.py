import os

def count_loc(file_path):
    """Counts the lines of code in a given Java file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        loc = sum(1 for line in lines if line.strip() and not line.strip().startswith("//"))
    return loc

def calculate_loc_for_java_files(directory):
    """Calculates LOC for all .java files in the given directory."""
    loc_data = {}
    total_loc = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                loc = count_loc(file_path)
                loc_data[file] = loc
                total_loc += loc

    return loc_data, total_loc

if __name__ == "__main__":
    directory = r"c:\Users\Jovana\Downloads\calculator-java"
    loc_data, total_loc = calculate_loc_for_java_files(directory)

    print("LOC Metrics:")
    for file, loc in loc_data.items():
        print(f"- {file}: {loc} lines")
    print(f"- Total: {total_loc} lines")