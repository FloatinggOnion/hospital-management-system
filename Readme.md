## Tech Amaka Hospital Management System
This is a simple hospital management web application built using Django and GraphQL

#### Installation and Setup
- Clone this repo
- cd into the root directory, and then enter this command:
```
pipenv install
```
- This installs the dependencies for the Django backend
- For the frontend, run `npm install`

#### Launching the app
- For the backend, run </br>
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Endpoints
`/` - Landing page of the website
`/hospitals` - View list of hospitals in database
`/graphql` - Access GraphQL UI for database interactions

- For the frontend, run </br>
```npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch```

#### Tools and Dependencies
- Django for the backend logic
- TailwindCSS and Flowbite for the frontend
- GraphQL for data modelling and database interaction