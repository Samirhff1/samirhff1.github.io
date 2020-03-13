import time
import random
MaxVal= 10
nVal = 5
listenombres = random.choises(range(MaxVal), k=Val)

def tri_insertion(L: list)->list:  
    for i in range(1, len(L)): 
        k = L[i] 
        j = i-1
        while j >= 0 and k < L[j] : 
                L[j + 1] = L[j] 
                j -= 1
        L[j + 1] = k
    return L