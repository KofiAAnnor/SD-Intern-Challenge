# Introduction
    This README outlines key aspects and functionalities of the Intern Application API
    
# Database Specification
The database used within this application is a sqlite database with a single table named "Interns".
The rows for the "Interns" table are as follows
* "id" = Integer & primary_key & auto-generated
* "first_name" = String of length 80 & not null
* "last_name" = String of length 80 & not null
* "position" = String of length 80 & not null
* "school" = String of length 80 & not null
* "degree_program" = String of length 80 & not null
* "time" = DateTime & not null & auto-generated

# How to run application
The application can be run using the following commands
````
$ docker build -t api .
````
This builds a docker image named "api" as well as runs the unit tests
````
$ docker run -p 5000:5000 api
````
This spins up the docker container and server with the following URL http://0.0.0.0:5000/

# Making API Requests
To make a GET request (which returns all entered applications in JSON format) either navigate to this URL 
http://0.0.0.0:5000/ on a browser or use the following command on a 
linux terminal.
````
$ curl -d "Content-Type: application/json" -X GET http://0.0.0.0:5000/
````
To make a POST request (which enters an application(s) into the database) use the following command as an example on a 
linux terminal. 
````
$ curl -d '[
{"first_name":"Jared", "last_name":"Voss", "position": "Software Development Intern", "school":"UMCP", 
"degree_program":"Computer Science"}
]' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/
````
This will add the following intern application data into the database:
* "first_name": "Jared"
* "last_name": "Voss"
* "position": "Software Development Intern"
* "school": "UMCP", 
* "degree_program": "Computer Science" 
* "id" and "timestamp" will be automatically generated

To add multiple entries at once simply append further entries to the JSON input as such:
````
$ curl -d '[
{"first_name":"Jared", "last_name":"Voss", "position": "Software Development Intern", "school":"UMCP", 
"degree_program":"Computer Science"},
{"first_name":"sarah", "last_name":"walker", "position": "Software Development 
Intern", "school":"UMCP", "degree_program":"Computer Science"}
]' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/
````