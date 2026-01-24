from extensions import db

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(100), unique=True, nullable=False)
    password = db.column(db.String(200), nullable=False)

    def set_password(self, raw_password):
        from extensions import bcrypt
        self.password = bcrypt.generate_password_hash(raw_password).decode('utf-8')
    def check_password(self, raw_password):
        from extensions import bcrypt
        return bcrypt.check_password_hash(self.password, raw_password)