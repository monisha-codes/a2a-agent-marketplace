import requests
import uuid

REGISTRY_SEARCH = "http://127.0.0.1:8000/api/agents/search"

def run_task(capability, user_input):

    agents = requests.get(
        REGISTRY_SEARCH,
        params={"capability": capability}
    ).json()

    if not agents:
        return "No agent found"

    agent = agents[0]

    task = {
        "task_id": str(uuid.uuid4()),
        "capability": capability,
        "input": user_input,
        "context": {}
    }

    response = requests.post(agent["endpoint_url"], json=task)

    return response.json()


if __name__ == "__main__":
    print(run_task("math", "10+5"))