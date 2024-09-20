from typing import List
from langchain.agents import Tool
from langchain.prompts import BaseChatPromptTemplate
from langchain.schema import HumanMessage

# Prompt Template
TEMPLATE = '''Your task is to answer the below question/inquiry as best concise you can. You have access to the following tools:

{tools}

Use the tools if you can not get to the answer by yourself! You can call different tools consecutively and always observe the output of an action that you execute! They might not be necessary to deduct the final answer. 
Strictly follow the following syntax:

Question: <the input question you must answer>
Thought: <you should always think about what to do>
Action: <exclusively the tool to use, should be one of [{tool_names}]>
Action Input: <exclusively the input to the tool>
Observation: <the result of the tool>
... (this Thought/Action/Action Input/Observation can repeat N times. Always observe the response after an Action.)
Thought: "I now know the final answer"
Final Answer: <the final answer to the original input question>

Begin!

Question: {input}
Thought: {agent_scratchpad}'''



class CustomPromptTemplate(BaseChatPromptTemplate):
    # The template to use
    template: str
    # The list of tools available
    tools: List[Tool]
    
    def format_messages(self, **kwargs) -> str:
        # Get the intermediate steps (AgentAction, Observation tuples)
        
        # Format them in a particular way
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        # The 'observation' is the unchanged output of the previously executed tool
        for action, observation in intermediate_steps:
            thoughts += action.log
            thoughts += f"\nObservation: {observation}\nThought: "
            
        # Set the agent_scratchpad variable to that value
        kwargs["agent_scratchpad"] = thoughts
        # print("Thoughts: ", thoughts)
                
        # Create a tools variable from the list of tools provided
        kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])
        
        # Create a list of tool names for the tools provided
        kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
        formatted = self.template.format(**kwargs)
        return [HumanMessage(content=formatted)]