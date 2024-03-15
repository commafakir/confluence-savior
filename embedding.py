from settings import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_MODEL_DEPLOYMENT_NAME, AZURE_EMBEDDING_MODEL 
import chromadb
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import AzureOpenAIEmbeddings

DB_PATH = 'chroma.db'
embedding_model = AzureOpenAIEmbeddings(
    azure_deployment=AZURE_EMBEDDING_MODEL,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    openai_api_key=AZURE_OPENAI_KEY,
    openai_api_version=AZURE_OPENAI_API_VERSION
)

client = chromadb.PersistentClient(DB_PATH)
chroma = Chroma(client=client, embedding_function=embedding_model, collection_name="default")

def embed_document(path):
    with open(path, 'r') as f:
        text = f.read()
    
    chunks = [text]
    metadata = [{}]

    chroma.add_texts(chunks, metadata)
