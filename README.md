# AI Research Assistant using LangChain and Gemini 

### Overview

The AI Research Assistant is a Python-based intelligent system that automates the process of researching a topic and generating a structured article. The application gathers information from multiple knowledge sources such as Wikipedia and web search, processes the information using a Large Language Model (Google Gemini), and produces a well-structured research article.

This project demonstrates how LLMs, external tools, and structured outputs can be combined to build intelligent research automation systems.

## Features

- AI-powered research generation

- Web search integration

- Wikipedia knowledge retrieval

- Structured output using Pydantic

- Automatic article generation

- Save research results to a text file

- Clean modular architecture

## Technologies Used
### Python

Python is used as the main programming language for building the application logic and integrating different components.

### LangChain

LangChain is used to build the AI pipeline and connect the language model with external tools.

Key LangChain features used:

- Prompt Templates

- Chains

- Tool Integration

- Output Parsers

### Google Gemini

Google Gemini acts as the Large Language Model responsible for generating research articles from collected information.

Capabilities used:

- Natural language understanding

- Content generation

- Structured responses

### Pydantic

Pydantic is used to define the structured schema for AI responses, ensuring consistent and validated outputs.

Example structured output fields:

- Title

- Article

- Sources

- Tools Used

### DuckDuckGo Search

Used to retrieve real-time web information relevant to the research topic.

### Wikipedia API

Used to obtain reliable background information about the topic.

### python-dotenv

Used to securely manage API keys and environment variables.

## Project Architecture

User Query 

   ⬇️

Search Tools (Wikipedia + Web Search)

LangChain Processing
    ↓
Gemini LLM Analysis
    ↓
Structured Output Generation
    ↓
Save Research Article to File

## Installation
1 Clone the repository
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant
2 Create a virtual environment
python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3 Install dependencies
pip install -r requirements.txt

Example requirements:

langchain
langchain-community
langchain-openai
langchain-anthropic
langchain-google-genai
pydantic
python-dotenv
duckduckgo-search
wikipedia
ddgs
4 Add API Key

Create a .env file in the project root.

GOOGLE_API_KEY=your_google_gemini_api_key
Running the Project

Run the application using:

python main.py

Example input:

What can I help you research?
cricket
Example Output

The system generates structured research articles such as:

Title: Cricket: A Bat-and-Ball Game

Article:
Cricket is a popular bat-and-ball sport played between two teams...
...

Sources:
- Wikipedia
- Web Search

Tools Used:
- Wikipedia Search
- Web Search

The output is also saved automatically to:

research_output.txt
Project Structure
AI-Research-Assistant
│
├── main.py              # Main application
├── tools.py             # Tool definitions (search, wikipedia, save)
├── research_output.txt  # Generated research articles
├── requirements.txt     # Project dependencies
├── .env                 # API keys
└── README.md            # Project documentation
Skills Learned From This Project
AI Development

Prompt engineering

Tool-augmented LLM systems

Structured output generation

AI workflow pipelines

Software Engineering

Modular architecture

API integration

Environment configuration

Error handling

LangChain Concepts

Chains

Prompt Templates

Output Parsers

Tool integration

Future Improvements
Multi-Step AI Research

Allow the AI to perform deeper research using multiple reasoning steps.

Citation System

Automatically generate academic-style citations.

Web Interface

Build a UI using:

Streamlit

React

Flask or FastAPI

Export Options

Allow exporting research reports as:

PDF

Word

Markdown

Knowledge Database

Store previous research results in a database for faster retrieval.

Possible Industry-Level Extensions

This project can be extended into larger AI systems such as:

AI Research Platform

Automated research assistant for students, analysts, and researchers.

AI Market Intelligence Tool

Automatically gather and analyze market trends and industry data.

Enterprise Knowledge Assistant

AI-powered internal documentation search tool for companies.

AI Content Generation System

Generate blogs, reports, and articles based on verified sources.

Author

Shashidhar
Master's in Computer Science
Saint Louis University

If you want, I can also help you add:

GitHub badges

architecture diagram

project screenshots

a workflow diagram

to make your README look like a top AI GitHub project.
