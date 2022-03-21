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

# Tech Talk 2 - Console Programming Part A

## Learning: Presentation, Organization, and Management
As development continues, we need to consider cleaning up our repository, runtime, and deployment on Replit.  Here are considerations required before turning in your next assignment.
1. Time box method in README for looking at week-over-week accomplishments is a standard.  README can cover time box and purpose.
    * Week 0 Menu, Tree, Matrix, Swap
    * Week 1 Car List, Fibonacci
    * Week 2 Fibonacci Class, Math Class, Adventure File
2. Directory structure for finding code.  Since these are short subjects, you could organize by when you implemented them or it would be equally fine to organize by subject.
```
src\
   week0\
   week1\
   week2\
```
3. Organizing your menu.  Often how you present things does not match your internal organization.  Our weekly lessons may not match how we think about the elements.  
Note: Data and Math should be familiar.  Adventure has been added to show that a menu could be used in different fashion, as a Menu is simply a question (title) and a response (options).
```
=========================
Main Menu
=========================
0 -> Exit
1 -> Data
2 -> Math
3 -> Adventure
Type your choice> 
```

4. Verify your code runs on both IntelliJ and Replit.

## Learning: OOP and Creating a Class   
Object-oriented programming (OOP) is a programming paradigm that allows you to package together data states and functionality to modify those data states, while keeping the details hidden away. As a result, code with OOP design is flexible and abstracts complexity.  Creating a "class" in Python starts OOP.

### Python Class Definition  
Python is an object oriented programming language. Most of the language elements (constructs) we use in Python are objects, this includes its  **variables(attributes) and functions(methods).**    A Class is like a "blueprint" or "template" for constructing(instantiating) objects.   The "class" is used to construct the "object" in OOP. 

###  __init__() definition - the Object constructor
All Python classes have a function called __init__(), which is always executed when the class is called and the resulting object is constructed.  Below is an __init__() function to assign initial values for the Fibonacci sequence [0, 1]. 
```python
class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]
```

### __call__() definition - the default Object method
The __call__ function/method is a special to Python, when implemented inside a class, this gives its object the ability to behave like a regular Python function. 

Definition of __call__.  The __call__ method  is defined inside the Python class.  The method allows the construct object to invoke this method using a "object_name()" notation. The "def __call__(self, n):" has keyword "self" in the parameter list, this means that the object itself is part of this functions properties.  The parameter "n" means it is expecting a value to be passed, in Fibonacci case it is the nth number in the Fibonacci sequence.

```python
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.fiboSeq.append(fib_number)
        return self.fiboSeq[n]
``` 

### Learning: Constructing and Using and Object
Step one is to make an object/instance of the class Fibonacci, fibo_of is that object.  The second step is to use "fibo_of" like a function and passing it the parameter 5.  This will perform the __call__ method and since it run inside the print it's return value will be output: 3.  This is from the fibonacci sequence (0,1,1,2,3).
```python
fibo_of = Fibonacci() # object instantiation and run __init__ method
print(fibo_of(5)) # object running __call__ method
```

## Vision: 2nd OOP example  
Classes can have a lot more data and contain many methods. Methods in objects are functions that belong to the object.  Illustrated is an example of "class Users" with the database table attributes and the CRUD methods.  Notice this contains the __init__ method which sets up the attributes for a row in the table.  The methods provide the ability to perform CRUD actions on a table row.

The "class Users(db.Model):" shows the advanced usage of inheritance.  This is adding an external library functionality to the instantiated object created from Users.  When constructing an object, this class expects many parameters, "def __init__(self, name, email, password, phone):".  Throughout the class you will see the usage of the "self" keyword ("userID": self.userID), this is always referring to data within the object.

```
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, password="", phone=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(password) > 0:
            self.password = password
        if len(phone) > 0:
            self.phone = phone
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


    #Example: Tester data for table
    u1 = Users(name='Thomas Edison', email='tedison@example.com', password='123toby', phone="1111111111")
    u2 = Users(name='Nicholas Tesla', email='ntesla@example.com', password='123niko', phone="1111112222")
    u1, u2 are objects of the class Users and methods Create, Read, Update, Delete methods are available to both the objects u1 and u2

```

## Coding: Challenges
* Hack 1: Organize files, directories and menus for the first 3 weeks.  Use Teacher implementation as an example.  Make sure that work is organized so it is easy to illustrate this weeks assignments.
* Hack 2: Write Factorial function using classes, providing implementation of __call__.  
    * Print final number
    * Print sequence
* Hack 3: Select your own Math function.  Write it in Imperative and OOP form.  Some Math functions have been provided.  Think about inputs and outputs to present to Teacher.  It is preferred to have Test data, not input to illustrate code.
* Hack 4: Write Palindrome function using classes, providing implementation of __call__.  
    * Evaluate if it is a palindrome
    * Evaluate complex algorithms eliminating spaces, case and special characters. "A man, a plan, a canal -- Panama!"
    * Use Test data, not input
    * Illustrate failure

