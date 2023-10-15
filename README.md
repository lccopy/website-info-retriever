# website-info-retriever

## Overview

A Flask web app that allows users to ask questions and retrieve information from any website, **using url only**.

## How It Works

HTML Parsing: Utilizes Langchain's WebBaseLoader to load and parse HTML content from the specified website.

Text Chunking: Splits the parsed text into manageable chunks using Langchain's CharacterTextSplitter.

Text Embedding and Indexing: Uses Langchain's OpenAIEmbeddings and FAISS vector store to index the text chunks.

Question Answering: Leverages Langchain's OpenAI and load_qa_chain to answer the query using the indexed text.

## Usage
- pip install requirements.txt

- create .env file with your OPENAI_API_KEY

- run app.py

## Screenshots
Exemple 1:

Retrieve today's three main topics from The New York Times
<img width="1247" alt="Screenshot 2023-10-15 235707" src="https://github.com/lccopy/website-info-retriever/assets/111251905/9c7857a0-5d21-4c4e-8032-8e00ad2d74bd">
____________________________________
Exemple 2:

Ask a question to a Github repo:
<img width="1248" alt="Screenshot 2023-10-15 235916" src="https://github.com/lccopy/website-info-retriever/assets/111251905/f4945de7-dcd6-4429-a930-6f7a8536ad62">
