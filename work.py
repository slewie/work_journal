from flask import Flask
import datetime
from data import db_session
from data.__all_models import users, jobs
from flask import render_template
import random
import flask
import os
from flask import url_for, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField
import flask
from flask import render_template


Jobs = jobs.Jobs
User = users.User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars.sqlite")
session = db_session.create_session()


def make_users():
    for i in range(10):
        info = [random.choice(['Ivanov', 'Vasilev', 'Antonov', 'Andreev', 'Alekseev']),
                random.choice(['Ivan', 'Andrey', 'Anton', 'Vasiliy', 'Aleksey']),
                random.choice(list(range(12, 40))),
                random.choice('middle junior senior'.split()),
                random.choice('programmer povar ingeneer pilot captain'.split()),
                'module_' + str(random.choice(list(range(1, 10)))),
                random.choice(list('qwertyuioasdfghjkzxcvbnm')) + random.choice(
                    list('qwertyuioasdfghjkzxcvbnm')) + random.choice(
                    list('qwertyuioasdfghjkzxcvbnm')) + '@ya.ru'
                ]

        s = User()
        s.surname = info[0]
        s.name = info[1]
        s.age = int(info[2])
        s.position = info[3]
        s.speciality = info[4]
        s.address = info[5]
        s.email = info[6]
        session.add(s)
        session.commit()


def make_jobs():
    for i in range(10):
        s = random.choice([2, 3, 4])
        lst = []
        lst2 = list(range(1, 11))
        for i in range(s):
            d = random.choice(lst2)
            lst.append(str(d))
            lst2.remove(d)
        team_lead_id = random.choice(list(range(1, 10)))
        info = [team_lead_id,
                random.choice(
                    'Make module_1, Make module_2, Make_module_3, Взять грунт, Поставить кровати, Заспавнить мобов'.split(
                        ', ')),
                random.choice(list(range(3, 30))),
                ', '.join(lst),
                session.query(User).filter(User.id == team_lead_id).first()
                ]

        s = Jobs()
        s.team_leader_id = info[0]
        s.job = info[1]
        s.work_size = int(info[2])
        s.collaborators = info[3]
        s.team_leader = info[4]
        session.add(s)
        session.commit()


@app.route('/')
def index():
    jobs_list = session.query(Jobs).all()
    return render_template('jobs_jurnal.html', list=jobs_list)


def main():
    app.run()


if __name__ == '__main__':
    main()
