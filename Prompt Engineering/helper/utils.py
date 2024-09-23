import re
from langchain.llms import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

import torch


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def text_blue(text):
    return bcolors.OKBLUE + str(text) + bcolors.ENDC
def text_cyan(text):
    return bcolors.OKCYAN + str(text) + bcolors.ENDC
def text_green(text):
    return bcolors.OKGREEN + str(text) + bcolors.ENDC
def text_red(text):
    return bcolors.FAIL + str(text) + bcolors.ENDC
def text_bold(text):
    return bcolors.BOLD + str(text) + bcolors.ENDC
def text_underline(text):
    return bcolors.UNDERLINE + str(text) + bcolors.ENDC

def remove_non_ascii_and_newline(string:str) -> str:
    string = re.sub(r'[^\x00-\x7F]', '', string)
    string = re.sub(r'[\n\r]', '', string)
    return string



def get_llama2_model(
    model_name: str = "meta-llama/Llama-2-7b-chat-hf", temperature: float = 0.0
):  # this is the  model used by IESTA
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        max_new_tokens=2048,
        do_sample=True,
        top_k=30,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )

    model = HuggingFacePipeline(
        pipeline=pipe, model_kwargs={"temperature": temperature}
    )
    return model
