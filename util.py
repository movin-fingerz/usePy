from functools import reduce

pi = 3.141592653589793238462643383279
e  = 2.718281828459045235360287471353


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True   

def isPalindrome(n):
  if(str(n) == str(n)[::-1]):return True
  else: return False

def getFactors(n): 
    sub = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    factors = list(sub)
    return factors

def prod(array):
  t=1
  for i in array: t*=i
  return t

def fib(n):
  fibs = [0, 1]
  for i in range(2, n):
    fibs.append(fibs[-1] + fibs[-2])
  return fibs

def gcd(a, b):
  if a==0 or b==0:
    return a+b
  else:
    l=[a,b]
    m=min(l)
    M=max(l)
    return gcd(M%m,m)
  
def lcm(a, b):
  return abs(a*b)//gcd(a,b)


