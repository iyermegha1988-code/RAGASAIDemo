import pytest
from ragas import SingleTurnSample
from ragas.metrics._answer_relevance import ResponseRelevancy
from ragas.metrics._factual_correctness import FactualCorrectness
from utils import getAPIData, getJsonData
from langchain_ollama import OllamaEmbeddings

#relevancy - similar like faithfulness but checks if LLM output is in context to user query(not involved vector DB)
#factualcorrectness - checks the llm response based on real world truth
@pytest.mark.asyncio
@pytest.mark.parametrize("createtestdata",
                        getJsonData("testData.json"),indirect=True)
async def test_factualcorrectnessrelevance(createLLM,createtestdata):
    embedding_model = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    metrics =  [ResponseRelevancy(
        llm=createLLM,embeddings=embedding_model
    ), FactualCorrectness (llm=createLLM)]

    for metric in metrics:
        score  = await metric.single_turn_ascore(createtestdata)
        print(score)

@pytest.fixture
def createtestdata(request):
    test_data = request.param
    responseAPI = getAPIData(test_data)

    sample = SingleTurnSample(
        user_input=test_data["question"],
        response=responseAPI["answer"],
        reference= test_data["reference"],
        retrieved_contexts= [doc["page_content"] for doc in responseAPI["retrieved_docs"]]
    )
    return sample