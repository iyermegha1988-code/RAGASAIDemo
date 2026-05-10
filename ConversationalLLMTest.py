import pytest
from markdown_it.rules_block import reference
from ragas import SingleTurnSample, MultiTurnSample
from ragas.messages import HumanMessage, AIMessage
from ragas.metrics._context_precision import (
    LLMContextPrecisionWithoutReference,
)
from ragas.metrics._context_recall import LLMContextRecall
from ragas.metrics._faithfulness import Faithfulness
from ragas.metrics.collections import TopicAdherence

from utils import getAPIData, getJsonData, getMultiAPIData


@pytest.mark.asyncio
@pytest.mark.parametrize("createtestdata",
                        getJsonData("testMultiData.json"),indirect=True)
async def test_conversationalLLM(createLLM,createtestdata):
    # TopicAdherence doesn't accept ChatOllama so this will fail but we can use structured InstructorLLM
    # concept and code is same
    topicAdherence =  TopicAdherence(
        llm=createLLM
    )
    score = await topicAdherence.multi_turn_score(createtestdata)
    print("topicAdherence:", score)


@pytest.fixture
def createtestdata(request):
    test_data = request.param
    responseAPI = getMultiAPIData(test_data)
    conversation = [
        HumanMessage(content=test_data["conversation"][0]["content"]),
        AIMessage(content=test_data["conversation"][1]["content"]),
        HumanMessage(content=test_data["conversation"][2]["content"]),
        AIMessage(content=responseAPI["answer"]),
    ]

    sample = MultiTurnSample(
        user_input=conversation,
        reference_topics=["selenium python course",
            "articles count",
            "downloadable resources"]
    )

    return sample