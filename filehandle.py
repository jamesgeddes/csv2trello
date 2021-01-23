def get_file(filename):
    with open(str(filename), "r") as file:
        content = []
        for line in file:
            if line == "\n":
                pass
            else:
                content.append(str(line).strip())
        return content


def write_file(filename: str, content: list):
    with open(str(filename), "w") as file:
        for line in content:
            file.write(str(line) + "\n")
        file.flush()
    return 0


def append_file(filename, content):
    with open(str(filename), "a") as file:
        for line in content:
            file.write(str(line) + "\n")
    return 0


def get_csv(filename):
    import csv
    with open(filename + ".csv", newline="") as file:
        reader = csv.reader(file)
        out = []
        for row in reader:
            out.append(row)
        return out
