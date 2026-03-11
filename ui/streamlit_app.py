import streamlit as st
import requests

REGISTRY_LIST = "http://127.0.0.1:8000/api/agents/list/"

st.title("A2A Agent Marketplace")

tab1, tab2 = st.tabs(["Agent Directory", "Send Task"])

with tab1:
    st.header("Registered Agents")

    response = requests.get(REGISTRY_LIST)

if response.status_code == 200:
    agents = response.json()
else:
    st.error("Registry service not responding")
    agents = []

    for agent in agents:
        st.write("###", agent["name"])
        st.write(agent["description"])
        st.write("Capabilities:", agent["capabilities"])


with tab2:

    capability = st.text_input("Capability (math/summarization/search)")
    user_input = st.text_area("Task Input")

    if st.button("Send Task"):

        res = requests.get(
            "http://127.0.0.1:8000/api/agents/search",
            params={"capability": capability}
        ).json()

        if res:
            agent = res[0]

            payload = {
                "task_id": "1",
                "capability": capability,
                "input": user_input,
                "context": {}
            }

            result = requests.post(agent["endpoint_url"], json=payload).json()

            st.success(result["result"])