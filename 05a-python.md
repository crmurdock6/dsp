# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they are sequences of values that can be any type. Only tuples can work as keys in dictionaries as they are immutable while lists are mutable and can lead to unexpected behavior.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both sequences of values with some key differences being that sets are unordered, can't contain duplicates, and can only contain hashable items. An example of a list is `a = ['string', ['list', 'within', 'list'], 1]` showing that any type can be used as a value. An example of a set is `b = {5, 'string', ('tuple', 'of', 'strings')}`

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` operator is used to create small, anonymous functions. They are throw-away functions and are therefore only needed where they are created.Lambda functions are often used in combindation with `filter()`, `map()`, and `reduce()`. Two examples are as follows:

```
square = lambda x: x ** 2
# square(2) will return 2 ** 2

vehicle_tuples = [
	('pontiac', 'firebird', 'red', 2002),
	('toyota', 'camry', 'blue', 2014),
	('ford', 'fiesta', 'white', 2008)
]

# sort by year
print(sorted(vehicle_tuples, key=lambda vehicle: vehicle[3]))
``` 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a concise way to make lists and include brackets containing an expression followed by a `for` clause and zero or more `if` or `for` clauses. A common application for list comprehensions is to make a new list where an operation is applies to each element. An example with the corresponding `map` and `filter` equivalents is shown below:

```
names = ['bob', 'kevin', 'mary', 'brian']
b_names = [x for x in names if x.startswith('b')]
b_names = list(map(lambda x: x.startswith('b'), names))
b_names = list(filter(lambda x: x.startswith('b'), names))
```

Examples of set demonstrations and dictionary comprehensions are below:

```
# set comprehension
even_numbers = {x for x in range(1, 10) if x % 2 == 0}

# dictionary comprehension
squares = {x: x ** 2 for x in range(10)} 
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
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

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





