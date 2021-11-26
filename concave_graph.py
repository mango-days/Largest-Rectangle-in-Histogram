# Largest Rectangle in Histogram
histogram = [ 10, 8, 4, 2, 4, 8, 10 ]

def largest_rectangle ( histogram ) :
  
    if len( histogram ) == 2 : return ( 2 * min ( histogram ) )
    
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
        
    return ( max ( ans ) )
   
small_index = 0
max_rect = 0

for index in range ( 1, len ( histogram ) ) :
    
    if ( histogram [ index ] < histogram [ index-1 ] or index == len ( histogram )-1 ) :
        
        sub_histogram = histogram [ small_index : index+1 ]
        temp_rect = largest_rectangle ( sub_histogram )
        
        if max_rect < temp_rect : max_rect = temp_rect
        
        small_index = index
    
print ( max_rect )
