with open("original_dictionary.txt", "r") as original_file:
    with open("modified_dictionary.txt", "w") as new_file:
        defn = False
        writing = True
        started = False
        definition = ""
        for line in original_file.readlines():
            if line.strip() == "*** START OF THIS PROJECT GUTENBERG EBOOK WEBSTER'S UNABRIDGED DICTIONARY ***":
                print("joo")
                started = True
                continue
            if started:
                if line.strip() == "*** END OF THIS PROJECT GUTENBERG EBOOK WEBSTER'S UNABRIDGED DICTIONARY ***":
                    break
                if writing:
                    if not line.strip():
                        writing = False
                        definition += "\n"
                        new_file.write(definition)
                        definition = ""
                    else:
                        definition += line

                elif defn:
                    if line.startswith("Defn:"):
                        writing = True
                        defn = False
                        definition += line

                elif line.isupper():
                    new_file.write(line)
                    defn = True
