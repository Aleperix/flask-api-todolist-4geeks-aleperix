from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]

#Ruta para imprimir Hello World
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request.get_json(force=True)
    request_body = json.loads(request.data)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)




# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)