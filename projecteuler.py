#######################################
# projecteuler.net - python solutions # (Ruben Giannotti, 2014/2015)
#######################################

#########################
# auxiliary tools
#########################

import time, math
from itertools import chain
from collections import Counter

#method to check if n is a prime
def isprime( n ):
    if (n == 0) or (n == 1) or ((n % 2 == 0) and (n>2)):
        return False
    if n == 2:
        return True
    m = n**0.5+1; i = 3
    while i <= m:
        if n % i == 0:
            return False
        i+=2
    return True

#prime generator: sieve of eratosthenes implementation
def table_primes( limit ):
    is_prime = [True] * (limit >> 1)
    is_prime[0] = False
    for i in xrange(3,int(limit**0.5+1), 2):
        if is_prime[i >> 1]:
            for j in xrange((i >> 1) + i, limit >> 1, i):
                is_prime[j] = False
    return chain([2], ((i << 1) + 1 for i, t in enumerate(is_prime) if t))

#depricated eratosthenes: very neffizient for n<=100000
#n = 100; N = [2]+[2*k+1 for k in xrange(1,n/2)]
#for k in xrange(2,n/2+1):
#    if k in N:
#        m = k**0.5+1
#        for i in N[1:]:
#            if (i > m) and (k % i != 0):
#                break
#        for j in xrange(2,n/k+1):
#            try:
#                N.remove(k*j)
#            except ValueError:
#                pass

#generate the first n primes beneath 2000000 (n~148000)
primes = list(table_primes(2000000))

#method to do the prime factorization
def prime_factorization( n ):
	i = 0; primedivisors = []
	while n > 1:
		p = primes[i]
		if n % p == 0:
			primedivisors.append(p)
			n = n/p
		else:
			i+=1
	return primedivisors

#methods for the sigma function
def sigma_aux( k , n ):
	divisors = [1]
	for d in xrange(2,n/2+1):
		if n % d == 0:
			divisors.append(d)
	divisors.append(n)
	s = 0
	for i in divisors:
		s += i**k
	return [s,divisors]

def sigma_function( k , n ):
	return sigma_aux(k,n)[0]

def divisor_function( n ):
	return sigma_function(0,n)

def table_divisors( n ):
	return sigma_aux(0,n)[1]

#method to check if num is a palindrome
def ispalindrome( num ):
    digitstring = str(num); n = len(digitstring); m = -1
    if n % 2 == 0:
        while n-m>1:
            n=n-1; m=m+1
            if digitstring[n] != digitstring[m]:
                return False
        return True
    else:
        while n-m>0:
            n=n-1; m=m+1
            if digitstring[n] != digitstring[m]:
                return False
        return True

#palidrome generator: deprecated due to memory problems
#tempa_array = []
#
#def palindrome_generator( length ):
#    if length == 1:
#        return [0,1,2,3,4,5,6,7,8,9]
#    if length == 2:
#        return [11,22,33,44,55,66,77,88,99]
#    if length == 3:
#        for a in range(1,10):
#            for b in range(0,10):
#                tempa_array.append(a*100+b*10+a)
#        return tempa_array
#    if length > 3:
#        n = length-2
#        for a in range (1,10):
#            for pal in palindrome_generator(n):
#                tempa_array.append(a*10**(n+1)+pal*10+a)
#        return tempa_array

#method to generate collatz sequences
def collatz( n ):
	coll = [n]
	while n > 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n+1
		coll.append(n)
	return coll

#method to print solutions
def printsolution( prob , sol ):
    print '\nThe solution to problem #' + `prob` + ' is ' + `sol`
    return

#########################
# start of the solutions
#########################

start_total = time.time()

##############
# problem #1
##############
# Multiples of 3 and 5

start = time.time()

# version 1: implementing the problem directly
#s = 0
#
#for k in xrange(0,1000):
#    if (k%3==0) or (k%5==0):
#        s=s+k
#
#print s # solution: 233168

# version 2: with the help of math

s = 3*sum(xrange(0,334)) + 5*sum(xrange(0,200)) - 15*sum(xrange(0,67))


end = time.time()

printsolution(1,s) # solution: 233168

print 'Elapsed time: ' + `end-start`


##############
# problem #2
##############
# Even Fibonacci numbers

start = time.time()

s = 0; f_ppred = 1; f_pred = 1

while f_pred < 4000000:
    f_curr = f_ppred + f_pred
    if f_curr % 2 == 0:
        s = s + f_curr
    f_ppred = f_pred; f_pred = f_curr

end = time.time()



printsolution(2,s) # solution: 4613732

print 'Elapsed time: ' + `end-start`


##############
# problem #3
##############
# Largest prime factor

start = time.time()

n = 600851475143; i = 0; primedivisors = []

while n > 1:
    p = primes[i]
    if n % p == 0:
        primedivisors.append(p)
        n = n/p
    else:
        i+=1

end = time.time()

printsolution(3,max(primedivisors)) # solution: 6857
print 'Elapsed time: ' + `end-start`


##############
# problem #4
##############
# Largest palindrome product

start = time.time()

#looping backwards to find the biggest palindrom first
def find_max_palindrome_prod( digits ):
	min = 10**(digits-1); max = 10**digits
	for x in xrange((max-1)**2,min**2,-1):
		if ispalindrome(x) is True:
			d = 10**(digits-1)
			while d < max:
				if x % d == 0:
					if (x/d>=min) and (x/d<max):
						return [x,d,x/d]
				d+=1

printsolution(4,find_max_palindrome_prod(3)[0]) # solution: 913*993 --> 906609

end = time.time()

print 'The seeked factors were: ' + `find_max_palindrome_prod(3)[1:2]`
print 'Elapsed time: ' + `end-start`


##############
# problem #5
##############
# Smallest multiple

start = time.time()

#version 1: very unefficient brute force
#flag = 0; n = 1
#
#while flag != 1:
#    if n % 20 == 0:
#        if n % 19 == 0:
#            if n % 18 == 0:
#                if n % 17 == 0:
#                    if n % 16 == 0:
#                        if n % 15 == 0:
#                            if n % 14 == 0:
#                                if n % 13 == 0:
#                                    if n % 12 == 0:
#                                        if n % 11 == 0:
#                                            flag = 1
#    n+=1
#
#print n-1 # solution: 232792560
#
#end = time.time()

#version 2: better
#print all the prime factorizations... (uses prime table, see auxiliary tools)
#for n in xrange(2,21):
#    i = 0; m = n; primedivisors = []
#    while n > 1:
#        p = primes[i]
#        if n % p == 0:
#            primedivisors.append(p)
#            n = n/p
#        else:
#            i+=1
#    print 'prime divisors of n=' + `m` + ':' + `primedivisors`

#...and use mathematical knowledge
#print `19*17*13*11*7*5*3**2*2**4` # solution: 232792560

#version 3: algorithm of version 2
def find_smallest_multiple( limit ):
	primedivisors_overall = []; prime_max_multiplicities = {}
	for n in xrange(2,limit+1):
		i = 0; m = n; primedivisors = []
		while n > 1:
			p = primes[i]
			if n % p == 0:
				primedivisors.append(p)
				n = n/p
			else:
				i+=1
			primedivisors_uniqified = list(set(primedivisors))
			for u in primedivisors_uniqified:
				if u in prime_max_multiplicities:
					if Counter(primedivisors)[u] > prime_max_multiplicities[u]:
						prime_max_multiplicities[u] = Counter(primedivisors)[u]
				else:
					prime_max_multiplicities[u] = Counter(primedivisors)[u]
			primedivisors_overall = list(set(primedivisors_overall+primedivisors_uniqified))
	s = 1
	for d in primedivisors_overall:
		s *= d**prime_max_multiplicities[d]
	return s

printsolution(5,find_smallest_multiple(20)) # solution: 232792560

end = time.time()

print 'Elapsed time: ' + `end-start`


##############
# problem #6
##############
# Sum square difference

start = time.time()

#math cracks it too easily
printsolution(6,(100*(100+1)/2)**2 - 100*(100+1)*(2*100+1)/6) # solution: 25164150

end = time.time()



print 'Elapsed time: ' + `end-start`


##############
# problem #7
##############
# 10001st prime

start = time.time()

#uses prime table (see auxiliary tools)
printsolution(7,primes[10000]) # solution: 104743

end = time.time()



print 'Elapsed time: ' + `end-start`


##############
# problem #8
##############
# Largest product in a series

start = time.time()

n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

#less effective
#for j in xrange(0,988):
#    n0 = 1
#    for i in xrange(0,13):
#        n0 *= int(n[i+j])

s = 7*3*1*6*7*1*7*6*5*3*1*3*3; s_max = s

for j in xrange(1,988):
    if (int(n[j-1])==0):
        s = 1
        for i in xrange(0,13):
            s *= int(n[i+j])
    else:
        s = s/int(n[j-1])*int(n[j+12])
    if s > s_max:
        s_max = s
        factors = ''
        for i in xrange(0,13):
            factors += n[i+j] + ', '
        factors = factors[:-2]

end = time.time()

printsolution(8,s_max)
print 'The seeked digit sequence was ' + factors # solution: 5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5 --> 23514624000
print 'Elapsed time: ' + `end-start`


##############
# problem #9
##############
# Special Pythagorean triplet

start = time.time()

#version 1: brute force
#for c in xrange(0,500):
#    for b in xrange(0,c):
#        for a in xrange(0,b):
#            if a**2+b**2 == c**2:
#                if a+b+c == 1000:
#                    s = [a,b,c]
#                    break
#
#end = time.time()
#
#print s[0]*s[1]*s[2] # solution: 31875000

#version 2: use of the alternate representation of pythagorean triplets
r = 0; m = 0

while r != 500:
    m += 1
    for n in xrange(1,m):
        r = m*(m+n)
        if r == 500:
            break

n = 500/m-m
a = m**2-n**2; b = 2*m*n; c = m**2+n**2
s = a*b*c
v = [a,b,c]

end = time.time()

printsolution(9,s) # solution: 31875000
print 'The seeked triple was ' + `v` # [200,375,425]
print 'Elapsed time: ' + `end-start`


##############
# problem #10
##############
#Summation of primes

start = time.time()

#p_i<2000000 for i<=148933
printsolution(10,sum(primes[0:148933])) # solution: 142913828922

end = time.time()

print 'Elapsed time: ' + `end-start`


##############
# problem #11
##############
#Largest product in a grid

grid = []

grid = []
grid.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
grid.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
grid.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
grid.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
grid.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
grid.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
grid.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
grid.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
grid.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
grid.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
grid.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
grid.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
grid.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
grid.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
grid.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
grid.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
grid.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
grid.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
grid.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
grid.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
 
grid = [i.split() for i in grid]
grid = [[int(j) for j in i] for i in grid]

grid_rev = []

for a in xrange(len(grid)):
	grid_rev.append(grid[a][::-1])

start = time.time()

s_max = 0

#horizontal and vertical products
for i in xrange(20):
	for j in xrange(17):
		if (j == 0) or (grid[i][j-1] == 0):
			s_hor = 1
			for k in xrange(4): s_hor *= grid[i][k+j]
		else:
			s_hor = s_hor/grid[i][j-1]*grid[i][j+3]
		if s_hor > s_max: s_max = s_hor

		if (j == 0) or (grid[j-1][i] == 0):
			s_ver = 1
			for k in xrange(4): s_ver *= grid[k+j][i]
		else:
			s_ver = s_ver/grid[j-1][i]*grid[j+3][i]
		if s_ver > s_max: s_max = s_ver

#diagonal products
for array in [grid,grid_rev]:
	for a in xrange(17):
		for b in xrange(17-a):
			if (b == 0) or (array[a+b-1][b-1] == 0):
				s_for_upp = 1
				for k in xrange(4): s_for_upp *= array[a+b+k][b+k]
			else:
				s_for_upp = s_for_upp/array[a+b-1][b-1]*array[a+b+3][b+3]
			if s_for_upp > s_max: s_max = s_for_upp

			if (b == 0) or (array[b-1][a+b-1] == 0):
				s_for_low = 1
				for k in xrange(4): s_for_low *= array[b+k][a+b+k]
			else:
				s_for_low = s_for_low/array[b-1][a+b-1]*array[b+3][a+b+3]
			if s_for_low > s_max: s_max = s_for_low

end = time.time()

printsolution(11,s_max) # solution : 70600674
print 'Elapsed time: ' + `end-start`


##############
# problem #12
##############
# Highly divisible triangular number

start = time.time()

limit = 500

n = 0; t = 0; s = 1
while s < limit+1:
	n = n+1; t += n; s = 1
	fact = Counter(prime_factorization(t))
	if t == 1:
		p_max = 1
	else:
		p_max = max(k for k, v in fact.iteritems() if v)
	for p in primes:
		if p > p_max:
			break
		if p in fact:
			s *= (fact[p]+1)

end = time.time()

printsolution(12,t) # solution: 76576500
print 'Elapsed time: ' + `end-start`


##############
# problem #13
##############
# Large sum

list_data = open("projecteuler_13_aux.dat","r")

L = []; carry = []

for line in list_data:
	striped_line = line.strip()
	L.append(str(striped_line))

list_data.close()

start = time.time()

for x in reversed(xrange(50)):
	a = 0
	for n in L:
		if len(n) >= x:
			a += int(n[x])
	carry.append(a*10**(49-x))

s = str(sum(carry))[0:10]

end = time.time()

printsolution(13,s) # solution: 5537376230...
print 'Elapsed time: ' + `end-start`


##############
# problem #14
##############
# Longest Collatz sequence

start = time.time()

limit = 1000000; c_max = 0

#only the upper half of the intervall needs to be checked due to identeties of subpaths of the collaz sequences
for k in xrange(limit/2,limit):
	c = len(collatz(k))
	if c > c_max: c_max = c; c_start = k

end = time.time()

printsolution(14,c_start)
print `end-start` # ~ 16s


##############
# problem #15
##############
# Lattice paths

start = time.time()

#breaks down to a combinatorics problem: multinomial(40;20,20)=binomial(20+20,20)=40!/(20!*20!)
s = math.factorial(40)/(math.factorial(20)*math.factorial(20))

end = time.time()

printsolution(15,s) # solution: 137846528820
print `end-start`


##############
# problem #16
##############
# Power digit sum

tart = time.time()

limit = 1000; digits = [1]

for n in xrange(limit):
	digits[:] = [x*2 for x in digits]
	for a in digits:
		if a >= 10:
			i = digits.index(a)
			digits[i] += -10
			if i < len(digits)-1:
				digits[i+1] += 1
			else:
				digits.append(1)

end = time.time()

printsolution(16,sum(digits)) # solution: 1366
print `end-start`


end_total = time.time()

##############
# problem #17
##############
# Number letter counts

def hex_digits_verb ( d ):
    if d == 0:  temp = ''
    if d == 1:  temp = 'one'
    if d == 2:  temp = 'two'
    if d == 3:  temp = 'three'
    if d == 4:  temp = 'four'
    if d == 5:  temp = 'five'
    if d == 6:  temp = 'six'
    if d == 7:  temp = 'seven'
    if d == 8:  temp = 'eight'
    if d == 9:  temp = 'nine'
    if d == 10: temp = 'ten'
    if d == 11: temp = 'eleven'
    if d == 12: temp = 'twelve'
    if d == 13: temp = 'thirteen'
    if d == 14: temp = 'fourteen'
    if d == 15: temp = 'fifteen'
    return temp

def tens_verb ( t ):
    if t == 0: temp = ''
    if t == 1: temp = 'teen'
    if t == 2: temp = 'twenty'
    if t == 3: temp = 'thirty'
    if t == 4: temp = 'forty'
    if t == 5: temp = 'fifty'
    if t == 6: temp = 'sixty'
    if t == 7: temp = 'seventy'
    if t == 8: temp = 'eighty'
    if t == 9: temp = 'ninety'
    return temp

def powers_ten_verb ( x ):
    if x == 10: temp = 'ten'
    if x == 100: temp = 'hundred'
    if x == 1000: temp = 'thousend'
    if x == 1000000: temp = 'million'
    return temp

def numbernames ( n ):
    num = str(n); temp = ''
    if n < 16:
        temp += hex_digits_verb(n)
    elif n >= 16 and n < 20:
        if n == 18:
            temp += 'eighteen'
        else:
            temp += hex_digits_verb(int(num[1])) + tens_verb(int(num[0]))
    elif n < 100:
        temp += tens_verb(int(num[0]))
        if int(num[1]) != 0:
            temp += '-' + hex_digits_verb(int(num[1]))
    elif n < 1000:
        temp += hex_digits_verb(int(num[0])) + ' hundred'
        n = n - int(num[0])*100
        if n != 0:
            temp += ' and ' + numbernames(n)
    else:
        temp = 'not yet finished'
    return temp

def number_letter_count( n ):
    s = numbernames(n)
    s = s.replace('-','')
    s = s.replace(' ','')
    return len(s)

def number_letter_counts( n ):
    s = 0
    for m in xrange(n):
        s += number_letter_count(m)
    return s

#print number_letter_counts(1000) + len('onethousand')# transform number_letter_counts(100) to basic arithmetic as total count below

start = time.time()

N = 10*number_letter_counts(100)# strings of numbers from 0-99 occur in every segment of the hundreds

units = [3,3,5,4,4,3,5,5,4]

K1 = 7*900# length of string 'hundred' (=7) appears 9*100=900 times in total
K2 = 3*891# length of string 'and' (=3) appears 9*99=891 times in total
K3 = len('onethousand')

s = N + K1 + K2 + K3# number of static strings

for i in xrange(9):# adding the number of changing strings
    s += units[i]*100

end = time.time()

printsolution(17,s)#
print `end-start`


##############
# problem #18
##############
# Maximum path sum I

def max_path_sum( t ):
    for i,j in [(i,j) for i in range(len(t)-2,-1,-1) for j in range(i+1)]:
        t[i][j] +=  max([t[i+1][j],t[i+1][j+1]])
    return t[0][0]

tri = [
        [75],
        [95,64],
        [17,47,82],
        [18,35,87,10],
        [20,4,82,47,65],
        [19,1,23,75,3,34],
        [88,2,77,73,7,63,67],
        [99,65,4,28,6,16,70,92],
        [41,41,26,56,83,40,80,70,33],
        [41,48,72,33,47,32,37,16,94,29],
        [53,71,44,65,25,43,91,52,97,51,14],
        [70,11,33,28,77,73,17,78,39,68,17,57],
        [91,71,52,38,17,14,91,43,58,50,27,29,48],
        [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
        [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
    ]

start = time.time()

printsolution(18,max_path_sum(tri))#

end = time.time()

print `end-start`


##############
# problem #19
##############
# Counting Sundays

daycount = [31,28,31,30,31,30,31,31,30,31,30,31]
firsts = [32]

for x in xrange(11): firsts.append(firsts[x]+daycount[x+1])

firsts_leap = [32] + [i+1 for i in firsts[1:12]]

def sundays_count( limit ):
    o = 1; s = 0
    for y in xrange(1901,limit+1):
        if y%4 == 0 and (y%100 != 0 or y%400 == 0):
            for f in firsts_leap:
                a=0
                for n in xrange(a,54):
                    if 7*n-o == f: s=s+1
                    a=a+4
            o = (o+2)%7
        else:
            for f in firsts:
                a=0
                for n in xrange(a,54):
                    if 7*n-o == f: s=s+1
                    a=a+4
            o = (o+1)%7
    return s

start = time.time()

printsolution(19,sundays_count(2000))#

end = time.time()

print `end-start`


##############
# problem #20
##############
# Factorial digit sum

start = time.time()

r = '1'

for k in xrange(1,100):
    r = int(r)*k
    fac = str(r).strip('0')

s = 0

for d in fac:
    s += int(d)

printsolution(19,s)#

end = time.time()

print `end-start`


##############
# problem #21
##############
# Amicable numbers

start = time.time()

N = range(2,10001)
s = 0

while N:
    x = N[0]
    d_x = 0
    for j in xrange(1,x/2+1):
        if x%j == 0:
            d_x += j
    d_d_x = 0
    for k in xrange(1,d_x/2+1):
        if d_x%k == 0:
            d_d_x += k
    if d_d_x == x and (x != d_x):
        s += x
    N = N[1:]

printsolution(21,s)#

end = time.time()

print `end-start`


##############
# problem #22
##############
# Names scores

end = time.time()

def alph2sum ( uc_str ):
    return sum([ord(char)-64 for char in uc_str])
    
f = open('p022_names.txt', 'r')

for line in f:
    names = line.split(',')
names = [n.strip('"') for n in sorted(names)]
    
f.close()

s=0

for i in xrange(len(names)): s += (i+1)*alph2sum(names[i])

printsolution(22,s)#

end = time.time()

print `end-start`


##############
# problem #23
##############
# Non-abundant sums


##############
# problem #24
##############
# Lexicographic permutations

start = time.time()

perm = []; loopcount = 0

A = range(10)
for a in A:
    if loopcount == 1000000: break
    B = copy.copy(A)
    B.remove(a)
    for b in B:
        C = copy.copy(B)
        C.remove(b)
        for c in C:
            D = copy.copy(C)
            D.remove(c)
            for d in D:
                E = copy.copy(D)
                E.remove(d)
                for e in E:
                    F = copy.copy(E)
                    F.remove(e)
                    for f in F:
                        G = copy.copy(F)
                        G.remove(f)
                        for g in G:
                            H = copy.copy(G)
                            H.remove(g)
                            for h in H:
                                I = copy.copy(H)
                                I.remove(h)
                                for i in I:
                                    J = copy.copy(I)
                                    J.remove(i)
                                    for j in J:
                                        perm.append('%s%s%s%s%s%s%s%s%s%s' % (a,b,c,d,e,f,g,h,i,j))
                                        loopcount += 1

printsolution(24,perm[999999])#

end = time.time()

print `end-start`


end_total = time.time()

print 'Total time of computation: ' + `end_total-start_total`

#########################
# end of the solutions
#########################
