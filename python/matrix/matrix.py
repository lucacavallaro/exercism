class Matrix:
    def __init__(self, matrix_str):
        self.matrix = [[int(el) for el in row.split()] for row in matrix_str.splitlines()]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
