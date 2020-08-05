def FindMaxNum(arr,noindex=int):
    '''
    use it for Selection sort.
    '''
    i = 0
    max_num = arr[noindex+1]
    for x in range(noindex+2,len(arr)):
        num = arr[x]
        if num > max_num:
            max_num = num
            i = x
    return [i,max_num]



def Bubble(arr):
    '''
    swap the number if the first number>the second number.
    '''
    for n in range(len(arr)):
        for x in range(0,len(arr)-1):
            a = arr[x]
            b = arr[x+1]
            if a>b:
                arr[x],arr[x+1]=arr[x+1],arr[x]
    return arr





def Selection(arr):
    '''
    Choice max number to sort.
    '''
    global max_num_index
    first = True
    ok_num_index = 0
    for mm in range(len(arr)):
        max_num_message = FindMaxNum(arr=arr,noindex=ok_num_index)
        max_num = max_num_message[1]
        max_num_index = max_num_message[0]
        if max_num_index>=ok_num_index+1:

            if first==True:
                #swep the number
                arr[max_num_index],arr[0] = arr[0],arr[max_num_index]
                first=False
            else:
                arr[max_num_index],arr[ok_num_index+1]=arr[ok_num_index+1],arr[max_num_index]
                max_num_index=max_num_index+1


    return arr




def Insertion(arr):
    complete_index = [0]
    for x in range(len(arr)):
        # assign
        num_index = complete_index[0]+1
        num = arr[num_index]
        if len(complete_index)==len(arr):
            break
        for ok in complete_index:
            a = arr[ok]
            if num < arr[ok]:
                #swap the number
                arr[ok],arr[num_index]=arr[num_index],arr[ok]
                #To update
                num_index=ok
            else:
                complete_index.insert(0,complete_index[0]+1)
                break
    return arr

