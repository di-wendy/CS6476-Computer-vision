for row in range(height):
        for column in range(width):
            p_val = l_H[row,column]
            for i in (row-delta_h,row+delta_h+1):
                for j in (column-delta_w,column+delta_w+1):
                    if i>= 0 and j>=0 and i<height and j<width:
                        if l_H[i,j]>=p_val:
                            l_H[row,column]=0
