# FLASKCONNEXION

This is a template blending [Flask](https://github.com/pallets/flask) and [Zalando connexion](https://github.com/zalando/connexion).

It provides a clean way of development for API based project with associated Web UI.

## How to tweak?

Prerequisite: a docker enabled machine

```
git clone ...
cd FLASKCONNEXION
create a .env file there (see thereafter)
docker-compose up -d
```

ctop is nice to check docker containers [bcicen/ctop](https://github.com/bcicen/ctop)

### When up and runing

- [home page](http://localhost:8000)   http://localhost:8000 
- [swagger test pages](http://localhost:8000/v1/ui)   http://localhost:8000/v1/ui
- [the user API](http://localhost:8000/v1/user) => give an empty result as the database is empty... http://localhost:8000/v1/user

### set some user using ctop

entering inside the runing container with ctop
```
sqlite3 framework.db
>.schema
...
>INSERT INTO user (email, firstname, lastname, role) VALUES ("gbrault@seadev.org","Gilbert","Brault","admin")
```

### making some changes

- Change the framework_api.yml file to add new API path
   - each tile you add a new API path
   - add the corresponding implementation function in api.py specified with the operationId tag
- To add a new Web UI page
   - add a new template in the templates folder
   - add a new processing backend in the pages folder
   - add this page in the app.py entrypoint

## .env file

```
MAIL_USERNAME = your gmail address
MAIL_PASSWORD = your gmail password
DATABASE_URL = sqlite:////framework/framework.db
VIRTUAL_PORT=5000
API_FILE=framework_api.yml
SQLALCHEMY_TRACK_MODIFICATIONS=false
```

## Folder layout

```
                                        flaskconnexion
docker orchestration file               ├── docker-compose.yml
container definition file               ├── Dockerfile
visual studio code project              ├── flaskconnexion.code-workspace
                                        ├── framework
definition of the API functions         │   ├── api.py
framework entry point                   │   ├── app.py
creating the database                   │   ├── database.py
Open API 3.0 Schema definition          │   ├── framework_api.yml
                                        │   ├── __init__.py
Website UI                              │   ├── pages
                                        │   │   └── home.py
Front End files                         │   ├── static
                                        │   │   ├── css
                                        │   │   │   ├── all.css
                                        │   │   │   ├── bootstrap.css
                                        │   │   │   ├── bootstrap.css.map
                                        │   │   │   ├── bootstrap-grid.css
                                        │   │   │   ├── bootstrap-grid.css.map
                                        │   │   │   ├── bootstrap-grid.min.css
                                        │   │   │   ├── bootstrap-grid.min.css.map
                                        │   │   │   ├── bootstrap.min.css
                                        │   │   │   ├── bootstrap.min.css.map
                                        │   │   │   ├── bootstrap-reboot.css
                                        │   │   │   ├── bootstrap-reboot.css.map
                                        │   │   │   ├── bootstrap-reboot.min.css
                                        │   │   │   ├── bootstrap-reboot.min.css.map
                                        │   │   │   ├── login_style.css
                                        │   │   │   └── scrolling-nav.css
                                        │   │   ├── images
                                        │   │   │   └── favicon.png
                                        │   │   ├── js
                                        │   │   │   ├── bootstrap.bundle.js
                                        │   │   │   ├── bootstrap.bundle.js.map
                                        │   │   │   ├── bootstrap.bundle.min.js
                                        │   │   │   ├── bootstrap.bundle.min.js.map
                                        │   │   │   ├── bootstrap.js
                                        │   │   │   ├── bootstrap.js.map
                                        │   │   │   ├── bootstrap.min.js
                                        │   │   │   ├── bootstrap.min.js.map
                                        │   │   │   ├── jquery-3.4.1.slim.min.js
                                        │   │   │   ├── popper.min.js
                                        │   │   │   └── popper.min.js.map
                                        │   │   └── webfonts
                                        │   │       ├── fa-brands-400.svg
                                        │   │       ├── fa-brands-400.woff
                                        │   │       ├── fa-brands-400.woff2
                                        │   │       ├── fa-solid-900.woff
                                        │   │       └── fa-solid-900.woff2
Jinja2 Page templates                   │   └── templates
                                        │       ├── base.html
                                        │       └── home.html
                                        ├── README.md
Dependencies                            └── requirements.txt
```
