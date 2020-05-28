class Matrix:
    def __init__(self, matrix_string):
        matrix_as_list = matrix_string.split("\n")
        self.list_of_rows = [list(map(int , matrix_as_list[i].split())) for i in range(len(matrix_as_list))]
         
    def row(self, index):
        
        return [x for x in self.list_of_rows[index - 1]]

    def column(self, index):
        return [list(map(int, [self.list_of_rows[i][index - 1]]))[0] for i in range(len(self.list_of_rows))]
    
        #return list(map(lambda x: x[index - 1] , self.list_of_rows)) ## mesmo resultado
        
