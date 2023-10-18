from shortGPT.gpt import gpt_utils
import json, re, sys
def generateScript(article, language):
    print(language)
    out = {'text': ''}
    
    #chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/chat_video_script.yaml')
    #chat = chat.replace("<<DESCRIPTION>>", script_description).replace("<<LANGUAGE>>", language)
    prompt = '\n\n### Instructions:\n  Your output must be less than 150 words. You are an expert video writer. You ONLY produce text that is read. You only produce the very short script that is 150 words long. It must have short sentences. If a sentence is long beak it up with commas. The script will be read by a voice actor for a video. Make sure the text is not longer than 150 words. The user will give you the contents of a new article, you will write the script. Make sure to directly write the script in response to the given article.\n Your script will not have any reference to the audio footage / video footage shown. Only the text that will be narrated by the voice actor.\n You will produce purely text. No emojis or hashtags.\n# Output:\nYou will output the script in a JSON format of this kind, and only a parsable JSON object\n{"text": "[SCRIPT HERE]"}\n# Article:\n{article}'#\n\n### Response:\n{"script": "'
    prompt = prompt.replace("{article}", article)
    #while not ('text' in out and out['text']):
    if True:
        try:
            result = gpt_utils.llama_completion(chat_prompt=prompt, temp=0.3, max_tokens=200)
            #if not result.endswith('"'): result+='"'
            #out = json.loads('{"text": "'+result+"}")
            matches = re.findall(r'"([^"]*)"', result)
            #out = json.loads('{}')
            print("\nSCRIPT:",matches[-1])
            
        except Exception as e:
            print(e, "Difficulty parsing the output in gpt_chat_video.generateScript")
            
    return matches[-1]

from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import PegasusForConditionalGeneration, AutoTokenizer

from transformers import pipeline
import torch
import base64

tokenizer = T5Tokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-248M")
base_model = T5ForConditionalGeneration.from_pretrained("MBZUAI/LaMini-Flan-T5-248M", device_map='auto', torch_dtype=torch.float32)

def summerize(input_text, max_length=512, min_length=50):
    # model_name = 'google/pegasus-cnn_dailymail'
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    # model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
    # batch = tokenizer(input_text, truncation=True, padding='longest', return_tensors="pt").to(device)
    # translated = model.generate(**batch)
    # tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    # print("Summary:", tgt_text)
    # return tgt_text[0]

    pipe_sum = pipeline(
        'summarization',
        model = base_model,
        tokenizer = tokenizer,
        max_length = max_length, 
        min_length = min_length)
    result = pipe_sum(input_text)
    result = result[0]['summary_text']
    return result

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('punkt')
# nltk.download('stopwords')

def extract_keywords(text):
    words = nltk.word_tokenize(text)

    words = [word for word in words if len(word) > 1]

    words = [word for word in words if not word.isnumeric()]

    words = [word.lower() for word in words]

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    fdist = nltk.FreqDist(words)

    output=[]
    for word, frequency in fdist.most_common(4):
        #print(u'{};{}'.format(word, frequency))
        output.append(word)
    return ' '.join(output)

def correctScript(script, correction):
    out = {'script': ''}
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/chat_video_edit_script.yaml')
    chat = chat.replace("<<ORIGINAL_SCRIPT>>", script).replace("<<CORRECTIONS>>", correction)

    while not ('script' in out and out['script']):
        try:
            result = gpt_utils.llama_completion(chat_prompt=chat, system=system, temp=1)
            out = json.loads(result)
        except Exception as e:
            print("Difficulty parsing the output in gpt_chat_video.generateScript")
    return out['script']