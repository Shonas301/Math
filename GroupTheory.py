# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 17:10:11 2016

@author: Jason Shipp
"""
import pickle, os
from random import randint
import re
from groups import *
from fractions import gcd

"""
Solution for 1:

Method: is_cayley_table
@param: List table

Description: Takes the list of lists table, type checks it to make sure it contains the
right type of elements, and that the size of the columns is equal to the size of the 
rows, then checks to make sure that the elements contained are all integers, less
than the size of the table length (n). If all criteria are met it is a valid cayley
table
"""
def is_cayley_table(table):
    if not type(table) is list:
        return False    
    if not type(table[0]) is list:
        return False
    size = len(table[0])
    
    for i in table:
        if len(table) is not len(i):
            return False
        if not type(i) is list:
            #print("Not a subgroup at all")
            return False
        if len(i) is not size:
            #print("Not the right subgroup size")
            return False
        for j in i:
            if type(j) is not int:
                #print("not an int")                
                return False
            if j < 0:
                #print("less than zero")
                return False
            if (j >= size):
                #print("too large")
                return False
    return True

"""
Solution for 2:

Method: problem2
@param: void

Description: Runs all the test cases for is_cayley_table described for problem 2, results
are listed beneath the call as a comment
"""
def solution2():
#2a
  a = "banana"
  is_cayley_table(a)
#returns false
#2b
  b = [["a","b","c"],["b","c","a"],["c","b","a"]]
  is_cayley_table(b)
#returns false
#2c
  c = [[0,1,1,3],[3,2,1,1],[3,3,0,3],[0,3,0,3]]
  is_cayley_table(c)
#returns true
#2d
  d = [[1,1,0],[1,1],[0,1,1]]
  is_cayley_table(d)
#returns false
#2e
  e = [[1, 1, 2], [2, 3, 1], [0, 0, 1]]
  is_cayley_table(e)
#returns false
#2f
  f = [[1, 1, 2, 1], [2, 3, 1, 3], [0, 0, 1, 0], [0, 0, 1, 0], [1, 2, 3, 0]]
  is_cayley_table(f)
#returns false
#2g
  g = [1, 1, 0], [0, 1, 2], [1, 2, 2]
  is_cayley_table(g)
#returns false
#2h
  h = [1,1,0,0,1,2,1,2,2]
  is_cayley_table(h)
#returns false
#2i
  i = [[1, 1, 2],[0, 1, 1, [1, 1, 0]]]
  is_cayley_table(i)
#returns false
#2j
  j = [[1, 0, 1], [0, 0, 1], [0, 1, 2]]
  is_cayley_table(j)
#returns true

   
"""
Solution for 3:

Method: random_cayley_table
@param: Int n

Description: Creates a nxn matrix for the assigned length, then creates integers to
populate it from 0 to n-1 using the randint function.
"""
def random_cayley_table(n):
    assert(n > 0 and type(n) is int), "Value Error"
    
    table = []
    for i in range(n):
        table.append([])
        for j in range(n):
            table[i].append(randint(0,n-1))
    return table   

"""
Solution for 4:

There are n^n^n possible Cayley tables for those defined by the set {0,1,...,n-1} 
as there are n choices for each value in an n by n grid.
"""
    
"""
Solution for 6:

Method: is_associative_cayley_table
@param: List table

Description: First checking to make sure the table fed in is in fact a valid cayley table
the function checks every possible triple contained in the table to insure that 
x*(y*z) is (x*y)*z
"""
def is_associative_cayley_table(table):
  if not is_cayley_table(table):
        return False
  n = len(table)
  for x in range(n):
    for y in range(n):
      for z in range(n):
        a = table[x][y]
        b = table[a][z]
        c = table[y][z]
        d = table[x][c]
        if b is not d:
         return False
  return True

"""
Solution for 6
"""
def solution6():
  tableOne = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,1,0,1],[0,0,0,2,1,1,2],[0,0,0,0,1,1,2]]
  tableTwo = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,1,0,1],[0,0,0,2,1,1,2],[0,0,0,0,1,1,6]]
  tableThree = [[0,0,0,0,0,0,0],[0,1,0,0,0,0,1],[0,0,2,2,2,2,0],[0,0,2,3,2,2,0],[0,0,2,2,4,4,0],[0,0,2,2,4,5,0],[0,1,0,0,0,0,6]]
  tableFour = [[0,1,2,3,4],[1,0,4,2,3],[2,3,0,4,1],[3,4,1,0,2],[4,2,3,1,0]]
  tableFive = [[0,1,2,3,4],[1,2,4,0,3],[2,4,3,1,0],[3,0,1,4,2],[4,3,0,2,1]]
  tableSix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0]]
  is_associative_cayley_table(tableOne)
#returns true
  is_associative_cayley_table(tableTwo)
#returns false
  is_associative_cayley_table(tableThree)
#returns true
  is_associative_cayley_table(tableFour)
#returns false
  is_associative_cayley_table(tableFive)
#returns true
  is_associative_cayley_table(tableSix)
#returns false

   
"""
Method: row_cayley_table
@param: List table, Int index

Description: Returns the row of the table described in the index if no error is raised
"""
def row_cayley_table(table, index):
  if not is_cayley_table(table) or not type(index) is int:
    raise TypeError
  elif index >= len(table) or index < 0:
    raise ValueError
  return table[index]

    
"""
Method: col_cayley_table
@param: List table, Int index

Description: Returns the column of the table described in the index if no error is raised
"""
def col_cayley_table(table, index):
  if not is_cayley_table(table) or not type(index) is int:
    raise TypeError
  elif index >= len(table) or index < 0:
    raise ValueError

  col = []
  for i in xrange(len(table)):
    col.append(table[i][index])
  return col

"""
Solution for 7:

Method: identity_cayley_table
@param: List table

Description: Takes in a valid cayley table and iterates over each row and column of the
table to see if the values in it correspond to the set {0,1,...,n-1} which shows the 
identity of the table. If there are more than one identity it keeps track of that and
appends it to a table.
"""
def identity_cayley_table(table):
  if not is_cayley_table(table):
    raise TypeError
  n = len(table)
  i = -1
  isE = False
  x = []
  y = []
  for j in range(n):
    x.append(j)
  for j in range(n):
    isE = True
    row = row_cayley_table(table,j)
    col = col_cayley_table(table,j)
    for k in range(n):
      if row[k] is not x[k] or col[k] is not x[k]:
        isE = False
    if isE is True:
      i = j
      y.append(i)
  if len(y) > 1:
    return y
  return i

"""
Method: test
@param: void

Description: Just used to test the identity function nothing else
"""
def test():
  table = [[0,1,2],[0,0,0],[0,1,1]]
  print("e is ", identity_cayley_table(table))
  table = [[0,0,2],[0,1,2],[0,2,1]]
  print("e is ", identity_cayley_table(table))
 
"""
Method: is_commutive_cayley_table
@param: List table

Description: Helper method which checks the cayley table to see if the group described
is commutive by running through every i*j and j*i and makes sure they are equal
"""
def is_commutive_cayley_table(table):
  if not is_cayley_table(table):
    raise TypeError
  Commutive = True
  n = len(table)
  for i in range(n):
    for j in range(n):
      if table[i][j] is not table[j][i]:
        Commutive = False
        return Commutive
  return Commutive

"""
Method: has_inverse_cayley_table
@param: List table, Int e

Description: takes in a valid cayley table, and checks to make sure every row and column
contains the identity for that group, ensuring that for each x in the group has a value
which produces the identity. 
"""
def has_inverse_cayley_table(table, e):
  if not is_cayley_table(table):
    raise TypeError
  n = len(table)
  for i in range(n):
    row = row_cayley_table(table, i)
    col = col_cayley_table(table, i)
    if type(e) is int:
      if e not in row or e not in col:
        return False
    else:
      ePrime = e[0]
      if e not in row or e not in col:
        return False
  return True



"""
Solution for 8:

Method: is_group_cayley_table
@param: List table

Definition: Takes in a cayley table and runs various methods on it compiling the results
into a list which is returned giving which of the axioms are fulfilled, and if the table
provided describes a group.
"""
def is_group_cayley_table(table):
  Closure = False
  Associativity = False
  Identity = False
  Inverses = False
  Multiple = 0
  Commutive = True

  if is_cayley_table(table):
    Closure = True

  if is_associative_cayley_table(table):
    Associativity = True

  e = identity_cayley_table(table)
  if e is not -1:
    Identity = True
    if type(e) is not int:
      Multiple =+ 1

  Commutive = is_commutive_cayley_table(table)
  
  if Identity:
    Inverses = has_inverse_cayley_table(table,e)

  Group = Closure and Associativity and Identity and Inverses

  return [Group, Closure, Associativity, Identity, Inverses, Commutive, Multiple]

       
def solution8():
  dir = os.path.dirname(__file__)
  tabs = pickle.load(file(dir + "cayley-tables-3.p", "rb"))
  a = 0
  b = 0
  c = 0
  cA = 0
  d = 0
  e = False
  f = False
  for table in tabs:
    x = is_group_cayley_table(table)
#counts the amount of groups
    if x[0]:
      a += 1
#returns 3
#counts all the abelian groups
    if x[0] and x[4]:
      b += 1
#returns 3
#counts all the tables that are commutative but not associative
    if x[5] and not x[2]:
      c += 1
#returns 666
#counts all the tables that are associative but not commutative
    if not x[5] and x[2]:
      cA += 1
#returns 50
#counts all the tables that have multible identities
    if x[-1] is not 0:
      d += 1
#returns 0
#checks if associativity is fulfilled but not identity and invers
    if x[2]:
      if not x[3] and not x[4]:
        e = True
#returns true
#checks if identity is fulfilled but not associativity nor invers
    if x[3]:
      if not x[2] and not x[4]:
        f = True
#returns true
#8a
  #print("How many of the Cayley Tables on {0,1,2} define groups: ", a)
#returns 3
#8b
  #print("How many of the Cayley tables on {0,1,2} define abelian groups: ", b)
#returns 3
#8c
  #print("How many of the Cayley tables on {0,1,2} are commutative but not associative: ", c)
#returns 666
#8d
  #print("How many are associative but not commutative ", cA)
#returns 50
#8e
  #print("Do any of the Cayley tables on {0,1,2} have more than one identity: ", d)
#returns 0
#8f
  #print("Can you find a Cayley table on satisfying the associativity axiom but neither the identity nor inverses axioms ", e)
#returns True
#8g
  #print("Can you find a Cayley table satisfying the identity axiom but neither the associativity nor inverses axioms" , f)
#returns True

solution2()
solution6()
solution8()

"""
Solution for 5.1:

Method: order_group_element
@param: Group g, Perm x

Description: Takes in a group x and an permutation x, ensuring first
that they fit those qualifications. It then utilizes the definition of 
order from the notes Definition 11.1, and takes successive powers of the
permutation until it is equal to the Group identity, at which point it
returns how many powers it has taken.
"""
def order_group_element(G,x):
  if not (IsSymmetricGroup(G) and IsPerm(x)):
    raise ValueError
  y = x
  i = 1
  while not (y == G.identity()):
    y = y*x
    i += 1
  return i  

"""
Solution for 5.2:

Method: solutionTwo
@param: void

Description: Runs all of the Permutations listed in 5.2 using the method
defined for the solution to 5.1 as opposed to the algortihm used for 
5.3
"""
def solutionTwo():
  #2a
  perm = Perm((1,2,3),(4,5,6),(10,11,112))
  order_group_element(SymmetricGroup(perm.degree()),perm)
  #Returns: 3
  #2b
  perm = Perm((1,3),(4,5),(6,8,10),(7,9))
  order_group_element(SymmetricGroup(perm.degree()),perm)
  #Returns: 6
  #2c
  perm = Perm((1,4,3,2,12,7,10,5),(9,11))
  order_group_element(SymmetricGroup(perm.degree()),perm)
  #Returns: 8
  #2d
  perm = Perm((1,8,12,9,7,5,4,11,10,2),(6,13))
  order_group_element(SymmetricGroup(perm.degree()),perm)
  #Returns: 10
  #2e
  perm = Perm((1,9,8,13,10,5),(2,14),(3,6,4,7,11,12))
  order_group_element(SymmetricGroup(perm.degree()),perm)
  #Returns: 6

"""
Solution for 5.3:

Method: solutionThree
@param: void

Description: Reads in the massive perumtation as described in the python
object provided and calls an external method which works based upon 
Definition 11.12 and Corollary 11.13, i.e lcm(m1,m2,m3,...,mn) for
the cycle decribed under p.
"""
def solutionThree():
  dir = os.path.dirname(__file__)
  p = pickle.load(file(dir + "my-huge-perm.p", "rb"))

  #I do NOT caclulate the symmetric group on p with degre 100000 as it 
  #takes too much computing power and times out the machine I am working
  #on. For referenee the code is:
  #G = SymmetricGroup(p.degree())
  order_group_element_large(p)
  #Returns: 17,431,821,765,154,920,624,670,282,823,376,665,752,284,251,760

"""
Method: lcm
@param: List[int] numbers

Description: A helper method for the solution of 5.2 which takes the list
of lengths of the disjoint cycles. It then recursivly iterates over the
elements in the list numbers using the definition of the least common 
multible. The lambda function reduce works as lcm(x1,lcm(x2,lcm(x3,x4)))
"""
def lcm(numbers):
  return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

   
"""
Method: order_group_element_large
@param: Perm x

Description: Takes in a large permutation x and breaks it up into it's component number
strings using a basic regex string parser. It then takes the length of each number strip
and takes the lcm of all those permutations to compute the order of the permutation.
"""
def order_group_element_large(x):
  s = str(x)
  y = [" ".join(x.split()) for x in re.split(r'[()]',s) if x.strip()]
  x = []
  for z in y:
    x.append(z.split(" "))

  for i in range(len(x)):
    x[i] = len(x[i])
  return lcm(x)

"""
Solution for 4:

Method: is_subgroup
@param: Group G, List H

Description: Takes in a group G and and a list of permutations H and checks the definitions
layed down in Theorem 12.5 to see if H is a subgroup. The axioms it checks for are closure
and Inverses
"""
def is_subgroup(G,H):
  if not (IsSymmetricGroup(G) and type(H) is list):
    raise TypeError
  for h in H:
    if not h in G:
      return False
  for x in H:
    for y in H:
      if x*y not in H or x*y not in G:
        return False
  for x in H:
    if x**-1 not in G:
      return False
  return True

"""
Solution for 5:

Method: is_cyclic_subgroup
@param: Group G, List H

Description: First checks that the subgroup in H is in fact a subgroup, and then checks each
element represented in H to see if it can generate H. If no element can generate H then
it is not cyclic by definition of a cyclic subgroup
"""
def is_cyclic_subgroup(G,H):
  if not is_subgroup(G,H):
    return False
  Ha = []
  x = None
  for h in H:
    Ha = []
    x = h*h
    Ha.append(h)
    while not(x == G.identity()) and not(x == h):
      Ha.append(x)
      x = x*h
    Ha.append(x)
    cyclic = True
    for h in H:
      if not (h in Ha):
        cyclic = False
        break
    if cyclic is True:
      return True
  return False

"""
Solution for 6:

Method: solutionSix
@param: void

Description: Checks all of the subgroup possibilities described in 6
"""
def solutionSix():
#6a
  H = [Perm((1,2,3)),Perm(),Perm((1,3,2))]
  G = SymmetricGroup(11)
  is_subgroup(G,H)
#Return: True
  is_cyclic_subgroup(G,H)
#Return: False
#6b
  H = [Perm((1,2,3)),Perm(),Perm((1,3,2))]
  G = SymmetricGroup(2)
  is_subgroup(G,H)
#Return: False
  is_cyclic_subgroup(G,H)
#Return: False
#6c
  H = [Perm((1,2)), Perm(), Perm((3,4))]
  G = SymmetricGroup(4)
  is_subgroup(G,H)
#ReturnL False
  is_cyclic_subgroup(G,H)
#Return: False
#6d
  H = [Perm((1,2)),Perm(),Perm((3,4)), Perm((1,2),(3,4))]
  G = SymmetricGroup(5)
  is_subgroup(G,H)
#Return: True
  is_cyclic_subgroup(G,H)
#Return: False

"""
Solution for 7a:

Method: is_abelian_group
@param: void

Description: checks first if it's a subgroup, then makes sure that every unit x and every
unit y in H x*y is y*x
"""
def is_abelian_subgroup(G,H):
  if not is_subgroup(G,H):
    return False
  for x in H:
    for y in H:
      if not(x*y == y*x):
        return False
  return True
  
def solutionSevenB():
#7ba
  H = [Perm((1,2,3)),Perm(),Perm((1,3,2))]
  G = SymmetricGroup(11)
  is_abelian_subgroup(G,H)
#Returns True
#7bb
  H = [Perm((1,2,3)),Perm(),Perm((1,3,2))]
  G = SymmetricGroup(2)
  is_abelian_subgroup(G,H)
#Returns False
#7bc
  H = [Perm((1,2)), Perm(), Perm((3,4))]
  G = SymmetricGroup(4)
  is_abelian_subgroup(G,H)
#Returns False
#7bd
  H = [Perm((1,2)),Perm(),Perm((3,4)), Perm((1,2),(3,4))]
  G = SymmetricGroup(5)
  is_abelian_subgroup(G,H)
#Returns True

def generate(G,X):
  H = []
  x = X
  H.append(X)
  while not (x == G.identity()):
    x = x*X
    H.append(x)
  return H

solutionTwo()
solutionThree()
solutionSix()
solutionSevenB()
solutionSevenC()
#print(generate(SymmetricGroup(4),Perm((1,2,3,4))))
G = SymmetricGroup(4)
i = 0
#for g in G:
 # print(generate(G,g))
