from flask import Flask, render_template , request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@26102000@localhost/our_users"


connection_url = sa.engine.URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="@26102000",
    host="localhost",
    database="our_users",
    port="3306"
)
print(connection_url)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_url #'mysql+pymysql://root:@26102000@localhost:3306/our_users'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/',methods=['GET','POST'])
def hello_world():
    if(request.method=='POST'):

        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo= Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/products')
def products():
    allTodo= Todo.query.all() 
    print(allTodo) 
    return 'this is product page!'

@app.route('/update/<int:snoforupdate>',methods=['GET','POST'])
def update(snoforupdate):
    if (request.method=='POST'):
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=snoforupdate).first()
        todo.title=title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno=snoforupdate).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:provided_sno>')
def delete(provided_sno):
    todo= Todo.query.filter_by(sno=provided_sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
