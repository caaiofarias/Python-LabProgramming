def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return alist.index(item)

def binsearch(seq, search):    
   right = len(seq)
   left = 0
   previous_center = -1
   if search < seq[0]:
       return -1
   while 1:
       center = (left + right) // 2
       candidate = seq[center]
       if search == candidate:
           return center
       if center == previous_center:
           return - 2 - center
       elif search < candidate:
           right = center
       else:
           left = center
       previous_center = center
