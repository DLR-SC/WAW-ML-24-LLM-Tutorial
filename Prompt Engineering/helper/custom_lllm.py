from openai import OpenAI
from langchain_core.language_models.llms import LLM
from typing import List, Optional
from .utils import text_cyan, text_bold, text_underline

# MODEL = "TheBloke/phi-2-GGUF"
MODEL = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
BASE_URL = "http://localhost:1234/v1"
API_KEY = "lm-studio"


class CustomLLM(LLM):

    client: OpenAI = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Point to the local server
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        # run_manager: Optional[CallbackManagerForLLMRun] = None,
        #chatbot=None,
    ) -> str:
        if self.verbose:
            print()
            print(text_bold(text_underline("Inferencing LLM with following prompt:")))
            print(text_cyan(prompt))
            print()
        completion = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                { "role": "user", "content": prompt }
            ],
            stop=stop,
            seed=1
        )
        response_text = completion.choices[0].message.content
        return response_text
