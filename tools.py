from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

from langchain.tools import tool
from datetime import datetime


@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves structured research data to a text file.
    """

    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

search = DuckDuckGoSearchRun()
@tool
def search_tool(query: str) -> str:
    """Search the web for information."""
    return search.run(query)

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100))
@tool
def wiki_tool(query: str) -> str:
    """Search Wikipedia for factual information."""
    return wiki.run(query)