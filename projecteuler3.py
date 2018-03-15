#######################################
# projecteuler.net - python 3 solutions
  # (problems 26-)
  # Ruben Giannotti, 2018-
#######################################

#########################
# auxiliary tools
#########################

import time
from math import gcd as bltin_gcd

#method to print the solution
def printsolution(prob,sol,time=(0,0)):
  print('Solution to problem '+str(prob)+': '+str(sol))
  if time[1] > 0:
    print('Elapsed time: '+str(round(time[1]-time[0],4))+'s')

#method to check if number is prime
def isprime(n):
  return not (n<2 or any(n%x == 0 for x in range(2,int(n**0.5)+1)))

#method to check if two numbers are coprime
def iscoprime2(n,m):
  return bltin_gcd(n,m) == 1


start_total = time.time()

##############
# problem #26
##############
# Reciprocal cycles

start = time.time()

cycle_length_max = 0

for i in range(1000):
  if i != 0:
    if i%2 != 0:
      rem = 1
      rem_list = [rem]
      digits_list = []
      while rem !=0:
        while rem<=i:
          rem = rem*10
          digits_list.append(0)
        digits_list = digits_list[:-1]
        digit = rem//i
        rem = rem%i
        if rem in rem_list:
          cycle_length = len(digits_list)+1-rem_list.index(rem)
          if cycle_length > cycle_length_max:
            cycle_length_max = cycle_length
            cycle_length_max_index = i
          break
        else:
          rem_list.append(rem)
          digits_list.append(digit)

end = time.time()

printsolution(26,cycle_length_max_index,(start,end))


##############
# problem #27
##############
# Quadratic primes

start = time.time()

n = 1000
check_init = []

for i in range(n):
  for j in range(-n+1,0):
    if iscoprime2(i,j):
      check_init.append([i,j])

check_init_flipped_signs = []

for c in check_init:
  check_init_flipped_signs.append([i*(-1) for i in c])

check_init = check_init + check_init_flipped_signs

check_flipped_signs = []

for c in check_init:
  check_flipped_signs.append([i*(-1) for i in c])

check = check_init + check_flipped_signs

def testprime(n,a,b):
  return n**2+a*n+b

max_prime_streak = 0
max_tuple = []

for c in check:
  temp_prime_streak = 0
  n = 0
  p = testprime(n,c[0],c[1])
  while isprime(p):
    temp_prime_streak += 1
    n += 1
    p = testprime(n,c[0],c[1])
  if temp_prime_streak > max_prime_streak:
    max_prime_streak = temp_prime_streak
    max_tuple = c

end = time.time()

printsolution(27,max_tuple[0]*max_tuple[1],(start,end))#-59231
#print(max_prime_streak,max_tuple)#71, [-69,971]


##############
# problem #28
##############
# Number spiral diagonals

start = time.time()

N = 1001

sum = 1
curr_num = 1

for n in range(1,N,2):
  for k in range(4):
    curr_num += n+1
    sum += curr_num

end = time.time()

printsolution(28,sum,(start,end))
#669171001

##############
# problem #29
##############
# Distinct powers

start = time.time()

N = 100

distinct_powers = []

for a in range(2,N+1):
  for b in range(2,N+1):
    power = a**b
    if power not in distinct_powers:
      distinct_powers.append(power)

number_all_powers = (N-1)*(N-1)
number_distinct_powers = len(distinct_powers)

end = time.time()

printsolution(29,number_distinct_powers,(start,end))
#9183

#print(number_all_powers)
#print(number_distinct_powers)
#print(number_all_powers-number_distinct_powers)
#print(count_double_powers)


##############
# problem #30
##############
# Digit fifth powers

#slow!~13s
#start = time.time()

#digit_five_powers = []

#for n in range(100,1000000):
#  fifth_power_sum = 0
#  for s in str(n):
#    fifth_power_sum += int(s)**5
#  if n == fifth_power_sum:
#    digit_five_powers.append(n)

#end = time.time()

#printsolution(30,123,(start,end))
#sum(digit_five_powers)
#443839

#print(digit_five_powers)
#[4150, 4151, 54748, 92727, 93084, 194979]
#print(sum(digit_five_powers))
#443839

def find_digit_powers(power):
  digit_powers = []
  n = 1
  arrayFull = False
  if power > 0:
    while not arrayFull:
      n += 1
      # TODO pls check this ruben, maybe the maximal amount of elements in the
      #      array is known beforehand?
      if power > 3:
        if(len(digit_powers) == 3*(power-3)):
          arrayFull = True
      else:
        if n > 10000:
          arrayFull = True
      find_digit_powers_process(n,power,digit_powers)
  return digit_powers

def find_digit_powers_process(num,exp,arr):
  digit_powers_sum = 0
  for s in str(num):
    digit_powers_sum += int(s)**exp
  if num == digit_powers_sum:
    arr.append(num)
  return arr

start = time.time()
problem_number = 30
problem_power = 5
result = sum(find_digit_powers(problem_power))
end = time.time()
printsolution(problem_number,result,(start,end))
#443839

#print(find_digit_powers(problem_power))
#[4150, 4151, 54748, 92727, 93084, 194979]
#print(sum(result))
#443839


##############
# problem #x
##############
# title

#start = time.time()



#end = time.time()

#printsolution(x,solution,(start,end))


end_total = time.time()

print('Total time of computation: '+str(round(end_total-start_total,4))+'s')

#########################
# end of the solutions
#########################
