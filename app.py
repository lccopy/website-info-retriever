from flask import Flask, render_template, request
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        url = None
        query = None
        response = None
        if request.method == 'POST':
            url = request.form.get('url')

            if not url.startswith("https://"):
                url = f"https://{url}"

            query = request.form.get('query')

            #load content from url
            loader = WebBaseLoader(url)
            data = loader.load()

            #split in chunks
            text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_documents(data)

            openai_embeddings = OpenAIEmbeddings()

            #croma vect to stock data
            knowledge_base = FAISS.from_documents(documents=docs, embedding=openai_embeddings)

            #retriever
            qa_with_source = knowledge_base.similarity_search(query)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=qa_with_source, question=query)

        return render_template('index.html', url=url, query=query, response=response)

    except:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=False)
