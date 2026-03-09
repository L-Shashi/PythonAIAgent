from dotenv import load_dotenv
from pydantic import BaseModel, Field
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    title: str = Field(description="Title of the article")
    article: str = Field(description="A complete article about the topic")
    sources: list[str] = Field(description="References used")
    tools_used: list[str] = Field(description="Tools used")


#llm1 = ChatOpenAI(model="gpt-4o-mini")
#llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")  

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a research assistant.
Use the provided Wikipedia result and web search result to answer the user's query.

Return the response in the required structured format.
Also write the 'article' field as a clear, well-organized article with an introduction, body, and conclusion.
Write the article in clean readable paragraphs.
Do not use markdown headings unless asked.

{format_instructions}
"""
        ),
        (
            "human",
            """
User query:
{query}

Wikipedia result:
{wiki_result}

Web search result:
{search_result}
"""
        ),
    ]
).partial(format_instructions=parser.get_format_instructions())


#tools = [search_tool]
# agent = create_tool_calling_agent(
#     llm = llm,
#     prompt = prompt,
#     tools = []
# )

# agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)

chain = prompt | llm | parser
query = input("what can i help you research? \n")

wiki_result = wiki_tool.invoke(query)
search_result = search_tool.invoke(f"{query} latest findings")

raw_response = chain.invoke({
    "query": query,
    "wiki_result": wiki_result,
    "search_result": search_result,
})

#print(raw_response)

# structured_response = parser.parse(raw_response.get("output")[0]["text"])
# print(structured_response)

print(raw_response.model_dump_json(indent=2))

try:
    save_result = save_tool.invoke(raw_response.model_dump_json(indent=2))
    print(save_result)
except Exception as e:
    print("Error parsing response:", e, "Raw Response - ", raw_response)