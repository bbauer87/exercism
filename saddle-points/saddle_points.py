def saddle_points(matrix):
    result = []
    
    ## verify if matrix is valid
    if not matrix:
        return result
    
    for line in matrix:
        if len(line) != len(matrix[0]):
            raise ValueError("Irregular Matrix")   

    ## "saddle point" is greater than or equal to every element in its row
    ## and less than or equal to every element in its column.

    nro_line = column = 1
    
    for line in matrix:
        for number in line:
            if number is max(line) and number is min([list(map(int, [matrix[i][column - 1]]))[0] for i in range(len(matrix))]):
                result.append({'row': nro_line, 'column': column})
                
            column += 1
            
        column = 1
        nro_line += 1
        
    return result


### feeva solution (https://exercism.io/tracks/python/exercises/saddle-points/solutions/e9c778a5eac445bf931a85cf453832ad)
##
##def saddle_points(matrix):
##    if len(set(map(len, matrix))) > 1:
##        raise ValueError('error')
##
##    columns = list(zip(*matrix))
##    result = []
##
##    for j, row in enumerate(matrix):
##        for i, val in enumerate(row):
##            if val == max(row) and val == min(columns[i]):
##                result.append({'row': j + 1, 'column': i + 1})
##
##    return result
                
