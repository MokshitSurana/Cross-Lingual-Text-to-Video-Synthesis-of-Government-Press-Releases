import requests, tiktoken, re, time

def get_llm(prompt):
    try:
        response = requests.post("http://localhost:8000/v1/completions", 
        json={
                "prompt": f"[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.\n<</SYS>>\n{prompt}[/INST] Sure I'd be happy to help! Here is the requested array [",
                "stop": [
                    "]",
                    "###"
                ],
                "temperature":0,
                "max_tokens":512
            }).json()
        response = response['choices'][0]['text']
    except Exception as e:
        print('LOCAL:',str(e))
        response = requests.post("https://gpt.sidd065.repl.co", json={"message":prompt}).json()
        response = response['text']
    
    
    print(response)
    response = response.replace('President','President Droupadi Murmu')
    if '1. ' in response:
        response = response.replace('"','').replace('\'','')
        response = re.findall(r'\d+\.\s(.*)', response)
    else:
        response = response[response.find('[')+1:response.find(']')]
        response = response.replace('\n','').replace('[','').replace(']','').replace('"','').replace('\'','')
        response= response.split(',')
    response = [ele.strip() for ele in response]
    return response

def num_tokens_from_messages(texts, model="gpt-3.5-turbo-0301"):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if isinstance(texts, str):
        texts = [texts]
    score = 0
    for text in texts:
        score += 4 + len(encoding.encode(text))
    return score

def image_queries(sentences, max_retries=5):
    len_sentences = len(sentences)
    sentences = str(sentences).replace('"', '\'')
    image_prompt = f"{sentences}\nThis is an array of sentences from a news article. You must respond in the format of an array that contains search queries to find images that are relevant to the article for each sentence in the array given above. Search queries MUST be relevant to what is in the sentence and the article in general. Write an array containing search queries. Each element must be a string that is a search query for an image. The first element must be a search query for an image that is relevant to the first sentence in the array given above. The second element must be a search query for an image that is relevant to the second sentence in the array given above. The third element must be a search query for an image that is relevant to the third sentence in the array given above and so on."    #image_prompt = image_prompt.format(sentences = sentences)
    response = []
    while len(response)<len_sentences:
        response = get_llm(image_prompt)
        if len(response)<len_sentences:
            max_retries-=1
            if max_retries==0:
                break
            time.sleep(3)
            print('Retrying... RESPONSE:',response)            

    print(response)
    return response[0:len_sentences]

def make_script(article, max_retries=5):
    return article

def get_keywords(article, max_retries=5):
    prompt = f"You must respond in the format of an array that contains keywords. Each element must be an important keyword mentioned in the news article below.\n\nArticle:\n{article}"
    response = get_llm(prompt)
    response = ' '.join(response[0:3])
    print(response)
    return response
