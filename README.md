
# Number 1 Hackers
## [GitHub Repository](https://github.com/JakubPonulak/flask_portfolio)
## [Scrum Board](https://github.com/JakubPonulak/flask_portfolio/projects/1)
## [Team Journal](https://docs.google.com/presentation/d/1TdBNp9JPyNSbcwWtPAHtlgM1XWtLP30hLIq9HZhdGtY/edit#slide=id.p)
### Anika
GitHub ID: anika1sharma1

### Jakub
GitHub ID: JakubPonulak
### Tristan
GitHub ID: Sinergixxx
### Vunsh
GitHub ID: vunsh
### Sprint 1,2 (code tangibles)
1. Greet integration in "about me" pages: [Anika](templates/about%20us/anika.html), [Jakub](templates/about%20us/jakub.html), [Tristan](templates/about%20us/tristan.html), [Vunsh](templates/about%20us/vunsh.html)
2. [Dropdown code](templates/layouts/navbar.html)
3. [Greet Integration in mini lab](templates/our%20work/lab1.html)
4. [Video Journal 0 Integration](templates/our%20work/lab2.html) 
5. README.md updates
6. "About Me" page completion [Anika](templates/about%20us/anika.html), [Jakub](templates/about%20us/jakub.html), [Tristan](templates/about%20us/tristan.html), [Vunsh](templates/about%20us/vunsh.html) 
### Sprint 3,4 (code tangibles)
1. Website theme, fonts/colors : [base.html](templates/layouts/base.html), [navbar.html](templates/layouts/navbar.html) 
2. [Our Work dropdown](templates/layouts/navbar.html) creation + content
3. Tech Talk 3: [Hack-a-thon](templates/our%20work/hackathontt3.html)
4. "About Us" pages improvement: [Anika](templates/about%20us/anika.html), [Jakub](templates/about%20us/jakub.html), [Tristan](templates/about%20us/tristan.html), [Vunsh](templates/about%20us/vunsh.html)
5. [Home page improvement](templates/main_page.html)
### Scores (9/3/21)
Team: 4/4   
Jakub: 3.5/4  
Anika: 3.5/4  
Tristan: 3.5/4  
Vunsh: 3.5/4
### Idea
Personalized starter website
### Visual thoughts
#### Organize with Bootstrap menu 
Utilize boostrap menu for navbar
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
Make use of VANTA templates
#### Show project specific links (hrefs) per page
This includes videos and mini labs that have been completed
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for root, Jakub, Tristan, Vunsh, and Anika
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, base.html, etc.. are called upon using the flask library in main.py
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
#### Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
