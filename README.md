AI Response Evaluation Framework

This project is a QA automation framework built using Python + RAGAS to evaluate the quality and authenticity of AI-generated responses in RAG (Retrieval-Augmented Generation) systems.

Objective

The framework helps QA teams validate AI responses by calculating metrics such as:

Faithfulness
Context Precision
Context Recall
Factual Correctness
Answer Relevancy

It helps identify:

Hallucinations
Incorrect answers
Poor retrieval quality
Irrelevant AI responses
Tech Stack
Python
Pytest
RAGAS
LangChain
OpenAI / Azure OpenAI
Project Structure
├── ContextPrecision.py
├── ContextRecall.py
├── Faithfulness.py
├── FactualCorrectnessAndRelevancy.py
├── ConversationalLLMTest.py
├── utils.py
├── testData.json
└── conftest.py
