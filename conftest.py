import pytest
from langchain_community.chat_models import ChatOllama


@pytest.fixture
def createLLM():
    chatOll = ChatOllama(
        model="llama3",
        temperature=0,
        format="json"
    )
    return chatOll