import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smartface-17341-default-rtdb.firebaseio.com/"
})

ref = db.reference('persons')

data = {
    "321654":
        {
                "name": "Divyang Jha",
                "address": "Balchand Para Bundi",
                "gender": "Male",
                "total_visits": 7,
                "standing": "G",
                "age": 21,
                "last_visiting_time": "2022-12-11 00:54:34"
        },
        "963852":
            {
                "name": "Hemant Dadhich",
                "address": "Sitapura PIET",
                "gender": "Male",
                "total_visits": 10,
                "standing": "G",
                "age": 20,
                "last_visiting_time": "2022-10-21 00:54:34"
            },
        "852741":
            {
                "name": "Prem Bhargav",
                "address": "Sitapura PIET",
                "gender": "Male",
                "total_visits": 12,
                "standing": "G",
                "age": 20,
                "last_visiting_time": "2021-06-11 00:54:34"
            }
}

for key, value in data.items():
    ref.child(key).set(value)
