# import torch
# import os
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import WebBaseLoader, PyPDFDirectoryLoader # Load From the internet and PDF Respectively

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.embeddings import SentenceTransformerEmbeddings

# #Please update your pinecone-client package version >=3.0.1
# from pinecone import Pinecone as PineconeClient #Importing the Pinecone class from the pinecone package
# from langchain_community.vectorstores import Pinecone

# from dotenv import load_dotenv
# load_dotenv()

# # for scraping the data from
# urls = [
#     "https://clickup.com/blog/chain-of-thought-prompting/"
# ]

# docs = [WebBaseLoader(url) for url in urls]
# docs_list = [item for sublist in docs for item in sublist] # List of documents ? 

# text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#     chunk_size = 250, chunk_overlap = 50
# )

# doc_splits = text_splitter.split_documents(docs_list) # Chunk of documents

# # # Load PDF Document
# # # Function to read documents
# # def load_docs(directory):
# #   """
# #     Given a directory, load every document in it.

# #     Input (s):
# #       directory (str): a path to directory 
    
# #     Return:
# #       loaded documents, ready to be processed further
# #   """

# #   loader = PyPDFDirectoryLoader(directory)
# #   documents = loader.load()
# #   return documents

# # #This function will split the documents into chunks
# # def split_docs(documents, chunk_size=1000, chunk_overlap=250):
# #   """
# #     Given the document, split them into chunks that have an overlapping length of aa specified value

# #     Input (s):
# #       documents: a loaded document, can be obtained by callinf the load_docs() function
# #       chunk_size (int): The size of each chunk. Default to 1000.
# #       chunk_overlap(int): The overlapping length between the chunk, the higher chunk_overlap value, the more context preserved 
# #                           (at the cost of more resource consumption). Default to 250.
    
# #     Return:
# #       a splitted docs, ready to be uploaded to the Pinecone vector database
# #   """

# #   text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
# #   docs = text_splitter.split_documents(documents)
# #   return docs

# # # Passing the directory to the 'load_docs' function
# # print("Preparing document for embedding ...")
# # directory = os.environ.get("PATH_PDF")
# # documents = load_docs(directory)
# # docs = split_docs(documents)
# # print("Preparing document complete!")

# # # embeddings = SentenceTransformerEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# # print("Preparing Sentence Transformer ...")
# # model_kwargs = {'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
# # encode_kwargs = {'normalize_embeddings': False}
# # embeddings = HuggingFaceEmbeddings(
# #     model_name=os.environ.get("EMBEDDER_NAME"),
# #     model_kwargs=model_kwargs,
# #     encode_kwargs=encode_kwargs
# # )
# # print("Preparing Sentence Transformer complete!")

# # print("Start uploading to Pinecone ...")
# # PineconeClient(environment="gcp-starter")
# # index_name="ragfinanceml"
# # index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
# # print("Uploading complete!")