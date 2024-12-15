import streamlit as st
import requests

# Streamlit app
st.title("Government Knowledge")  # Corrected spelling

# API Key and Endpoint
api_key = "xai-2ir0TPlXU8OzYsvXK4S6BUE7B1OMUqitJcjRkpoh3tsj65f2jKxf0Qy2qQEjUTQbojas9GKg8mWSAHPB"
api_endpoint = "https://api.x.ai/v1/chat/completions"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Enter your message"):  # More concise phrasing
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the request payload
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful and informative assistant."},  # Improved system message
            {"role": "user", "content": prompt}
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0
    }

    # Make the API call
    response = requests.post(api_endpoint, headers=headers, json=data)

    # Extract the response
    if response.status_code == 200:
        grok_response = response.json()["choices"][0]["message"]["content"]
        # Add Grok response to chat history
        st.session_state.messages.append({"role": "assistant", "content": grok_response})

        # Display Grok response
        with st.chat_message("assistant"):
            st.markdown(grok_response)
    else:
        st.error(f"Grok API request failed with status code: {response.status_code}")
        st.error(response.text)  # Display the error message from the API
