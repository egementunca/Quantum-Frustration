from itertools import permutations

def form(a,b):
    #returns a list that contains a 'z' and b 'i' 
    return ['z']*a + ['i']*b

def valid(perm):
    #checks if a permutation is valid or not
    for i in range(len(perm)-1):
        if (perm[i] == 'z' and perm[i+1] == 'z') or (perm[0] == 'z' and perm[-1] == 'z'):
            return True
    return False

def myPermutation(array):
    #returns a list that contains every 'valid' permutation with no duplicate
    check = list(set(permutations(array)))
    out = []
    for perm in check:
        if valid(perm):
            out.append(perm)
    return out

def mySort(array): #quicksort, but checks the indices of 'z'
    if len(array)<=1:
        return array
    else:
        pivot = array.pop()
        greater=[]
        smaller=[]
        for perm in array:
            if perm.index('z') > pivot.index('z'):
                greater.append(perm)
            else:
                smaller.append(perm)

        return mySort(smaller) + [pivot] + mySort(greater)

def changeValues(array,A,B):
    #every 'z' will be A, and every 'i' will be B
    #array contains all the permutations in tuple form
    out = []
    for perm in array:
        perm = list(perm)
        for i in range(len(perm)):
            if perm[i] == 'z':
                perm[i] = A
            else:
                perm[i] = B
        out.append(perm)
    return out


#all the permutations with  2 'z' and 4 'i'
example = myPermutation(form(2,4))

#to sort,
sortedExample = mySort(example)

#to change values,
changed = changeValues(sortedExample,'object1','object2')

print(example)
print("-----------")
print(sortedExample)
print("-----------")
print(changed)