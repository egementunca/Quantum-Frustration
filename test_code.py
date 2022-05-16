from itertools import permutations
import sympy as sp
from sympy.physics.matrices import msigma
from sympy.physics.quantum import TensorProduct
sp.init_printing()

def form(a,b):
    #returns a list that contains a 'z' and b 'i' 
    return ['z']*a + ['i']*b

def formx(a,b):
    #returns a list that contains a 'z' and b 'i' 
    return ['x']*a + ['i']*b

def valid(perm):
    #checks if a permutation is valid or not
    for i in range(len(perm)-1):
        if (perm[i] == 'z' and perm[i+1] == 'z') or (perm[0] == 'z' and perm[-1] == 'z'):
            return True
    return False

def permutationX(array):
    pass

def myPermutation(array):
    #returns a list that contains every 'valid' permutation with no duplicate
    check = list(set(permutations(array)))
    out = []
    for perm in check:
        if valid(perm):
            out.append(perm)
    return out

def mySort(array, indicator): #quicksort, but checks the indices of 'z'
    if len(array)<=1:
        return array
    else:
        pivot = array.pop()
        greater=[]
        smaller=[]
        for perm in array:
            if perm.index(indicator) > pivot.index(indicator):
                greater.append(perm)
            else:
                smaller.append(perm)

        return mySort(smaller, indicator) + [pivot] + mySort(greater, indicator)

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

def changeValuesField(array,A,B):
    #every 'z' will be A, and every 'i' will be B
    #array contains all the permutations in tuple form
    out = []
    for perm in array:
        perm = list(perm)
        for i in range(len(perm)):
            if perm[i] == 'x':
                perm[i] = A
            else:
                perm[i] = B
        out.append(perm)
    return out

def fix(array):
    if array[0][1] == 'z':
        array[0],array[1] = array[1],array[0]
    return array

def bond_label(length):

    j = [sp.Symbol('J_{}1'.format(length))]
    for i in range(1,length):
        j.append(sp.Symbol('J_{}{}'.format(i,i+1)))
    return j

def field_label(length):

    h = []
    for i in range(1,length+1):
        h.append(sp.Symbol('h_{}'.format(i)))
    return h

def tensor_prod(array):

    a = TensorProduct(array[0][0],array[1][0])
    for i in range(2,len(array)):
        a = TensorProduct(a,array[i][0])
    return a

def nnInteraction(chain_length, j=None):

    z = msigma(3)
    identity = sp.eye(2)
    if j is None:
        j = bond_label(chain_length)
    combs =fix(mySort(myPermutation(form(2,chain_length-2)),'z'))
    res = sp.zeros(2**len(combs),2**len(combs))
    for i,comb in enumerate(combs):
        comb = changeValues(comb,z,identity)
        bond = j[i]
        res += bond*tensor_prod(comb)
    return res

def magneticField(chain_length, h=None):

    x = msigma(1)
    identity = sp.eye(2)
    if h is None:
        h = field_label(chain_length)
    combs = mySort(list(set(permutations(formx(1,chain_length-1)))),'x')
    res = sp.zeros(2**len(combs),2**(len(combs)))
    for i, comb in enumerate(combs):
        comb = changeValuesField(comb,x,identity)
        field = h[i]
        res += field*tensor_prod(comb)
    return res