from flask import Flask, jsonify
import elasticsearch
import redis

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Switch on Laptop',
        'description': 'Press the power button',
        'done': False
    },
    {
        'id': 2,
        'title': 'Login',
        'description': 'Enter the login credentials',
        'done': False
    }
]

#API 1
@app.route('/index', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    tasks = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201

#index data into Radis
tasks = {
            'id': 3,
            'title': 'Open explorer',
            'description': 'Search file',
            'done': False
        }
r = redis.StrictRedis()
r.set('tasks', tasks)
#index data into ElasticSearch
curl -XPUT '/index' -d '{
                            'id':3,
                            'title': 'Open explorer',
                            'description': 'Search file',
                            'done': False
                        }'

#API 2
@app.route('/index', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

#gets data from Radis
r.get('tasks')

#API 3
@app.route('/search', methods=['GET'])
def search_tasks():
    return jsonify({'tasks': tasks})

#gets data from ElasticSearch
curl -XGET '/search_search?q=title: Login'

if __name__ == '__main__':
    app.run(debug=True)

