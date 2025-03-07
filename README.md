# AI-Powered MSA Chatbot (Dummy Project)

This is a **template implementation** of an AI-powered chatbot designed to assist with **Master Service Agreement (MSA) compliance** and **Statement of Work (SoW) generation** using **FastAPI, ChromaDB, and an open-source model**.

---

## 🚀 Features
- ✅ **FastAPI-powered chatbot API**
- ✅ **Retrieval-Augmented Generation (RAG) using ChromaDB**
- ✅ **Mocked open-source LLM response**
- ✅ **Structured vector database for MSA clause retrieval**
- ✅ **Logging, preprocessing, and testing utilities**
- ✅ **Lightweight and easy-to-extend architecture**

---

## 📦 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/teckyonAI/msa-sow-chatbot.git
cd msa-sow-chatbot
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the API Server**
```sh
uvicorn main:app --reload
```

---

## 🔥 Using the Chatbot API
### **Check Health Status**
```sh
curl http://127.0.0.1:8000/ping
```

### **Retrieve MSA Clause**
```sh
curl -X GET "http://127.0.0.1:8000/retrieve?query=payment"
```

### **Generate Sample SoW**
```sh
curl -X GET "http://127.0.0.1:8000/generate"
```

---

## 📂 Project Structure
```
msa_chatbot_dummy/
│── README.md                     # Overview of the project
│── requirements.txt               # Dependencies
│── main.py                        # FastAPI server
│── config.py                      # Configuration file
│── data/
│   ├── sample_msa.txt             # Sample MSA document
│   ├── sample_sow.txt             # Sample SoW document
│── models/
│   ├── retrieval.py                # RAG-based retrieval with ChromaDB
│   ├── generator.py                # Mocked LLM response
│── vector_store/
│   ├── embedder.py                 # Handles document embedding
│── utils/
│   ├── preprocessing.py             # Text chunking and cleaning
│   ├── logger.py                    # Logging utility
│── tests/
│   ├── test_retrieval.py            # Unit tests for retrieval
│   ├── test_generator.py            # Unit tests for LLM responses
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📞 Contact
For any questions or collaborations, reach out via **GitHub issues** or **discussions**.

Happy Coding! 🚀
