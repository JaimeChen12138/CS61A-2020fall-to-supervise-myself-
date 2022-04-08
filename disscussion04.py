Questions 1.1
You want to go up a flight of stairs that has n steps. You can either take 1
or 2 steps each time. How many different ways can you go up this flight of
stairs? Write a function count_stair_ways that solves this problem. Assume n is positive.
Before we start, what’s the base case for this question? What is the simplest
input?
What do count_stair_ways(n - 1) and count_stair_ways(n - 2) represent?
Fill in the code for count stair ways:

#把树状图画出来
def count_stair_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

# another base case can write as follows
   if n == 1:
       return 1
   elif n == 2:
       return 2
   ......


#*******************************************
1.2 Tutorial: Consider a special version of the count_stairways problem,
where instead of taking 1 or 2 steps, we are able to take up to and including
k steps at a time.
Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.

#同上画树状图就很简单，所以叫 tree recursion
def count_k(n, k):
"""
>>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
4
>>> count_k(4, 4)
8
>>> count_k(10, 3)
274
>>> count_k(300, 1) # Only one step at a time
1
"""
if n == 0:
    return 1
elif n < 0:
    return 0
else:
    i = 1
    total = 0
    while i <= k:
        total += count_k(n-i,k)
        i += 1
    return total

# can not use partition like solution before because for example this problem count (3,3) 2+1,1+2 as two times,but partition just count one time.
#************************************************************


Questions
2.1 What would Python display?
>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])
1 3

>>> len(a)
5

>>> 2 in a
False

>>> 4 in a
True

>>> a[3][0]
2


2.2 Tutorial: Write a function that takes a list s and returns a new list
that keeps only the even-indexed elements of s and multiplies them by their
corresponding index.

def even_weighted(s):
""">>> x = [1, 2, 3, 4, 5, 6]
>>> even_weighted(x)
[0, 6, 20]
"""

  return [s[index] * index for index in range(0,len(s),2)]




2.3 Write a function that takes in a list and returns the maximum product that
can be formed using nonconsecutive elements of the list. The input list will
contain only numbers greater than or equal to 1.

def max_product(s):
"""Return the maximum product that can be formed using non-consecutive
elements of s.
>>> max_product([10,3,1,9,2]) # 10 * 9
90
>>> max_product([5,10,5,10,5]) # 5 * 5 * 5
125
>>> max_product([])
1
"""
    if s == []:
        return 1
    else:
        with_digit = s[0] * max_product(s[2:])
        without_digit = max_product(s[1:])
        return max(with_digit,without_digit)
