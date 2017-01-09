from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

comments = [
	{'writer': 'aaa', 'content': '수능1'},
	{'writer': 'bbb', 'content': '수능2'},
	{'writer': 'aaa', 'content': '수능3'},
	{'writer': 'bbb', 'content': '수능4'},
	{'writer': 'aaa', 'content': '수능5'},
	{'writer': 'bbb', 'content': '수능6'},
	{'writer': 'aaa', 'content': '수능7'},
	{'writer': 'bbb', 'content': '수능8'},
	{'writer': 'aaa', 'content': '수능9'},
	{'writer': 'bbb', 'content': '수능10'},
	{'writer': 'aaa', 'content': '수능11'},
	{'writer': 'bbb', 'content': '수능12'},
	{'writer': 'aaa', 'content': '수능13'},
	{'writer': 'bbb', 'content': '수능14'},
	{'writer': 'aaa', 'content': '수능15'},
	{'writer': 'bbb', 'content': '수능16'},
	{'writer': 'aaa', 'content': '수능17'},
	{'writer': 'bbb', 'content': '수능18'},
	{'writer': 'aaa', 'content': '수능19'},
	{'writer': 'bbb', 'content': '수능20'},
	{'writer': 'aaa', 'content': '수능21'},
	{'writer': 'bbb', 'content': '수능22'},
	{'writer': 'aaa', 'content': '수능23'},
	{'writer': 'bbb', 'content': '수능24'},
	{'writer': 'aaa', 'content': '수능25'},
	{'writer': 'bbb', 'content': '수능26'},
	{'writer': 'aaa', 'content': '수능27'},
	{'writer': 'bbb', 'content': '수능28'},
	{'writer': 'aaa', 'content': '수능29'},
	{'writer': 'bbb', 'content': '수능30'},
	{'writer': 'aaa', 'content': '수능31'},
	{'writer': 'bbb', 'content': '수능32'},
	{'writer': 'ccc', 'content': '수능33'}
]

userlist = [
	{'user': '장재훈1', 'age': '17'},
	{'user': '장재훈2', 'age': '18'},
	{'user': '장재훈3', 'age': '19'}
]

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
	return render_template('index.html', countdown=delta, comments=comments[start:end], page=page)


@app.route('/post_comment', methods=['GET','POST'])
def new_comment_form():
	if request.method == 'POST':
		print("POST method")
		print('Writer: '+request.form['writer'])
		print('Content: '+request.form['content'])
		comments.append({'writer': request.form['writer'], 'content': request.form['content']})
		return redirect('/')

	return render_template('write.html')

	

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		print('ID: '+request.form['id'])
		print('PW: '+request.form['password'])

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
