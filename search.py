def Binary(arr,number):
    '''
    this is the fastest Search algorithm,but the array must completion sort.
    '''
    l = 0  #the left number index
    r = len(arr)    #the right number index
    while True:
        m = int((l+r)/2)     #Middle index
        n = arr[m]  #Middle number.
        if number==n:
            return m
        if number > n:
            l = m
        if number < n:
            r = m


def Linear(arr,number):
    '''
one by one search number.
    '''
    i = -1
    for x in arr:
        i = i+1
        if x==number:
            return i
