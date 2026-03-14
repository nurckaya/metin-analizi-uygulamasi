import streamlit as st
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import tempfile

# 1. Ayarlar: Google Gemini API Anahtarını Tanımla
os.environ["GOOGLE_API_KEY"] = "AIzaSyB5bhMmgXjBv1P2MNJJpSZktrsTjALUvHc"


# Large Language Model
Settings.llm = Gemini(
    model_name="models/gemini-2.5-flash",
    transport="rest" 
)

# Embedding model 
Settings.embed_model = GeminiEmbedding(
    model_name="models/gemini-embedding-001"
)

st.title("Metin Analizi Uygulaması")

uploaded_file = st.file_uploader("Bir PDF yükleyin", type=["pdf"])

if uploaded_file:
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Gemini dökümanı inceliyor..."):
        
            reader = SimpleDirectoryReader(input_dir=temp_dir)
            documents = reader.load_data()
            index = VectorStoreIndex.from_documents(documents)
            query_engine = index.as_query_engine()

        st.success("Hazır!")
        user_query = st.text_input("Döküman hakkında sorunuzu yazın:")
        
        if user_query:
            response = query_engine.query(user_query)
            st.markdown("### Yanıt:")
            st.write(response.response)