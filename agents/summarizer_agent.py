from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

REGISTRY_URL = "http://127.0.0.1:8000/api/agents/register/"

agent_data = {
    "name": "Text Summarizer",
    "description": "Summarizes text",
    "capabilities": ["summarization"],
    "endpoint_url": "http://127.0.0.1:8002/execute"
}

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    text = data["input"]

    summary = text[:100] + "..."

    return jsonify({
        "task_id": data["task_id"],
        "status": "success",
        "result": summary,
        "error": None
    })


def register():
    requests.post(REGISTRY_URL, json=agent_data)


if __name__ == "__main__":
    register()
    app.run(port=8002)