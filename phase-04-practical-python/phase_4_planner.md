## **Phase 4 — AI and intelligent application development**



Days 31–42

&#x20;Goal: Build an AI-powered application using an existing language model.



Before starting, understand one important distinction:

**Building an AI application is different from training an AI model.**

In these 12 days, you will build an application that communicates with an existing LLM through an API. You will not train a ChatGPT-scale foundation model.

| Day    | Topics                                    | Practical assignment                                      |
| ------ | ----------------------------------------- | --------------------------------------------------------- |
| **31** | AI, ML, DL, NLP, LLMs, tokens and context | Explain how ChatGPT works and create a rule-based chatbot |
| **32** | REST APIs, HTTP, JSON, authentication     | Build an API client                                       |
| **33** | LLM API integration, system prompts       | Build a real AI chatbot                                   |
| **34** | Conversation memory, JSON persistence     | Save and retrieve chat history                            |
| **35** | Prompt engineering and roles              | Add Tutor, Friendly and Strict modes                      |
| **36** | Streamlit fundamentals                    | Build a web-based chat interface                          |
| **37** | Sessions and user separation              | Create separate user chat histories                       |
| **38** | PDF processing and extraction             | Upload PDF and extract text                               |
| **39** | Document question answering               | Answer questions using document context                   |
| **40** | Text chunking and retrieval               | Search for relevant document passages                     |
| **41** | RAG fundamentals and integration          | **Project 4: PDF Chatbot**                                |
| **42** | Testing, UI, error handling and security  | Polish the chatbot                                        |

### **Detailed assignments**

**Day 31 — Understand artificial intelligence**

Learn these terms:

- Artificial Intelligence (AI).
- Machine Learning (ML).
- Deep Learning (DL).
- Natural Language Processing (NLP).
- Large Language Models (LLMs).
- Tokens.
- Context window.
- Training versus inference.
- Parameters and neural networks.

Resources:

- YouTube: 3Blue1Brown — Neural Networks.
- YouTube: Andrej Karpathy — Intro to Large Language Models.
- [3Blue1Brown neural networks](https://www.3blue1brown.com/topics/neural-networks?utm_source=chatgpt.com).

Assignment: Write a two-page explanation of how an LLM receives a prompt and generates a response. Build a simple rule-based chatbot to understand the difference between a fixed-response program and an LLM.

**Day 32 — APIs**

Learn:

- HTTP.
- GET and POST.
- Status codes.
- JSON.
- API keys.
- Authentication.

Assignment:

- Create a Python API client.
- Send requests.
- Receive JSON.
- Parse and display the response.

**Day 33 — Your first real AI chatbot**

Choose an LLM provider. For the OpenAI option, use the official developer documentation:

[OpenAI API Developer Quickstart](https://developers.openai.com/api/docs/quickstart?utm_source=chatgpt.com).

Learn:

- API authentication.
- Sending messages.
- Receiving responses.
- System instructions.
- Error handling.

Assignment: Build a terminal chatbot that accepts user questions and returns AI-generated responses.

Important: API usage may incur charges independently of a ChatGPT subscription. Check the provider's pricing before making calls. Never expose your API key in source code.

**Day 34 — Conversation memory**

Learn:

- Conversation history.
- Message roles.
- Context management.
- JSON persistence.

Assignment:

- Store conversations.
- Save history.
- Reload history.
- Continue an earlier session.

**Day 35 — Prompt engineering**

Learn:

- System instructions.
- User instructions.
- Role-based prompting.
- Output formatting.
- Context and constraints.

Create three modes:

1. Tutor mode — explains concepts step by step.
2. Friendly mode — conversational and approachable.
3. Strict mode — concise and focused.

**Day 36 — Streamlit**

Learn:

- Streamlit installation.
- Text input.
- Buttons.
- Session state.
- Chat messages.
- Layout.

Resource: [Official Streamlit documentation](https://docs.streamlit.io/?utm_source=chatgpt.com).

Assignment: Build a browser-based chatbot.

**Day 37 — Sessions**

Learn:

- Session state.
- User identification.
- Conversation separation.
- Data persistence.

Assignment:

- Ask for a username.
- Create individual conversation histories.
- Load the appropriate user's saved history.

For this learning project, simple usernames are fine. They are not secure production authentication.

**Day 38 — PDF processing**

Learn:

- PDF structure.
- Text extraction.
- File upload.
- File validation.

Library: `pypdf`.

Assignment:

- Upload a PDF.
- Extract its text.
- Display a text preview.
- Handle empty and unreadable PDFs.

**Day 39 — Document Q&A**

Learn:

- Context injection.
- Document-grounded answers.
- Text splitting.
- Retrieval basics.

Assignment:

- Split document text into chunks.
- Find relevant passages.
- Send the question and relevant passages to the AI model.
- Ask the model to answer using the supplied context and acknowledge when the document does not contain the answer.

**Day 40 — Better document retrieval**

Learn:

- Chunk size.
- Chunk overlap.
- Keyword matching.
- Ranking.
- Retrieval quality.

Assignment:

- Retrieve the top three relevant text chunks.
- Compare results with a basic full-document approach.
- Test questions whose answers are absent from the document.

**Day 41 — Project 4**

[Chat with your documents! - DocGPT](https://images.openai.com/static-rsc-4/dcSW_GL_t_nkKQBLUhjKP0HcCoS4Y4rGiKJkqh0tHe6QhcI53O-SJX108-LEtosfhQ546CxEL5yRFYbecZ3tXRczRKrIVbAxjnUGoLBl0wYKyefUBlFiTe1WY8WYjBbYIiW1z3d7l3O87yVONmVWVaiHCkC_UprrZkEs0fLIq5o?purpose=inline)

[docgpt.io](https://docgpt.io/?trk=public_post-text\&utm_source=chatgpt.com)

**PDF Chatbot Assistant**

Required features:

- Upload PDF.
- Extract document text.
- Ask questions about the document.
- Retrieve relevant content.
- Generate AI responses.
- Display chat history.
- Handle unsupported and irrelevant questions.

**Technology:** Python, Streamlit, pypdf, LLM API.

Major milestone

**Day 42 — Polish and testing**

- Add loading indicators.
- Add clear error messages.
- Validate file size and file type.
- Handle API failures.
- Add chat clearing.
- Test multiple documents.
- Improve the interface.
- Write a proper README.

**Resources for Phase 4**

| Subject         | Resource                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| LLM concepts    | Andrej Karpathy                                                                                              |
| Neural networks | 3Blue1Brown                                                                                                  |
| AI fundamentals | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course?utm_source=chatgpt.com) |
| LLM development | [Hugging Face Learn](https://huggingface.co/learn?utm_source=chatgpt.com)                                    |
| API integration | [OpenAI developer docs](https://developers.openai.com/api/docs?utm_source=chatgpt.com)                       |
| Web UI          | [Streamlit docs](https://docs.streamlit.io/?utm_source=chatgpt.com)                                          |
| PDF processing  | [pypdf docs](https://pypdf.readthedocs.io/?utm_source=chatgpt.com)                                           |

For now, implement document retrieval with basic keyword matching. You can study embeddings and vector databases in the next programme.