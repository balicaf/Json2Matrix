def reset_matrix(data):
    matrix_size = len(data)
    matrix = matrix = [0] * 192
    print(data[0]["0"])
    for key, pairs in data[0].items():  # Assuming 'data' is a list with one dictionary
        if key not in ['ip', 'port', 'name']:
            for j in range (8):
            #print(key)
                #print(pairs[j])
                x = pairs[j][0]
                y = pairs[j][1]
                index = int(key) * 8 + j
                print(index)
                matrix[index] = x + y

    #return matrix

import csv
import json
f = open('pinMap1.json')
data = json.load(f)

# Call the function to reset the matrix
reset_matrix(data)
