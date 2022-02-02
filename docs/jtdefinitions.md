{% include navigation.html %}

This page serves as a guide to the vocabulary we have learned in Computer Science: Principles. Some terms are shown through examples, while others are defined in simple terms.

## Table of Contents:
1. [Binary / Hexadecimal](#binary--hexadecimal)
2. [Bit](#bit)
3. [Nibble / Byte](#nibble--byte)
4. [Lossless/Lossy Compression](#losslesslossy-compression)
5. [Metadata](#metadata)
6. [Computer Network](#computer-network)
7. [Parallel/Distributed computing](#paralleldistributed-computing)
8. [Protocol](#protocol)
9. [TCP/IP](#tcpip)
10. [HTTP](#http)
11. [GET / POST](#get--post)
12. [MVC](#mvc)
13. [CRUD](#crud)
14. [FETCH](#fetch)
15. [Async](#async-operations)
16. [REST](#rest)
17. [API/Library](#apilibrary)
18. [OOP](#oop)
19. [Class](#class)
20. [Attribute](#attribute)
21. [Method](#method)
22. [Object](#object)
23. [Procedures/Functions](#proceduresfunctions)
24. [Data/procedural Abstraction](#dataprocedural-abstraction)
25. [Sort](#sort)
26. [Search-Linear/Binary](#search-linearbinary)
27. [Blueprints](#blueprints)

### Binary / Hexadecimal
[Binary Lab](https://5hackers.tk/lab4)

Binary: base 2 number system (0 and 1), used by computers to store information

Hexadecimal: base 16 number system, uses 0-9 and A-F
### Bit
[Binary Math with Conversions](https://5hackers.tk/hackathontt3)

a single unit of information in a computer (Binary Digit)
### Nibble / Byte
A Nibble is 4 bits, while a Byte is 8 bits
### Lossless/Lossy Compression
Lossless Compression: data compression algorithm that allows original data to be perfectly reconstructed from compressed data. Examples include PNGs, ZIPs, executable programs.

Lossy Compression: data compression algorithm where some amount of data is lost, attempts to eliminate redundant information. Examples include JPEGs, videos, audio.
### Metadata
[RGB Lab](https://5hackers.tk/lab3)

data that describes other data
### Computer Network
Computers connected together to share information and resources. Use communication protocols to to transmit information through physical or wireless methods. Nodes in a computer network can include personal computers, servers, or other hosts.
### Parallel/Distributed computing
Parallel Computing: breaking down larger problems into simpler parts which can be executed at the same time by multiple computers / processors which communicate with each other through shared memory. When combined, these parts make up a completed algorith, usually with a faster run time compared to traditional computing methods. 

Distributed computing: Similarl to parallel computing, main difference is method of communication between devices: distributed computing uses communcation networks, with each device using its own memory.
### Protocol
set of rules controlling the exchange of data between devices. Protocols allows computers with different software and hardware to communicate with each other, such as in distributed computing or computer networks.
### TCP/IP
Transmission Control Protocol: used with IP, ensures reliable data delivery, puts IP packets in sequence and checks for errors in transmission

Internet Protocol: main delivery system for information on the internet, delivers network packets from one host to another based on their IP Addresses.
### HTTP
Hypertext Transfer Protocol: used to connect to Web servers on the Internet or local networks, puts information into a format that programs such as web browsers can use directly. 
### GET / POST
[Greet Function](https://5hackers.tk/lab1)

GET: request method that sends all form data to the server

POST: request method used for sensitive information
### MVC
Model-View-Controller: software design pattern commonly used for developing user interfaces that divide the related program logic into three interconnected elements (Model, View, Controller). 
- Model is the central component, responsible for managing data, recieves input from controller
- View is the representation of information, renders model in a particular format
- Controller responds to inputs and converts it into commands for model or view

### CRUD
[CRUD Operations](https://5hackers.tk/crud)

Create, Read, Update, Delete (important functions for a storage application) 
### FETCH
fetching data from one source to another (disk to memory buffer, memory to CPU). In JavaScript, the fetch method is used to get resources from a network, such as in APIs.
### Async Operations
[Async CRUD Operations](https://5hackers.tk/crud_api)

tasks performed without dependency on each other
### REST
Representational State Transfer (provides standards between computer systems on the web, easier to communicate)
### API/Library
[API Collection](https://5hackers.tk/api_collection)

Applications Program Interface (A library of classes for use in other programs. Provides standard interfaces that hide the details of implementation)

Library: a collection of resources that are referenced and used by computer programs
### OOP
Object Oriented Programming: organizes software design around objects interacting with each other, mainly in large or complex programs such as programs for manufacturing, design, or mobile applications. Classes can reuse code from other classes which reduces development time and produces better data analysis.

The main selling point of object oriented programming is its modular coding process in which data and methods can be simplified and abstracted into API's which are easily stacked and combined to make complex applications fast and is believed to help with code rot. However the argument of whether OOP is better than procedural is still ongoing.

### Class
program/code template for creating objects

A class is one of the most basic and most powerful tools in complex code. Classes allow you to bundle code into a resusable and malleable bits. Classes appear constantly in web programming so programmers can have a place where aethestic can be easily changed globally and modules in the site can be easily unified.

### Attribute

An attribute in programming often refers to a piece of data inside an object. Attributes may be constants or variables. Attributes are key to OOP as they allow the unification of functions and data into one place.

### Method
Functions or procedures inside a class that can be accessed through objects.

Methods allow for the alteration of internal or external variables in a clean abstracted way.

Accesing an object may yield a couple methods which may actually be quite deep and complex, however their method is abstracted so it can be more easily reused and repurposed.

### Object
Objects can be anything: functions, methods, variables, data structures, etc.

Objects in object oriented programming allow programmers to create API's or modules which are supposed to work both independently and together to form complex maintainable super structures. Objects in procedural programming lack the ability to have both data and method combined in the same area.

### Procedures/Functions
[Mini Quizzes](https://5hackers.tk/math)

Procedure: block of code that accomplishes a certain task, executes commands

Function: similar to a procedure, but also returns a result
### Data/procedural Abstraction
Data: Information translated into a form that is more efficient for processing or moving

Procedural Abstraction: Writing code sections (procedures) that have variable parameters, allowing them to be used in multiple situations
### Sort
[Search Bar](https://5hackers.tk/crud/search)

Putting elements in a list in a specific order

This is highly useful when a function or method needs to methodically access and alter data in a place where order of input matters.

### Search-Linear/Binary
Linear Search: sequentially checking elements in a list, rarely used because of slowness

Binary Search: searches an array by dividing sections in half until object is found, fast and commonly used
### Blueprints
an alternate method of creating app routes / a plan or outline used for software development, either documentation for coders or code-generating tools for machines
