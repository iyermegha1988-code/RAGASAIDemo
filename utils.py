from pathlib import Path

import requests,json

def getJsonData(filename):
    test_data_path=Path(__file__).parent.absolute()/filename
    with open(test_data_path) as fileJson:
        return json.load(fileJson)


def getAPIData(test_data):
    response = requests.post("https://rahulshettyacademy.com/rag-llm/ask", json={
        "question": test_data["question"],
        "chat_history": [

        ]
    })
    responseJson = response.json()
    return responseJson

def getMultiAPIData(test_data):
    # extract last human question
    last_question = None

    for msg in test_data["conversation"]:
        if msg["role"] == "human":
            last_question = msg["content"]

    # send full chat history as API expects
    response = requests.post(
        "https://rahulshettyacademy.com/rag-llm/ask",
        json={
            "question": last_question,
            "chat_history": test_data["conversation"]
        }
    )

    return response.json()