import anvil.server
import os
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

def generate_summary_kivy(input_summary, query_input):
    # diese Funktion ist in der Application GUI Valuation Summarization verbaut
    os.environ["OPENAI_API_KEY"] = "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"
    # die Enviroment Variabel wird mit dem API Key von OpenAI befüllt

    loader = PyPDFLoader(input_summary)
    # die PDF, welche zusammengefasst wird, wird durch einen PDFLoader eingelesen
    index = VectorstoreIndexCreator().from_loaders([loader])
    # die eingelesene PDF wird Embedded und in einem Vectorstore gespeichert

    return index.query_with_sources(query_input, llm=ChatOpenAI(model="gpt-3.5-turbo  ", temperature=0.1))
    # zurückgegeben wird ein String, welche die  Inputquery, die erzeugte Zusammenfassung von GPT-Modell 3.5-turbo mit Temperature(0.1) und die Quelle der Zusammenfassung ausgibt


  
