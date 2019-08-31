temp = [10, 20, 30, 40]

def convert(temp):
    with open("sample.txt", "w") as file:
        for c in temp:
            f = c * 9/5 + 32
            file.write(str(f) + "\n")

convert(temp)
