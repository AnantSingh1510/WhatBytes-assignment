# WhatBytes: Backend Developer Intern Assignment

## Notes
### Styling
1. As mentioned in the assignment document, styling wasn't a criteria for the evaluation, therefore I have used BootStrap to make the development process a bit fast.

### Others
1. As mentioned in the document, I have used Django's built in authentication system and used Django forms as much as possible.


## Installation

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/AnantSingh1510/WhatBytes-assignment.git
cd WhatBytes-assignment/assignment
```

### 2.  Create and Activate a Virtual Environment
create and activate a virtual environment using the following commands:
```bash
python -m venv venv
venv\Scripts\activate
```

### 5. Apply Migrations
Before running the project, apply the database migrations:

```bash
python manage.py migrate
```

### 7. Run the Development Server
Now, you can start the development server:

``` bash
python manage.py runserver
```
Open your web browser and go to http://127.0.0.1:8000/ to see the application.
