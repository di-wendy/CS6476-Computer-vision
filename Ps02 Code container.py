def hough_peaks(H, Q, cols, rows, hough_threshold=200, nhood_radii=(5, 5)):
    """

    Parameters
    ----------
        H (numpy.array): Hough accumulator array
        Q (int): number of peaks to find (max)
        cols (numpy.array): 1D array with column values, ie. theta = [-pi : pi]
        rows (numpy.array): 1D array with row values, ie. rho = [-x : x]
        hough_threshold (float): minimum value in accumulator array for peaks
        nhood_radii (tuple): a pair of integers indicating the distance in the rho and
                    theta directions over which non-maximal suppression should take place

    Returns
    -------
        peaks (numpy.array): A matrix where each row is a (col_id, row_id) pair where the peaks are.

    """
    peaks = []
    height,width = H.shape
      
    
    #print H    
    delta_h = nhood_radii[0]
    delta_w = nhood_radii[1]
    
    H_copy = np.copy(H)
    
    cv2.normalize(H_copy,H_copy,0,255,cv2.NORM_MINMAX) 
    #def maxima supression
    def supress (row,column):
        delta_h = nhood_radii[0]
        delta_w = nhood_radii[1]
        p_val = H_copy[row,column]
        for i in range(row-delta_h,row+delta_h+1):
            for j in range(column-delta_w,column+delta_w+1):
                if i>= 0 and j>=0 and i<height and j<width:
                    if H_copy[i,j]>p_val:
                        return 0
                    if H_copy[i,j]==p_val:
                        H_copy[i,j]==0
        return p_val
    
    for row in range(height):
        for column in range(width):
            peaks.append((supress(row,column),row,column))

            
    
    sort_peak = sorted(peaks,key=lambda student : student[0],reverse = True)
    result = np.array(sort_peak,dtype=int)
    
    global k
    k = 0
    
    #Set threshold
    for k in range(len(result)):
        if result[k,0]>=hough_threshold:
            continue
        else:
            break

    return_len = min(len(sort_peak),Q,k) #Controled by length, input and threshold

    return result[0:return_len,1:3]  # TODO: change to return peaks
