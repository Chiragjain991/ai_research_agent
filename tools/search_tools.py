from typing import List

def clean_search_results(results: List[dict]) -> str:
    """
    Clean and format google_search results into readable text.
    """
    formatted = ""

    for result in results:
        title = result.get("title", "")
        snippet = result.get("snippet", "")

        formatted += f"Title: {title}\n"
        formatted += f"Snippet: {snippet}\n\n"

    return formatted