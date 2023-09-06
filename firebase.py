# importing required modules

import firebase_admin
from firebase_admin import db, credentials

# authenticate to firebase

cred= credentials.Certificate("credentials.json")

