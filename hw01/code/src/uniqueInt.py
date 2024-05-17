import os

class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        unique_integers = set()

        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                # Remove leading/trailing whitespace
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Check if the line has exactly one integer
                parts = line.split()
                if len(parts) != 1:
                    continue

                try:
                    number = int(parts[0])
                    if -1023 <= number <= 1023:
                        unique_integers.add(number)
                except ValueError:
                    # Skip lines that do not contain an integer
                    continue

        # Write the sorted unique integers to the output file
        with open(outputFilePath, 'w') as outputFile:
            for number in sorted(unique_integers):
                outputFile.write("{}\n".format(number))

# Samples
if __name__ == "__main__":
    input_folder = "/dsa/hw01/sample_inputs/"
    output_folder = "/dsa/hw01/sample_results/"

    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, "{}_results.txt".format(input_file))
        UniqueInt.processFile(input_path, output_path)
