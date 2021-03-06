# [CO2e Tracker](https://co2e-tracker.herokuapp.com/)

## About
As Capstone 1 of Springboard's Software Engineering Career Track, [CO2e Tracker](https://co2e-tracker.herokuapp.com/) is an database-driven app that allows users to record their activities along with corresponding CO2 emissions.
Using Climatiq's API to calculate CO2e, four types of activities are available to be recorded: Flights, driving, and purchasing of new clothing or plastic bottles. The emission factor for purchasing includes the cradle-to-shelf product lifecycle.

## User Flow
After registration, a user may add an activity via a form designated to one of the four activities available. Quantity of expenditure, date, and CO2e (measured in kg) appears in their history table. Users may edit and delete activity data. Several groups of history stats appear on the 'stats' page, including total CO2e kg based on current year, month, and activity type.

## Tools Used
- [Climatiq REST API](https://www.climatiq.io/)
- Flask
- Flask SQLAlchemy
- WTForms
- Axios
- Jinja
- PostgreSQL
- jQuery
- Vanilla JS
- Native CSS
- Python

## Run Locally

`python3 -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  
`touch ".env"`  
  
Add the following variables into your .env file:
`SECRET_KEY`  
`BEARER`  Retrieve from [Climatiq.io](https://www.climatiq.io/)  
`BASE_URL = "https://beta3.api.climatiq.io"`  
  
`createdb co2tracker_db`  
`sudo service postgresql start`  
`python3 app.py`  
`flask run`  




