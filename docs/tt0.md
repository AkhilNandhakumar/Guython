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

# Tech Talk 0 - Python Menu, Replit, GitHub

## Python Menu

```
"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Listy' )
    print('4 -- Exit' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')

# menu option 3
def listy():
    print('You chose \'3 - Listy\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            # Exit menu    
            elif option == 4:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()
```

### Exception Handling - Python Try-Except-Finally
When an error occurs, or "**except**"ion as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:

![Exception](https://github.com/nighthawkcoders/nighthawk_csp/raw/master/static/assets/Py-try-finally.jpg)

## Python Menu

Creating a Python menu with data structures and try/except statements - the lazy programmer way

```
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import loopy
import mathpy
import funcy
import patterns


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Stringy", "stringy.py"],
    ["Listy", "listy.py"],
    ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", mathpy.factors],
    ["GCD", mathpy.gcd],
    ["LCM", mathpy.lcm],
    ["Primes", mathpy.primes],
]

patterns_sub_menu = [
    ["Patterns", "patterns.py"],
    ["PreFuncy", "prefuncy.py"],
    ["Funcy", funcy.ship],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```

**Note**: All your code should be on replit for easy view. You must have version control connected and have history showing individual work. This is MANDATORY.

### Learning Considerations

Many of the following concepts should be in your final Create Task

You will need to checkout on Python on several concepts like

A. Variable assignments
B. Loops and zero based counting
C. Dictionaries, Lists, Two-dimensional (2D) lists(arrays)
D. Python Classes
More...

## Menu Challenge

1. Build your own menu and sub-menu
2. Add swap and keypad from Tri 2 Week 10, to your project and menu.
3. For additional challenge and review, build a Christmas tree with stars or a pattern of your choice

<img src="https://user-images.githubusercontent.com/88572244/156895395-6bbf72be-605f-4bca-a376-b9ee985b5786.png" alt="tree" height="300" width="200"/>

4. Add two items below to get ready for animations and interacting with terminal codes
- Here's an example of a ship pattern. Implement it in your project and make your own pattern following the example.

```
#prefuncy.py
import time
import os

Color34 = "\u001b[34m"
Color37 = "\u001b[37m"


# As you can see, its not very optimal 
def ship1():
    print("    |\ ")
    print("    |/ ")
    print("\__ |__/ ")
    print(" \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship2():
    print("      |\ ")
    print("      |/ ")
    print("  \__ |__/ ")
    print("   \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship3():
    print("        |\ ")
    print("        |/ ")
    print("    \__ |__/ ")
    print("     \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship4():
    print("          |\ ")
    print("          |/ ")
    print("      \__ |__/ ")
    print("       \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship5():
    print("            |\ ")
    print("            |/ ")
    print("        \__ |__/ ")
    print("         \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship6():
    print("              |\ ")
    print("              |/ ")
    print("          \__ |__/ ")
    print("           \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship7():
    print("                |\ ")
    print("                |/ ")
    print("            \__ |__/ ")
    print("             \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship8():
    print("                  |\ ")
    print("                  |/ ")
    print("              \__ |__/ ")
    print("               \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship9():
    print("                    |\ ")
    print("                    |/ ")
    print("                \__ |__/ ")
    print("                 \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship10():
    print("                      |\ ")
    print("                      |/ ")
    print("                  \__ |__/ ")
    print("                   \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship11():
    print("                        |\ ")
    print("                        |/ ")
    print("                    \__ |__/ ")
    print("                     \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship12():
    print("                          |\ ")
    print("                          |/ ")
    print("                      \__ |__/ ")
    print("                       \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship13():
    print("                            |\ ")
    print("                            |/ ")
    print("                        \__ |__/ ")
    print("                         \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship14():
    print("                              |\ ")
    print("                              |/ ")
    print("                          \__ |__/ ")
    print("                           \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship15():
    print("                                |\ ")
    print("                                |/ ")
    print("                            \__ |__/ ")
    print("                             \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship16():
    print("                                  |\ ")
    print("                                  |/ ")
    print("                              \__ |__/ ")
    print("                               \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship17():
    print("                                    |\ ")
    print("                                    |/ ")
    print("                                \__ |__/ ")
    print("                                 \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship18():
    print("                                      |\ ")
    print("                                      |/ ")
    print("                                  \__ |__/ ")
    print("                                   \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship19():
    print("                                        |\ ")
    print("                                        |/ ")
    print("                                    \__ |__/ ")
    print("                                     \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship20():
    print("                                          |\ ")
    print("                                          |/ ")
    print("                                      \__ |__/ ")
    print("                                       \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


os.system("cls")
time.sleep(.1)
ship1()
time.sleep(.5)
os.system("cls")
ship2()
time.sleep(.5)
os.system("cls")
ship3()
time.sleep(.5)
os.system("cls")
ship4()
time.sleep(.5)
os.system("cls")
ship5()
time.sleep(.5)
os.system("cls")
ship6()
time.sleep(.5)
os.system("cls")
ship7()
time.sleep(.5)
os.system("cls")
ship8()
time.sleep(.5)
os.system("cls")
ship9()
time.sleep(.5)
os.system("cls")
ship10()
time.sleep(.5)
os.system("cls")
ship11()
time.sleep(.5)
os.system("cls")
ship12()
time.sleep(.5)
os.system("cls")
ship13()
time.sleep(.5)
os.system("cls")
ship14()
time.sleep(.5)
os.system("cls")
ship15()
time.sleep(.5)
os.system("cls")
ship16()
time.sleep(.5)
os.system("cls")
ship17()
time.sleep(.5)
os.system("cls")
ship18()
time.sleep(.5)
os.system("cls")
ship19()
time.sleep(.5)
os.system("cls")
ship20()
time.sleep(.5)
os.system("cls")
print("or so you thought...")
time.sleep(.5)
os.system("cls")
```

