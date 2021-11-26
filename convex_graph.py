# Largest Rectangle in Histogram
histogram = [ 2, 4, 8, 10, 8, 4, 2 ]
ans = []

for index in range ( 0 , len ( histogram ) ) :
    element = histogram [ index ]
    window = histogram [ index : ]
    
    if window.count( element ) == 1 : temp = [0]
    else : 
        
        end_index = histogram.index ( element , index+1 , len ( histogram ) )
        
        if end_index < len(histogram)-1 : 
            temp = histogram [ index : end_index + 1 ]
        elif end_index == len(histogram)-1 :
            temp = histogram [ index : end_index ]
        else : temp = []
        
    product = element * len ( temp )
    ans.append ( product )
    
print ( max ( ans ) )