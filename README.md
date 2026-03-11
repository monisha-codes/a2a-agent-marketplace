# A2A Agent Marketplace with MCP Gateway

## Overview
This project implements a simple **Agent-to-Agent (A2A) marketplace** where AI agents can register themselves and perform tasks based on their capabilities.

The system contains:
- A **Django registry service** where agents register.
- Two example agents:
  - **Math Helper Agent**
  - **Text Summarizer Agent**
- A **Streamlit UI** to browse agents and send tasks.

This demonstrates how agents can communicate using a simple **A2A JSON protocol**.

---

# Architecture

User interacts with the system through the UI.


Streamlit UI
↓
Django Agent Registry
↓
Search agent by capability
↓
Send A2A request
↓
Agent executes task
↓
Return result


---

# Project Structure


a2a-agent-marketplace
│
├── registry_project
│ ├── registry_project
│ │ ├── settings.py
│ │ ├── urls.py
│ │
│ ├── agents_registry
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │
│ ├── manage.py
│
├── agents
│ ├── math_agent.py
│ ├── summarizer_agent.py
│
├── ui
│ ├── streamlit_app.py
│
├── README.md


---

# Technologies Used

- Python
- Django
- Django REST Framework
- Flask
- Streamlit
- SQLite (default database)

---

# Agent-to-Agent (A2A) Protocol

Agents communicate using a simple **JSON message format**.

## Task Request

```json
{
 "task_id": "123",
 "capability": "math",
 "input": "25 * 4",
 "context": {}
}
Task Response
{
 "task_id": "123",
 "status": "success",
 "result": "100",
 "error": null
}
Agents
Math Helper Agent

Capability:

math

Function:

Receives math expressions

Solves them using Python eval()

Example:

Input

25 * 90

Output

2250

Runs on:

http://127.0.0.1:8001/execute
Text Summarizer Agent

Capability:

summarization

Function:

Receives text

Returns a short summary (first 100 characters)

Example:

Input:

Artificial Intelligence is transforming industries by automating tasks and improving decision making.

Output:

Artificial Intelligence is transforming industries by automating tasks...

Runs on:

http://127.0.0.1:8002/execute
Registry Service (Django)

The registry stores agent information.

Agent model:

class Agent(models.Model):
    name = CharField(max_length=100)
    description = TextField()
    capabilities = JSONField()
    endpoint_url = URLField()
    status = CharField(default='active')
API Endpoints
Register Agent
POST /api/agents/register/

Registers a new agent.

List Agents
GET /api/agents/list/

Returns all registered agents.

Search Agent by Capability
GET /api/agents/search/?capability=math

Returns agents that support the requested capability.

Streamlit UI

The UI provides two tabs:

Agent Directory

Displays all registered agents.

Send Task

Allows users to:

Choose capability

Enter input

Send task to the correct agent

Example:

Capability:

math

Task Input:

25*90

Result:

2250
How to Run the Project

You must run four services.

1. Start Django Registry
cd registry_project
python manage.py runserver

Runs on:

http://127.0.0.1:8000
2. Start Math Agent
cd agents
python math_agent.py

Runs on:

http://127.0.0.1:8001
3. Start Summarizer Agent
python summarizer_agent.py

Runs on:

http://127.0.0.1:8002
4. Start Streamlit UI
cd ui
streamlit run streamlit_app.py

Open in browser:

http://localhost:8501
Example Demo
Example 1 – Math Task

Capability:

math

Input:

25*90

Output:

2250
Example 2 – Summarization Task

Capability:

summarization

Input:

Artificial Intelligence is transforming many industries including healthcare and finance.

Output:

Artificial Intelligence is transforming many industries...