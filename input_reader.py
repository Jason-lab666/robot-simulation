import sys

def read_file(max_attempt=5):
    attempt = 0
    while attempt < max_attempt:
        filename = input("Enter input filename: ").strip()
        try:
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
                if len(lines) < 8:
                    sys.stderr.write("ERROR: Input file must contain at least 8 lines.\n")
                    sys.exit(1)

                rowNum = int(lines[0])
                if not (12 <= rowNum <= 100):
                    sys.stderr.write("ERROR: The number of rows was outside the specified range (12 to 100 inclusive)\n")
                    sys.exit(1)

                colNum = int(lines[1])
                if not (12 <= colNum <= 100):
                    sys.stderr.write("ERROR: The number of columns was outside the specified range (12 to 100 inclusive)\n")
                    sys.exit(1)

                robotNum = int(lines[2])
                if not (1 <= robotNum <= 10):
                    sys.stderr.write("ERROR: The number of robots was outside the specified range (1 to 10 inclusive)\n")
                    sys.exit(1)

                initType = int(lines[3])
                if not (1 <= initType <= 3):
                    sys.stderr.write("ERROR: The initialization type was outside the specified range (1 to 3 inclusive)\n")
                    sys.exit(1)

                seed = int(lines[4])
                if not (10 <= seed <= 32767):
                    sys.stderr.write("ERROR: The initialization seed was outside the specified range (10 to 32767 inclusive)\n")
                    sys.exit(1)

                iterations = int(lines[5])
                if not (5 <= iterations <= 2000):
                    sys.stderr.write("ERROR: The number of iterations was outside the specified range (5 to 2000 inclusive)\n")
                    sys.exit(1)

                interval = int(lines[6])
                if not (1 <= interval <= iterations):
                    sys.stderr.write("ERROR: The print interval was outside the specified range (1 to number of iterations inclusive)\n")
                    sys.exit(1)

                outputFile = lines[7]
                if outputFile == "":
                    sys.stderr.write("ERROR: Output file name cannot be empty.\n")
                    sys.exit(1)

                return rowNum, colNum, robotNum, initType, seed, iterations, interval, outputFile

        except FileNotFoundError:
            sys.stderr.write("ERROR: Open file unsuccessful.\n")
            attempt += 1
        except ValueError:
            sys.stderr.write("ERROR: One or more lines in the file are not valid integers.\n")
            sys.exit(1)

    sys.stderr.write("ERROR: Too many failed attempts.\n")
    sys.exit(1)