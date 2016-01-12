# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> In Python, lists and tuples fairly identical. The big difference is that lists are mutable while tuples are mutable. Tuples are used as keys in dictionaries because they are immutable and they can be hashed by their contents without worries about modications. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in terms of creating list of elements/variables/items. You can create a list of different data types in lists and sets. They are different in many ways as well. Lists are sequence type and sortable while sets store unordered, non-duplicate items. Every element is unique in a set. You can also use mathematical set operations on sets, such as intersection (&), union (|), and symmetric difference (^).

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda expressions are small anonymous functions. It's an expression used to create functions. You can think of them as nested functions. You can use these unnamed functions in other functions to perform simple tasks. They are known as one-statement, throw-away functions.

```python
tups = [(1, 3, -2), (3, 2, 1), (-1, 0, 4), (0, -1, 3), (-2, 6, -5)]

sorted(tups, key=lambda tup: tup[1])
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide concise way to create lists. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

```python
## examples of list comprehension
list1 = [y for y in range(10)]
list2 = [z**2 for z in range(10) if z > 4]

## examples of map function
map1 = map(lambda x: x, range(10))
map2 = map(lambda x: x**2, range(10))[5:]

## examples of filter function
filter1 = filter(lambda x: x >= 0, map1)
filter2 = map(lambda y: y**2, filter(lambda x: x>4, range(10)))

## example of set comprehension
set1 = {3*x for x in range(10) if x > 5}

## example of dictionary comprehension
dic1 = {n: n**2 for n in range(10)}

```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





