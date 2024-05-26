class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.elements = {}

    def load_from_file(self, filePath):
        self.elements = {}
        with open(filePath, 'r') as file:
            lines = file.readlines()
            self.numRows = int(lines[0].split('=')[1])
            self.numCols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                if line.strip():
                    try:
                        row, col, value = self.parse_entry(line.strip())
                        self.set_element(row, col, value)
                    except ValueError:
                        raise ValueError("Input file has wrong format")

    @staticmethod
    def parse_entry(entry):
        if entry[0] != '(' or entry[-1] != ')':
            raise ValueError("Input file has wrong format")
        parts = entry[1:-1].split(',')
        if len(parts) != 3:
            raise ValueError("Input file has wrong format")
        row = int(parts[0])
        col = int(parts[1])
        value = int(parts[2])
        return row, col, value

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for key, value in self.elements.items():
            result.set_element(key[0], key[1], value + other.get_element(key[0], key[1]))
        for key, value in other.elements.items():
            if key not in self.elements:
                result.set_element(key[0], key[1], value)
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for key, value in self.elements.items():
            result.set_element(key[0], key[1], value - other.get_element(key[0], key[1]))
        for key, value in other.elements.items():
            if key not in self.elements:
                result.set_element(key[0], key[1], -value)
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (i, k), v in self.elements.items():
            for j in range(other.numCols):
                result.set_element(i, j, result.get_element(i, j) + v * other.get_element(k, j))
        return result

    def __str__(self):
        return f"SparseMatrix({self.numRows}, {self.numCols}, {self.elements})"

    def save_to_file(self, filePath):
        with open(filePath, 'w') as file:
            file.write(f"rows={self.numRows}\n")
            file.write(f"cols={self.numCols}\n")
            for (row, col), value in self.elements.items():
                file.write(f"({row}, {col}, {value})\n")
