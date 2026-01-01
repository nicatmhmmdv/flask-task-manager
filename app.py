from flask import Flask, render_template, request, redirect, url_for, jsonify
import service

app = Flask(__name__)
service.init_db()

#Routes
@app.route('/')
def index():
    
    tasks = service.get_all_tasks()
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def add_task_ui():
    title = request.form.get('title')
    if title:
        service.add_task(title)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)