import pytest
from ragas import SingleTurnSample
from ragas.metrics._context_precision import (
    LLMContextPrecisionWithoutReference,
)
from utils import getAPIData, getJsonData

#Context Precision= Relevant retrieved items/Total retrieved items

@pytest.mark.asyncio
@pytest.mark.parametrize("createtestdata",
                        getJsonData("testData.json"),indirect=True)
async def test_context_precision(createLLM,createtestdata):
    context_precision =  LLMContextPrecisionWithoutReference(
        llm=createLLM
    )
    score = await context_precision.single_turn_ascore(createtestdata)
    print("Context Precision Score:", score)


@pytest.fixture
def createtestdata(request):
    test_data = request.param
    responseAPI = getAPIData(test_data)

    sample = SingleTurnSample(
        user_input=test_data["question"],
        response=responseAPI["answer"],
        retrieved_contexts=[responseAPI["retrieved_docs"][0]["page_content"],
                            responseAPI["retrieved_docs"][1]["page_content"]]
    )
    return sample