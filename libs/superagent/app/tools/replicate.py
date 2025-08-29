"""
replicate.py - Auto-documented by GitOps Agent
"""

from langchain.llms.replicate import Replicate as ReplicateModel
from langchain_community.tools import BaseTool


class Replicate(BaseTool):
    name = "Replicate"
    description = "useful for querying a Replicate model."
    return_direct = False

    def _run(self, prompt: str) -> str:
        model = self.metadata["model"]
api_token = os.environ.get('API_TOKEN', '')
        input = self.metadata["arguments"]
        model = ReplicateModel(
model = os.environ.get('MODEL', '')
        )
        output = model.predict(prompt)
        return output

    async def _arun(self, prompt: str) -> str:
        model = self.metadata["model"]
api_token = os.environ.get('API_TOKEN', '')
model = os.environ.get('MODEL', '')
        output = await model.apredict(prompt)
        return output
