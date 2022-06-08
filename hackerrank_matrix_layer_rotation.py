#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def encode(mat,r,offset):
    m = len(mat)
    n = len(mat[0])
    queue=[]
    for i in range(offset,n-1-offset):
        queue.append((offset,i))
    for i in range(offset,m-1-offset):
        queue.append((i,n-1-offset))
    for i in range(n-1-offset,offset,-1):
        queue.append((m-1-offset,i))
    for i in range(m-1-offset,offset,-1):
        queue.append((i,offset))
    return queue

def rotateQueue(q,r):
    # prevent unnecessary rotating if r is more 
    # than the length of q
    r = r%len(q)
    for i in range(r):
        t = q.pop(0)
        q.append(t)
        #print(q)

def update(mat,newMat,queue,offset):
    m = len(mat)
    n = len(mat[0])
        
    for i in range(offset,n-1-offset):
        c = queue.pop(0)
        newMat[offset][i] = mat[c[0]][c[1]]
    for i in range(offset,m-1-offset):
        c = queue.pop(0)
        newMat[i][n-1-offset] = mat[c[0]][c[1]]
    for i in range(n-1-offset,offset,-1):
        c = queue.pop(0)
        newMat[m-1-offset][i] = mat[c[0]][c[1]] 
    for i in range(m-1-offset,offset,-1):
        c = queue.pop(0)
        newMat[i][offset] = mat[c[0]][c[1]]

def matrixRotation(matrix, r):
    # Write your code here
    m = len(matrix)
    n = len(matrix[0])
    p = min(m,n)
    #print(m,n)
    newMat = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(p//2):
        queue = encode(matrix,r,i)
        #print(queue)
        rotateQueue(queue,r)
        #print(queue)
        update(matrix,newMat,queue,i)
        #print(newMat)
    
    for i in range(m):
        s = ""
        for j in range(n):
            s=s+str(newMat[i][j])+" "
        print(s)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
