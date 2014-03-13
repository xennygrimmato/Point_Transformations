from sys import stdout

def Show(mat):
    print 'Matrix: '
    for row in mat:
        for element in row:
            stdout.write(str(element))
            stdout.write('\t')
        print

def GetNumberOfRows():
    number_of_rows = int(raw_input())
    return number_of_rows

def GetRow():
    row = map(float, raw_input().split())
    return row

def GetMatrix():
    print 'Enter number of rows: '
    num_rows = GetNumberOfRows()
    matrix=[]
    for n in xrange(0,num_rows):
        matrix.append(GetRow())
    return matrix

def GetProduct(A , B):  # Pdt = A * B
    rows_a=len(A)
    cols_a=len(A[0])
    rows_b=len(B)
    cols_b=len(B[0])
    if cols_a != rows_b:
        print 'Incompatible matrices\n'
    else:
        pdt=[[0 for x in range(0,cols_b)] for i in range(0, rows_a)] # initializing product matrix
        
        for i in range(0, rows_a):
            for j in range(0, cols_b):
                for k in range(0, cols_a):
                    pdt[i][j]+=(A[i][k]*B[k][j])
        return pdt


def GetScalingMatrix():
    print 'Input Scaling Matrix: '
    return GetMatrix()

def GetScalingParameters_3D():
    print 'Enter Sx, Sy and Sz separated by spaces: '
    Sx, Sy, Sz = map(float, raw_input().split())
    params = [Sx, Sy, Sz]
    return params

def GetAndScale_3D(original_matrix):
    params = GetScalingParameters_3D()
    Sx, Sy, Sz = params[0], params[1], params[2]
    scaling_matrix = [[Sx,0,0,1],
                      [0,Sy,0,1],
                      [0,0,Sz,1],
                      [0,0,0,1]]
    return GetProduct(original_matrix, scaling_matrix)

def Scale_3D(original_matrix, scaling_matrix):
    return GetProduct(original_matrix, scaling_matrix)

####################

def Rotate_3D():
    pass

####################



def GetAndTranslate_3D(Tx, Ty, Tz, original_matrix):
    translation_matrix = [[1, 0, 0, 0],
                          [0, 1, 0, 0], 
                          [0, 0, 1, 0], 
                          [Tx,Ty,Tz,1]]
    
    return GetProduct(original_matrix, translation_matrix)
    
def Translate_3D(original_matrix, translation_matrix):
    return GetProduct(original_matrix, translation_matrix)




def Scale_2D():
    pass
def Rotate_2D():
    pass
def Translate_2D():
    pass

    
 
def main():
    print 'Original Matrix: '
    original_matrix = GetMatrix()
    #scaling_matrix = GetScalingMatrix()
    #Show(Scale_3D(original_matrix, scaling_matrix))
    
    Show(GetAndScale_3D(original_matrix))
    
    

if __name__ == '__main__':
    main()
