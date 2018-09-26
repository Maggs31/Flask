a)Clone the project

b) cd backend (from the terminal)

c) To install dependencies: make bootstrap (from the terminal)

d) sudo service mongod start (run mongodb)

d) To run the application: make prod  (from the terminal)

e) To view application page:
 
http://localhost:8090/

The app folder inside backend contains the application logic. Models,Views,Static,Templates has the db schema, python logic, html template logic and css files respectively.
Views contains the two blueprints used in the code.

Structure

Flask(git repository)
|-backend
|---make file (install dependencies by typing make bootstrap)
|---run application (type make prod)
|---app
|-------models (contains Mongodb schema)
|-------views (contains python logic for CRUD )
|-------static (contains style.css for the project )
|-------templates (contains html files for Projects, UserList Page, CreateUser page, updateuser and deleteuser page) 
|-------config contains flask configuration
|-------extensions loads extensions required
|-------factory (registers all handlers)


