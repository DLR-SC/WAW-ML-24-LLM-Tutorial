from datetime import datetime
from langchain.agents import Tool
from typing import List, Optional, Callable
from utils import text_red, text_underline, remove_non_ascii_and_newline
import smtplib
import re
import ast

# E-Mail Setup
SERVER = smtplib.SMTP("smtprelay.dlr.de")
FROM_MAIL = "<email>"
DISCLAIMER = "\n\n---\nDisclaimer: This is an automated e-mail sent by a Language Model."


class ToolManager:
    def __init__(self):
        self.tools = dict()
        self._make_tools()
    
    def _make_tools(self) -> None:
        """
        Creates all tools available to the agent.
        """
        # TOOL - Get the current date and time
        def get_current_datetime(input:str=None):
            print()
            print(text_underline(text_red(f" > Tool 'get_current_datetime' was called with input '{input}")))
            now = datetime.now()
            return now.strftime("%A, %B %d, %Y at %I:%M %p")
        self.tools["Current Datetime"] = {
            "func": get_current_datetime,
            "description": "Returns the current date and time."
        }

        # TOOL - Get an email adress by the persons name
        def find_email_address(person:str) -> str:
            person = person.strip()
            firstname, lastname = ast.literal_eval(person)
            print()
            print(text_underline(text_red(f" > Tool 'find_email_address' was called with input '{person}")))
            return f"The e-mail adress of {firstname} {lastname} is: {firstname.lower()}.{lastname.lower()}@dlr.de"
        self.tools["Find Email"] = {
            "func": find_email_address,
            "description": "Returns the E-Mail adress for a person. Input: a tuple of two strings in the following format: (<firstname>, <lastname>)"
        }

        # TOOL - Send email within DLR
        def send_mail(data:tuple) -> str:
            print()
            print(text_underline(text_red(f" > Tool 'send_mail' was called with input '{data}'")))
           
            # Clean input
            email, subject, message = ast.literal_eval(data)
            subject = remove_non_ascii_and_newline(subject)
            message = remove_non_ascii_and_newline(message)

            # Compose and Send E-Mail
            try:
                msg = f"Subject: {subject}\n\n{message}{DISCLAIMER}"
                SERVER.sendmail(FROM_MAIL, email, msg)
                SERVER.quit()
                return f"E-Mail successfully sent to {email}!"
            except Exception as e:
                return f"Could not send E-Mail to {email} due to the following error: {e}"
        self.tools["Send Mail"] = {
            "func": send_mail,
            "description": "Sends an E-Mail to another person. Input: A tuple of strings in the following format: (<email>, <subject>, <message>)"
        }


    def get_tools(self) -> list[Tool]:
        """
        Returns a list of all available Tools.
        """
        tools = list()
        for tool_name in self.tools.keys():
            t:dict = self.tools[tool_name]
            tool = Tool(
                name=tool_name,
                func=t['func'],
                description=t['description']
            )
            tools.append(tool)
        return tools