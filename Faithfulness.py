import pytest
from ragas import SingleTurnSample
from ragas.metrics._context_precision import (
    LLMContextPrecisionWithoutReference,
)
from ragas.metrics._context_recall import LLMContextRecall
from ragas.metrics._faithfulness import Faithfulness

from utils import getAPIData, getJsonData

@pytest.mark.asyncio
@pytest.mark.parametrize("createtestdata",
                        getJsonData("testData.json"),indirect=True)
async def test_faithfulness(createLLM,createtestdata):
    faithfulness =  Faithfulness(
        llm=createLLM
    )
    score = await faithfulness.single_turn_ascore(createtestdata)
    print("faithfulness:", score)

#Faithfulness= Statements supported by context(AI stick to context)/Total statements in answer
# checks in reference to the vector DB content - not hallucinating

@pytest.fixture
def createtestdata(request):
    test_data = request.param
    responseAPI = getAPIData(test_data)

    sample = SingleTurnSample(
        user_input=test_data["question"],
        response=responseAPI["answer"],
        retrieved_contexts= [doc["page_content"] for doc in responseAPI["retrieved_docs"]]
    )
    return sample