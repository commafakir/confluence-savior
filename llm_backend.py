import chromadb
from langchain.chains import ChatVectorDBChain
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from settings import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_MODEL_DEPLOYMENT_NAME, AZURE_EMBEDDING_MODEL 
from embedding import chroma


prompt_template = """
You are a project documentation assistant. The user is writing new pieces of documentation and wants to know whether it is conflicting with previous documentation. 
You are given a set of documents and a new document. You need to check whether the new document is conflicting with the previous documents.

Documents: {context}

New Document: {question}

Is the new document conflicting with the previous documents? Please answer with "yes" or "no", and give a reason for your answer.
"""

prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

llm = AzureChatOpenAI(
    azure_deployment=AZURE_MODEL_DEPLOYMENT_NAME,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    openai_api_key=AZURE_OPENAI_KEY,
    openai_api_version=AZURE_OPENAI_API_VERSION
)

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    input_key="question",
    output_key="answer",
    k=0,
)

chain = ChatVectorDBChain.from_llm(
    llm=llm,
    chain_type="stuff",
    vectorstore=chroma,
    verbose=True,
    return_source_documents=True,
    memory=memory,
    get_chat_history=lambda h: h,
    rephrase_question=True,
    combine_docs_chain_kwargs={"prompt": prompt},
    top_k_docs_for_context=5,
)

def validate_document(text):
    return chain(text)