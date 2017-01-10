from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///satcounter2.db'
app.config['SQLALCHEMY_ECHO'] = True

db= SQLAlchemy(app)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	writer = db.Column(db.String(80), nullable=False)
	content = db.Column(db.Text, nullable=False)

	def __init__(self, writer, content):
		self.writer = writer
		self.content = content

	def __repr__(self):
		return '<Message %r>' % self.id

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, nullable=False)
	password = db.Column(db.Text, nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.id

intro = "strstrstrstr"

@app.route('/')
def index():
	sat_date = datetime(2017, 11, 16)
	now = datetime.now()
	delta = sat_date - now

	page = int(request.args.get('page', 1))
	limit = 5
	
	start = (page - 1) * limit
	end = start + limit

	#db = get_db()
	#comments = db.execute("SELECT * FROM comments LIMIT 5 OFFSET "+str(start)).fetchall()

	comments = Message.query.offset(start).limit(5).all()
	count = Message.query.count()
	if(count%5==0):
		count = count/5

	else:
		count=count/5+1

	count = int(count)

	return render_template('index.html', countdown=delta, comments=comments, page=page, end=count)


@app.route('/post_comment', methods=['GET','POST'])
def new_comment_form():
	if request.method == 'POST':
		print("POST method")
		print('Writer: '+request.form['writer'])
		print('Content: '+request.form['content'])

	#	db = get_db()
	#	db.execute(
	#		"INSERT INTO comments (writer, content) VALUES (?, ?)",
	#		(request.form['writer'], request.form['content'])
	#	)
	#	db.commit()

		msg = Message(request.form['writer'], request.form['content'])
		db.session.add(msg)
		db.session.commit()

		return redirect('/')

	return render_template('write.html')

	

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		print('ID: '+request.form['id'])
		print('PW: '+request.form['password'])

		usr = User(request.form['id'], generate_password_hash(request.form['password']))
		db.session.add(usr)
		db.session.commit()

	return render_template('register.html')

@app.route('/hello/')
def hello():
	return '안녕!'

@app.route('/users')
def users():
	return render_template('user_list.html', userlist=userlist)

@app.route('/users/<string:username>')
def user_profile(username):
	print(username)
	return render_template('profile.html', username=username)

@app.route('/about')
def about():
	return render_template('about.html', intro_str=intro)

@app.route('/article/<int:num>')
def number(num):
	print(num)
	return "%d번째 문서" % num

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1828, debug=True)
