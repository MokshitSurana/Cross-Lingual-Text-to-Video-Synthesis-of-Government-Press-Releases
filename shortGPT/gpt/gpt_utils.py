import json
import os
import re
from time import sleep, time

import requests
import tiktoken
import yaml

from shortGPT.config.api_db import ApiKeyManager
import asyncio, json
#from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import copy
# from langchain.llms import LlamaCpp
# from langchain import PromptTemplate, LLMChain
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# llm = LlamaCpp(
#     model_path="/home/siddharth/llama/models/llama-2-13b.ggmlv3.q5_1.bin",
#     temperature=0.75,
#     max_tokens=2000,
#     top_p=1,
#     callback_manager=callback_manager, 
#     verbose=True, 
#     n_ctx=3008,
#     n_gpu_layers=20# Verbose is required to pass to the callback manager
# )

def num_tokens_from_messages(texts, model="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
        if isinstance(texts, str):
            texts = [texts]
        score = 0
        for text in texts:
            score += 4 + len(encoding.encode(text))
        return score
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
        See https://github.com/openai/openai-python/blob/main/chatml.md for information""")


def extract_biggest_json(string):
    json_regex = r"\{(?:[^{}]|(?R))*\}"
    json_objects = re.findall(json_regex, string)
    if json_objects:
        return max(json_objects, key=len)
    return None


def get_first_number(string):
    pattern = r'\b(0|[1-9]|10)\b'
    match = re.search(pattern, string)
    if match:
        return int(match.group())
    else:
        return None


def load_yaml_file(file_path: str) -> dict:
    """Reads and returns the contents of a YAML file as dictionary"""
    return yaml.safe_load(open_file(file_path))


def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

from pathlib import Path

def load_local_yaml_prompt(file_path):
    _here = Path(__file__).parent
    _absolute_path = (_here / '..' / file_path).resolve()
    json_template = load_yaml_file(str(_absolute_path))
    return json_template['chat_prompt'], json_template['system_prompt']


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def get_stream(url, json):
    s = requests.Session()

    with s.post(url, json=json, stream=True) as resp:
        for line in resp.iter_lines():
            if line:
                print(line)

async def main(prompt):
    cookies = json.loads(open("./bing_cookies_*.json", encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.balanced, simplify_response=True)
    response = copy.copy(response['text'])
    await bot.close()
    #response = json.dumps(response, indent=2)
    return response


def llama_completion(chat_prompt="", system="You are an AI that can give the answer to anything", temp=0.7, stop=['}','###','</s>'], model="gpt-3.5-turbo", max_tokens=1000, remove_nl=True):
    max_retry = 5
    retry = 0
    while True:
        try:
            #text = asyncio.run(main(chat_prompt))
            response = requests.post("https://gpt.sidd065.repl.co/", json={"message":chat_prompt}).json()
            text=response['text']
            print(text)
            # finish_reason = 'length'
            # #while finish_reason == 'length':
            # response = requests.post("http://localhost:8000/v1/completions", json={
            #     "prompt":chat_prompt,
            #     "max_tokens":max_tokens,
            #     "temperature":temp,
            #     "stop":stop,
            # }).json()
            # text = response['choices'][0]['text'].strip()
            # finish_reason = response['choices'][0]['finish_reason']
            # print(text, finish_reason)
            # # print(text)
            if remove_nl:
                text = re.sub('\s+', ' ', text)
            filename = '%s_llm.txt' % time()
            if not os.path.exists('.logs/gpt_logs'):
                os.makedirs('.logs/gpt_logs')
            with open('.logs/gpt_logs/%s' % filename, 'w', encoding='utf-8') as outfile:
                outfile.write(f"System prompt: ===\n{system}\n===\n"+f"Chat prompt: ===\n{chat_prompt}\n===\n" + f'RESPONSE:\n====\n{text}\n===\n')
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                raise Exception("LLM error: %s" % oops)
            print('Error communicating with LLM:', oops)
            sleep(1)