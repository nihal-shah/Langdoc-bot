import os 
from langchain_tavily import TavilyCrawl
from dotenv import load_dotenv
import json
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

TAVILY_CRAWLER = TavilyCrawl()

target_url = "https://en.wikipedia.org/wiki/Main_Page"

result = TAVILY_CRAWLER.invoke({
    "url": target_url,
    "max_depth": 1,
    "extract_depth": "advanced"
})

with open ("output.json", "w") as f:
    json.dump(result, f, indent=4)