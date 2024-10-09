from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/deploy', methods=['GET', 'POST'])
def deploy():
    return render_template('deploy.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('schedule.html')

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    return render_template('reports.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('settings.html')


def load_tasks():
    with open('static/tasks.json', 'r') as file:
        tasks = json.load(file)
    return tasks


def save_tasks(tasks):
    with open('static/tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

@app.route('/add_task', methods=['POST'])
def add_task():
    
    tasks = load_tasks()
    
    
    task_data = request.get_json()
    new_task = {
        "name": task_data["name"],
        "status": "Pending",  
        "progress": 0,        
        "date": "2024-09-23", 
    }
    
    tasks.append(new_task)
    
    save_tasks(tasks)
    
    return jsonify({"message": "Task added successfully"}), 200

@app.route('/remove_task/<int:index>', methods=['DELETE'])
def remove_task(index):
    
    tasks = load_tasks()

    
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)  
        save_tasks(tasks) 
        return jsonify({"message": f"Task '{removed_task['name']}' removed successfully"}), 200
    else:
        return jsonify({"error": "Invalid task index"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
