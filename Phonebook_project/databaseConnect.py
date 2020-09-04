from mongoengine import *

class PhonebookData(Document):
    user_id = IntField(unique = True, required = True)
    user_name = StringField(required = True)
    user_email = EmailField()
    user_contact = IntField(required = True, unique = True)

    
