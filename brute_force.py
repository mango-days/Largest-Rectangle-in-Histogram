# Largest Rectangle in Histogram
histogram = [ 2, 4, 8, 10, 8, 4, 2 ]
max_rectangle_area = 0
ans = []

for index1 in range ( 0 , len ( histogram ) ) :
    temp = 0
    stop_index = -1
    
    for index2 in range ( index1 , len ( histogram )  ) :
        if histogram [ index2 ] >= histogram [ index1 ] : 
            temp += histogram [ index1 ]
            stop_index = index2
        else : break
    
    if temp > max_rectangle_area : 
        max_rectangle_area = temp
        ans = []
        ans.append ( index1 )
        ans.append ( stop_index )
        
print ( max_rectangle_area , ans )