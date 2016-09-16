def find_parallel(peaks):
# type peaks: List[List[int,int]]
        dst_list = []
        
        for i in range(len(peaks)):
            for j in range(i,len(peaks)):
                k = (peaks[i][0]*1.0-peaks[j][0]*1.0)**2
                h = (peaks[i][1]*1.0-peaks[j][1]*1.0)**2
                new_dst = np.sqrt(k+h)
                dst_list.append([new_dst,i,j])
        sort_d = sorted(dst_list,key=lambda student : student[0],reverse = True)
        
        return sort_d[1:3][0:4]
