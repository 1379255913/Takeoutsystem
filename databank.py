# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
import pymysql

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
# 创建数据库的操作对象
db = SQLAlchemy()


class Test(db.Model):
    __tablename__ = "test"

    name = db.Column(db.String(255), primary_key=True)
    id = db.Column(db.Integer)
    inf = db.Column(db.String(255))

    # 给Role类创建一个uses属性，关联users表。
    # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
    # users = db.relationship('User', backref="role")

    # 相当于__str__方法。
    def __repr__(self):
        return "Role: %s %s %s" % (self.id, self.name, self.inf)


class UserInformation(db.Model):
    __tablename__ = "userinformation"

    email = db.Column(db.String(128), primary_key=True)
    nickname = db.Column(db.String(100))
    password = db.Column(db.String(128), nullable=False)
    type = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    phone = db.Column(db.String(128))
    address = db.Column(db.String(255))
    information = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    children1 = db.relationship("ShopData", backref="userinformation")

    def __repr__(self):
        return "Role: %s %s %s %s %s %s %s %s %s " % (
        self.email, self.nickname, self.password, self.type, self.create_time, self.phone, self.address,
        self.information, self.photo)


class ShopType(db.Model):
    __tablename__ = "shoptype"

    email = db.Column(db.String(255), primary_key=True)
    type0 = db.Column(db.String(255))
    type1 = db.Column(db.String(255))
    type2 = db.Column(db.String(255))
    type3 = db.Column(db.String(255))
    type4 = db.Column(db.String(255))
    type5 = db.Column(db.String(255))
    type6 = db.Column(db.String(255))
    type7 = db.Column(db.String(255))
    type8 = db.Column(db.String(255))
    type9 = db.Column(db.String(255))


class ShopData(db.Model):
    __tablename__ = "shopdata"

    email = db.Column(db.String(255),db.ForeignKey('userinformation.email') ,nullable=False)
    title = db.Column(db.String(255))
    price = db.Column(db.String(255))
    information = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    type = db.Column(db.String(255), nullable=False)
    likes = db.Column(db.Integer)
    fav = db.Column(db.Integer)
    repeats = db.Column(db.Integer)
    movie = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)
    def __repr__(self):
        return "Role: %s %s %s %s %s %s %s %s %s %s %s %s" % (
        self.email, self.title, self.price, self.information, self.photo, self.type,
        self.likes, self.fav,self.repeats,self.movie,self.id,self.userinformation.nickname)

class OrderMoney(db.Model):
    __tablename__ = "ordermoney"

    email = db.Column(db.String(255))
    shop = db.Column(db.String(255))
    horseman = db.Column(db.String(255))
    submit_time = db.Column(db.DateTime)
    money_shop = db.Column(db.String(255))
    money_horse = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)


class OrderData(db.Model):
    __tablename__ = "orderdata"

    email = db.Column(db.String(255))
    information = db.Column(db.Text)
    shop = db.Column(db.String(255))
    submit_time = db.Column(db.DateTime)
    arrive_time = db.Column(db.DateTime)
    ino = db.Column(db.String(255))
    horseman = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)


class Likes(db.Model):
    __tablename__ = "likes"

    email = db.Column(db.String(255), nullable=False)
    shop_email = db.Column(db.String(255), nullable=False)
    food = db.Column(db.String(255), nullable=False)
    judge = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)


class Fav(db.Model):
    __tablename__ = "fav"

    email = db.Column(db.String(255), nullable=False)
    shop_email = db.Column(db.String(255), nullable=False)
    food = db.Column(db.String(255), nullable=False)
    judge = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)


class Follow(db.Model):
    __tablename__ = "follow"

    email = db.Column(db.String(255), nullable=False)
    follow_email = db.Column(db.String(255), nullable=False)
    others = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)


class Issue(db.Model):
    __tablename__ = "issue"

    Ino = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    title = db.Column(db.Text)
    issue_time = db.Column(db.DateTime)
    shop = db.Column(db.String(255))


class Comment(db.Model):
    __tablename__ = "comment"

    Cno = db.Column(db.String(128), nullable=False)
    Ino = db.Column(db.String(128), nullable=False)
    comment = db.Column(db.Text)
    comment_time = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(128))
    shop = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)

# class User(db.Model):
#     # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(16), unique=True)
#     email = db.Column(db.String(32), unique=True)
#     password = db.Column(db.String(16))
#     # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
#     role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
#
#     def __repr__(self):
#         return "User: %s %s %s %s" % (self.id, self.name, self.password, self.role_id)