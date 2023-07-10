from flask import Flask

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template'index.html'

@app.route('/about.html')
def about(): # put application's code here
    return render_template('about.html')

@app.route('/courses.html')
def courses(): # put application's code here
    return render_template('courses.html')

@app.route('/blog.html')
def blog(): # put application's code here
    return render_template('blog.html')

@app.route('/courses2.html')
def courses2(): # put application's code here
    return render_template('courses2.html')

@app.route('/xuqiutupu.html')
def xuqiutupu(): # put application's code here
    return render_template('xuqiutupu.html')

if __name__ == '__main__':
    app.run()
