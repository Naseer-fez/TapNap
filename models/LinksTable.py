from models.LoginSql import db
# from LoginSql import db
import time

class Links(db.Model):
    __tablename__="Links"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId=db.Column(db.Integer, db.ForeignKey('User.id'),index=True, nullable=True,default=-1)
    Link=db.Column(db.String(768),unique=True,nullable=False)
    Code=db.Column(db.Integer,unique=True,nullable=False)
    CreatedTime= db.Column(db.BigInteger, default=lambda: int(time.time()),nullable=False)
    AllowedTime=db.Column(db.BigInteger, default=lambda: int(time.time())+864000,nullable=False)
    