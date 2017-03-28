import random as r
from pprint import pprint
import numpy as np


def tab_random_half(n,hashtab):
    if (n%2==1):
        return "Le nombre est impair"
    res=[0 for i in range(n)]
    list_int=[i for i in range(1,n+1)]
    for i in range(n//2):
        index=r.randint(0,len(list_int)-1)
        value=list_int[index]
        res[i]=value
        res[n-(i+1)]=hashtab[value]
        list_int.remove(value)
        list_int.remove(n-value+1)
    return res

def tab_random(n):
    res=[0 for i in range(n)]
    list_int=[i for i in range(1,n+1)]
    for i in range(n):
        index=r.randint(0,len(list_int)-1)
        value=list_int[index]
        res[i]=value
        list_int.remove(value)
    return res

def hash_tab(n):
    hashtab={}
    for i in range(1,n+1):
        hashtab[i]=(n+1)-i
    return hashtab






