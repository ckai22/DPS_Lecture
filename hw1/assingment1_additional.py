from math import *
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import time

def isPrime(N):
    if N <= 1:
        return False

    if N == 2 :
        return True
    
    if N%2 == 0 :
        return False
    
    for i in range(2, int(N**0.5+1)):
        if N%i == 0:
            return False
    
    return True

#N이 소수인지 아닌지를 검사하는 함수 
def isPrimeSieve(N):
    #초기화
    
    if N <= 1:
        return False
    
    if N == 2:
        return True
    
    #짝수의 경우 초기화에서 처리
    primFlags = [False if (x)%2==0 else True for x in range(0,N + 1)]
    primFlags[0] = False
    primFlags[1] = False
    primFlags[2] = True
    
    for i in range(3, int(sqrt(N)) + 1):
        #소수가 아닌 경우 건너띄는 부분
        if primFlags[i] == False:
            continue
            
        if N%i == 0:
            return False
        
        #해당 소수의 배수는 전부 제외
        interval = 2 * i
        next = i + interval
        while next < int(sqrt(N)) + 1:
            primFlags[next] = False
            next += interval
    
    return primFlags[N]

def isPrimeSpeedCheck(NS):
    elapsed = []
    for n in NS:
        st = time.clock()
        primes = []
        for m in range(1, n):
            if isPrime(m):
                primes += [m]
        elapsed += [time.clock() - st]
    return elapsed

def isPrimeSieveSpeedCheck(NS):
    elapsed = []
    for n in NS:
        st = time.clock()
        primes = []
        for m in range(1, n):
            if isPrimeSieve(m):
                primes += [m]
        elapsed += [time.clock() - st]
    return elapsed

NS = range(1000, 10000, 1000)

prev_elapsed = isPrimeSpeedCheck(NS)
prime_sieve_elapsed = isPrimeSieveSpeedCheck(NS)

plt.grid()

plt.xlabel('Required Range Limit \'N\'')
plt.ylabel('Elapsed Time (s)')

prev_line = mlines.Line2D([], [], color='r', marker='s', markersize=7, label='Prev')
sieve_line = mlines.Line2D([], [], color='m', marker='s', markersize=7, label='BS')
plt.legend(handles=[prev_line, sieve_line])

plt.plot(NS, prev_elapsed, 'r')
plt.plot(NS, prev_elapsed, 'rs', label='Prev')
plt.plot(NS, prime_sieve_elapsed, 'm')
plt.plot(NS, prime_sieve_elapsed, 'ms')

import matplotlib.pylab as pylab
params = {'legend.fontsize': '25',
          'figure.figsize': (13, 13),
         'axes.labelsize': '25',
         'axes.titlesize':'25',
         'xtick.labelsize':'25',
         'ytick.labelsize':'25'}
pylab.rcParams.update(params)

plt.show()