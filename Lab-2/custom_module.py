class Matrix:
    def __init__(self, row_count: int, col_count: int, data: list):
        self.create(row_count, col_count, data)
    
    def create(self, row_count: int, col_count: int, data: list):
        self.rows = row_count
        self.cols = col_count
        self.mat = []
        for i in range(row_count):
            row_list = []
            for j in range(col_count):
                row_list.append(data[row_count * i + j])
            self.mat.append(row_list)
    
    def transpose(self):
        matrix_T = []
        for j in range(self.cols):
            row=[]
            for i in range(self.rows):
                row.append(self.mat[i][j])
            matrix_T.append(row)
        
        return matrix_T
    
    def det(self):
        if self.cols != self.rows:
            print('Number of columns must be equal to number of rows.')
            return

        if self.rows == 1:
            return self.mat[0]
        elif self.rows == 2:
            return self.mat[0][0] * self.mat[1][1] - self.mat[1][0] * self.mat[0][1]
        else:
            summ = 0
            for i in range(self.cols):
                minor = self.minor(0, i)
                flat_minor_list = [item for sublist in minor for item in sublist]
                summ += ((-1)**i) * self.mat[0][i] * Matrix(len(minor), len(minor[0]), flat_minor_list).det()
            return summ

    def minor(self, i, j):
        return [row[:j] + row[j+1:] for row in (self.mat[:i] + self.mat[i+1:])]
    
    def squared(self):
        if self.cols != self.rows:
            print('Number of columns must be equal to number of rows.')
            return

        C = self.zeros_matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                total = 0
                for ii in range(self.cols):
                    total += self.mat[i][ii] * self.mat[ii][j]
                C[i][j] = total

        return C
    
    def zeros_matrix(self, rows, cols):
        return [[0 for _ in range(cols)] for _ in range(rows)]