import lxml


with open("dictionary.txt", "r") as file:
    defn = False
    printing = False
    for line in file.readlines():
        if printing:
            if not line.strip():
                printing = False
            else:
                print(line.rstrip("\n"))
        elif defn:
            if line.startswith("Defn:"):
                printing = True
                defn = False
                print(line.rstrip("\n"))
        elif line.startswith("HELL"):
            print()
            print(line.rstrip("\n"))
            defn = True
