# CO2e Tracker

## Demo
<div style="position: relative; padding-bottom: 59.4059405940594%; height: 0;"><iframe src="./static/images/demo.mp4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## About
As Capstone 1 of Springboard's Software Engineering Career Track, CO2e Tracker is an database-driven app that allows users to record their activities along with corresponding CO2 emissions.
Using Climatiq's API to calculate CO2e, four types of activities are available to be recorded: Flights, driving, and purchasing of new clothing or plastic bottles. The emission factor for purchasing includes the cradle-to-shelf product lifecycle. [View Emission Descriptions](./proposal/emission_desc.png)

## [User Flow](./proposal/user_flow.png)
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
Note: Requires PostgreSQL installation

`python -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  
`touch ".env"`
  
Create & Start database locally:

`createdb co2tracker_db`
`sudo service postgresql start`

Add the following variables into your .env file:

`SECRET_KEY`  
`BEARER`  Retrieve from [Climatiq.io](https://www.climatiq.io/)  
`BASE_URL = "https://beta4.api.climatiq.io"`
`DATABASE_URL`

Run app:

`python app.py`  
`flask run`  




