# Verbal Autopsy System

## Description

A Verbal Autopsy System is a digital form that is used to gather information of a deceased person, this information is retrieved through an interview with a witness at the time of the deceased person's death. The records gathered are then used by health professionals to conclude on the possible cause of death.

## How to run locally

1. Clone the repository from this github repository, either by downloading the zip file from the green code button, or running this command in your terminal:

    ` git clone https://github.com/GraceMonde/va-system.git ` and ` cd va-system `

2. Create a virtual environment using this command:

    ` python3 -m venv venv `

3. Activate the virtual environment using this command:

    ` source venv/bin/activate `

    You will be able to see '(venv)' at the beginning of your next terminal line

4. Install these dependencies

    ` pip install -r requirements.txt `

5. Run database migrations to create the tables needed:

    ` python manage.py migrate `

6. Start the development server using this command:

    ` python manage.py runserver `

    then open the url link in your web browser, it should be something like this ` http://127.0.0.1:8000 `


## Live deployed URL

 `  `

## What I learned

- I learned how to separate concerns using the MVT model which enabled me to define my database structure in models, create views where logic and requests are processed and templates where the structure of information is defined.
- I learned how to use a Linux environment for building and running an app, using the terminal, virtual environments, and running a live dev server.
- I learned that migrations keep a history of every database change and it allows anyone else to recreate the exact same database structure from scratch.

## Grace Kabwe