from flask import Flask, render_template, request
import git

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    if request.method == 'POST':
        try:
            expression = request.form.get('expression')
            result = str(eval(expression))
        except:
            result = "Error"
    return render_template('index.html', result=result)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/famil-student/pythonanywhere-testapp.git')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')