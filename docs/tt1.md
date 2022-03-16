{% include navigation.html %}

# Tech Talks - Trimester 3

<table>
    <tr>
        <td><a href="tt0">Tech Talk 0</a></td>
        <td><a href="tt1">Tech Talk 1</a></td>
        <td><a href="tt2">Tech Talk 2</a></td>
        <td><a href="tt3">Tech Talk 3</a></td>
    </tr>
</table>
<hr>

# Tech Talk 1 - Data Structures

## Python [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), Iteration, Recursion

Python Lists Vs Dictionaries (classes)  
List is a collection of index values pairs as that of array in JS.	
Dictionary is a hashed structure of key and value pairs.  

Space-Time Trade-Off  
It is more efficient to use a dictionary for lookup 
of elements because it takes less time to traverse in the dictionary than a list.
It takes more time for fetching a single element in a list than that of a dictionary because dictionary uses hash table for implementing the arrangement.
 
The list() Constructor:  
thislist = ["Jake", "Jim", "Drew"]  
It is also possible to use the list() constructor when creating a new list.  
thislist = list(("Jake", "Jim", "Drew")) # note the double round-brackets  

Dictionaries:  
The values in dictionary items can be of any data type:
String, int, boolean, and list data types:

## List Elements with embedded Dictionary
Very similar to all the JSON work we have done 

```python   

# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Mortensen",  
               "DOB": "October 21",  
               "Residence": "San Diego",  
               "Email": "jmortensen@powayusd.com",  
               "Owns_Cars":["2015 Fusion","2011 Ranger","2003 Excursion","1997 F-350", "1969 Cadillac"]  
              })  

InfoDb.append({  
               "FirstName": "Sunny",  
               "LastName": "Naidu",  
               "DOB": "August 2",  
               "Residence": "San Diego",  
               "Email": "snaidu@powayusd.com",  
               "Owns_Cars":["A","B","C"]  
              })  
```

## Accessing and Printing Data

How do we print the second car from the Owns_Cars list  
x = InfoDb[0]["Owns_Cars"][1] # Gives "2011 Ranger"

There is also a method called get() on the Dictionary(InfoDb[0]) that will give you the same result:  
x = InfoDb[0].get("Owns_Cars")[1]

Here is a function designed to print content from InfoDB
```python
# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
```


## Iteration:  
### Python Loops:    
Python has two primitive loop commands:  
* for loops, while loops  

### For loops:     
Python For Loops  
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).  
This is less like the for keyword in other programming languages, and **works more like an iterator method** as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.  
The range() Function:  
To **loop through a set of code a specified number of times**, we can use the range() function,  
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.  
     
```python
# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
```
### While Loop:  
With the while loop we can execute a set of statements as long as a condition is true or false.  

```python
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
```

## Recursion:  
Recursion means a defined function can call itself.  
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. There must be a **termination/exit condition** that allows the function to exit without calling itself. This condition allows the recursion to stop - that is, without it the function would call itself over and over again, resulting in an error.
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

```python
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)
```

## Tester:  

When building terminal or backend code you should always build a tester

```python
# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
``` 


## Challenges:
* See hack 1 above, InfoDB lists
* See hack 2 above, InfoDB loops
* See hack 3 above, Fibonacci
