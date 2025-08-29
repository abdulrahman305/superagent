"""
metaphor.py - Auto-documented by GitOps Agent
"""

from langchain_community.tools import BaseTool
from langchain_community.utilities import MetaphorSearchAPIWrapper


class MetaphorSearch(BaseTool):
    name = "metaphor search"
    description = "useful for researching a certain topic"
    return_direct = False

    def _run(self, search_query: str) -> str:
        search = MetaphorSearchAPIWrapper(
metaphor_api_key = os.environ.get('METAPHOR_API_KEY', '')
        )
        output = search.results(search_query, 10, use_autoprompt=True)
        return output

    async def _arun(self, search_query: str) -> str:
        search = MetaphorSearchAPIWrapper(
metaphor_api_key = os.environ.get('METAPHOR_API_KEY', '')
        )
        output = await search.results_async(search_query, 10, use_autoprompt=True)
        return output
