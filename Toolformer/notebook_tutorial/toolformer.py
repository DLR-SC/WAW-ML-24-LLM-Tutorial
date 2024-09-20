from InferenceLLM import InferenceLLM
from ToolManager import ToolManager
from langchain.agents import AgentExecutor, LLMSingleActionAgent
from langchain.chains import LLMChain
from CustomPromptTemplate import CustomPromptTemplate, TEMPLATE
from CustomOutputParser import CustomOutputParser
from utils import text_blue, text_cyan, text_bold, text_green, text_underline


class Toolformer:
    def __init__(self, tools):
        self.tools = tools

    def run(self, input:str):
        # Define LLM - responsible for generating text
        llm = InferenceLLM()

        # Define tools available to the LLM
        tool_manager = ToolManager()
        available_tools = self.tools
        print(text_bold(text_underline("Available Tools:")))
        for tool in available_tools:
            print(tool)
            print()
        print()
        print()

        # Define PromptTemplate - responsible for crafting any prompt to the LLM using a template
        prompt = CustomPromptTemplate(
            template=TEMPLATE,
            tools=available_tools,
            input_variables=["input", "intermediate_steps"]
        )

        # Define Chain
        llm_chain = LLMChain(llm=llm, prompt=prompt)

        # Define OutputParser - responsible for extracting tool names and tool inputs from a LLM response
        output_parser = CustomOutputParser()

        # Define Agent and AgentExecutor - responsible for coordinating all the functionality
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            output_parser=output_parser,
            stop=["Observation:", "Observations:", "Output:", "Outputs"],
            allowed_tools=available_tools
        )
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=available_tools, verbose=True)

        #input = "What's tomorrow's date?" # works fine
        #input = "Tell me the E-Mail adress of Dominik Opitz."
        #input = "Send an email to Dominik Opitz and greet him from our event today: the WAW ML Tutrial on Toolformers!" # should work
        response = agent_executor.run(input)

        print()
        print("Response: ", response)