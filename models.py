from app import db


class User(db.Document):
    mac_adress = db.StringField(required=True)
    agree = db.BooleanField(required=True)

    def __unicode__(self):
        return f'{self.mac_adress}-{self.agree}'
