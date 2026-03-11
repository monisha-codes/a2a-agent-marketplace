from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

REGISTRY = "http://127.0.0.1:8000/api/agents/register"

agent_data = {
    "name": "Web Search Agent",
    "description": "Searches the web",
    "capabilities": ["search"],
    "endpoint_url": "http://127.0.0.1:8003/execute"
}

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    query = data["input"]

    result = f"Mock search result for: {query}"

    return jsonify({
        "task_id": data["task_id"],
        "status": "success",
        "result": result,
        "error": None
    })


def register():
    requests.post(REGISTRY, json=agent_data)


if __name__ == "__main__":
    register()
    app.run(port=8003)