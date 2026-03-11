from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

REGISTRY_URL = "http://127.0.0.1:8000/api/agents/register/"

agent_data = {
    "name": "Math Helper",
    "description": "Solves math problems",
    "capabilities": ["math"],
    "endpoint_url": "http://127.0.0.1:8001/execute"
}

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    task_id = data["task_id"]
    question = data["input"]

    try:
        result = eval(question)
    except:
        result = "Invalid expression"

    return jsonify({
        "task_id": task_id,
        "status": "success",
        "result": str(result),
        "error": None
    })


def register():
    try:
        r = requests.post(REGISTRY_URL, json=agent_data)
        print("Registry response:", r.status_code, r.text)
    except Exception as e:
        print("Registration failed:", e)


if __name__ == "__main__":
    register()
    app.run(port=8001)