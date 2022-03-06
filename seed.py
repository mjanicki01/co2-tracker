from app import app #previously db
from models import User, Activity, UserActivity, Event, db #db may be in 'from app'


db.drop_all()
db.create_all()

act1 = Activity(id="clothing", emission_factor_id="consumer_goods-type_clothing", spend_unit="USD", co2e="9.999")
act2 = Activity(id="driving", emission_factor_id="passenger_vehicle-vehicle_type_motorcycle-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na", spend_unit="mi", co2e="9.999")
act3 = Activity(id="flying", emission_factor_id="passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na", spend_unit="mi", co2e="9.999")
act4 = Activity(id="bottle", emission_factor_id="plastics_rubber-type_plastic_bottles", spend_unit="lb?", co2e="9.999")

db.session.add_all([act1, act2, act3, act4])
db.session.commit()

user1 = User(username="kitties123", email="test@gmail.com", password="sdfhbsd", first_name="Joe", last_name="Shmoe")
user2 = User(username="mjanicki01", email="test2@gmail.com", password="sdfhbsd", first_name="Jane", last_name="Doe")
user3 = User(username="bobcats456", email="test3@gmail.com", password="sdfhbsd", first_name="Jack", last_name="Nickleson")
user4 = User(username="bobjoe123", email="test4@gmail.com", password="sdfhbsd", first_name="Nice", last_name="Butt")

db.session.add_all([user1, user2, user3, user4])
db.session.commit()

ua1 = UserActivity(user_id=2, emission_factor_id="consumer_goods-type_clothing", date="2/2/2000", spend_qty=21, spend_unit="USD", co2e=151)


db.session.add_all([ua1])
db.session.commit()

event1 = Event(user_id=2, user_activity_id=1)

db.session.add_all([event1])
db.session.commit()