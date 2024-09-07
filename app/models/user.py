class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def find_by_email(db, email):
        return db.users.find_one({"email": email})

    @staticmethod
    def insert_user(db, user):
        return db.users.insert_one(user.to_dict())
