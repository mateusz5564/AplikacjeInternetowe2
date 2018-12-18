#Map

print(list(map(int, ['12', '-2', '0'])))

print(list(map(len, ['Hello', 'World'])))

print(list(map(lambda x: x[::-1], ['Hello', 'World'])))

print(list(map(lambda x: (x, x**2, x**3), range(2,6))))

print(list(map(lambda x: x[0]*x[1], zip(range(2, 5), range(3, 9, 2)))))

print(list(map(lambda x,y: x*y, range(2, 5), range(3, 9, 2))))



#Filter

print(list(filter(lambda x: (int(x) >= 0) , ['12','-2','0'])))

print(list(filter(lambda x: (x == 'world'), ['hello', 'world'])))

print(list(filter(lambda x: (x[0:2] == 'St'), ['Standford', 'Cal', 'UCLA'])))

print(list(filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(20))))



#Other Useful Tools - Reduce
#Module: functools

from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return reduce(lambda x, y: x * y / gcd(x, y), args)

print(lcm(3, 12, 18, 21))



# Other Useful Tools - Operator
#Module: operator


from functools import reduce
import operator

def fact(n):
    return reduce(operator.mul, range(1, n+1))

print(fact(3))
print(fact(7))



#Custom comparison for sort, max, and min


def alpha_score(upper_letters):
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))


def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))


#Replacing Control Flow


def funkcja(score):
    return (score == 1 and "Winner") or (score == -1 and "Loser") or "Tied"

print(funkcja(-1))



#(Challenge) Linear Algebra

import itertools
import operator

def dot_product(u, v):
    return sum(itertools.starmap(operator.mul, zip(u, v)))


print(dot_product([1, 3, 5], [2, 4, 6]))




#Matrix Transposition

def transpose(m):
    return zip(*m)

matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12)
)
print(list(transpose(matrix)))


#Matrix Multiplication


def matmul(m1, m2):
    return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))

#Lazy generation

def transpose_lazy(m):
    return zip(*m)

def matmul_lazy(m1, m2):
    return map(lambda row: (dot_product(row, col) for col in transpose(m2)), m1)




#
####Generator expressions####
#


def generate_triangles():
    n = 1
    while True:

        yield n * (n + 1) // 2
        n = n + 1

def triangles_under(n):
    x = 0
    triangles = generate_triangles()
    while x < n:
        print(x)
        x = next(triangles)

triangles_under(100)










