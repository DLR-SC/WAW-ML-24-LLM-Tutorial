import re
from typing import Union
from langchain.agents import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish

class CustomOutputParser(AgentOutputParser):
    
    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        """
        This function parses the output of a Language Model. Specifically, it extracts
        the Action (i.e. the name of the tool to be executed) as well as the ActionInput (i.e. the input to
        this tool). If the LLM response contains the string "Final Answer:", then the function
        assumes that the LLM wants to return a final response to the user and returns an object
        of type AgentFinish. If the response contains  no string "Final Answer:", then the function
        attempts to extract the tool and tool input and returns a respective AgentAction, which will
        eventually call the tool.

        Parameters:
        llm_output (str): The output straight from the Language Model

        Returns:
        Union[AgentAction, AgentFinish]: AgentAction or AgentFinish, depending on `llm_output`
        """

        # Check if agent should finish
        llm_output = llm_output.strip()
        if "Final Answer:" in llm_output:
            return AgentFinish(
                # Return values is generally always a dictionary with a single `output` key
                # It is not recommended to try anything else at the moment :)
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        if "I now know the final answer:" in llm_output:
            return AgentFinish(
                # Return values is generally always a dictionary with a single `output` key
                # It is not recommended to try anything else at the moment :)
                return_values={"output": llm_output.split("I now know the final answer")[-1].strip()},
                log=llm_output,
            )
        
        # Parse out the action and action input
        regex = r"Action: (.*?)[\n]*Action Input:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        
        # If it can't parse the output it raises an error
        # You can add your own logic here to handle errors in a different way i.e. pass to a human, give a canned response
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        
        # Return the action and action input
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)
    