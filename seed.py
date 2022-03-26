from app import app
from models import User, UserActivity, db


db.drop_all()
db.create_all()

user1 = User(username="kitties123", email="test@gmail.com", password="sdfhbsd", first_name="Joe", last_name="Shmoe")
user2 = User(username="mjanicki01", email="test2@gmail.com", password="sdfhbsd", first_name="Jane", last_name="Doe")
user3 = User(username="bobcats456", email="test3@gmail.com", password="sdfhbsd", first_name="Jack", last_name="Nickleson")
user4 = User(username="bobjoe123", email="test4@gmail.com", password="sdfhbsd", first_name="Nice", last_name="Butt")

db.session.add_all([user1, user2, user3, user4])
db.session.commit()

ua1 = UserActivity(user_id=2, activity_id="Clothing Purchase", emission_factor_id="consumer_goods-type_clothing", date="2/2/2000", spend_qty=21, spend_unit="USD", co2e=151)


db.session.add_all([ua1])
db.session.commit()
