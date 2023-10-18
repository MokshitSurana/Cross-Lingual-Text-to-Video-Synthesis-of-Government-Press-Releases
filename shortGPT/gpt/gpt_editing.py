from shortGPT.gpt import gpt_utils
import json, re
def getImageQueryPairs(captions, n=10, maxTime=3):
    prompt = "### Instructions:\nRespond in the format of a Python dict with timestamp to query format like { 1.0: 'happy person', 3.2: 'sad person' }. DON'T GENERATE A QUERY FOR EACH CAPTION. You are a tiktok video editor. You take the transcript of your short and put a very simple google image to illustrate the narrated sentances. If the transcript contains a proper noun such as a name, then you MUST include it in the Python dict.\nIf the picture is of a role such as 'President of India', then you must include the name of the person in that role right now. Example: 'President of India Droupadi Murmu', 'President Droupadi Murmu giving speech'\nI will give you a transcript which contains which words are shown at the screen, and the timestamps where they are shown. Understand the transcript, and time images at timestamps and, write me the query for each image. Generate generate many image queries to last the whole duration of the video.\n DO NOT depicting shocking or nude / crude images. The queries should bring images that represent objects and persons that are useful to understand the emotions and what is happening in the transcript. The queries should describe OBJECTS or PERSONS. Use names places and real life people that are mentioned as image queries. Avoid using overly generic queries like 'smiling man', use the word 'person instead'. Instead, try to use more specific words that describe the action or emotion in the scene. Also, try to avoid queries that don't represent anything in images, such as abstract concepts, ideas, or feelings. MAKE SURE THAT THE QUERIES ARE VERY DESCRIPTIVE AND VISUAL AND CAN BE DRAWN AND NEVER USE WORDS THAT ONLY DESCRIBE AN ABSTRACT IDEA. NEVER USE ABSTRACT NOUNS IN THE QUERIES. ALWAYS USE REAL OBJECTS OR PERSONS IN THE QUERIES.\nTranscript:\n{captions}\nEvery 3 transcript captions, find an image that can be shown. Really understand the context and emotions for the image to be good! The queries should describe OBJECTS or PERSONS. Generate many image queries and time them accordingly in the video length. NEVER use the same search query for multiple captions. Make sure that the timestamps make sense.\n NEVER USE ABSTRACT NOUNS IN THE QUERIES. ALWAYS USE REAL OBJECTS OR PERSONS IN THE QUERIES."#\n\n### Response:\n{"
    prompt = prompt.replace("{captions}",str(captions))#.replace("{n}",str(n))
    #res = gpt_utils.llama_completion(chat_prompt=prompt, temp= 0.75, max_tokens=1024)
    res = "{ 0.9: 'President of India', 2.36: 'National Awards', 4.34: 'importance of elementary education', 6.38: 'holistic approach', 9.68: 'female teachers in india', 11.7: 'teacher teaching in class', 14.4: 'children are future of the nation', 16.2: 'teachers and parents india, 19.24: 'teachers teaching students', }"
    res = re.findall(r'{([^}]*)}', res)[-1]
    # combined = {}
    # for i in range(len(captions)-1):
    #     start = captions[i][0][0]
    #     text = captions[i][1] + " " + captions[i+1][1]
    #     combined[start] = text

    # print(combined)
    # res=str(combined)
    imagesCouples = ('{'+res).replace('{','').replace('}','').replace('\n', '').split(',')
    pairs = []
    t0 = 0
    end_audio = captions[-1][0][1]
    for a in imagesCouples:
        try:
            query = a[a.find("'")+1:a.rfind("'")]
            time = float(a.split(":")[0].replace(' ',''))
            if (time > t0 and time< end_audio):
                pairs.append((time, query))
                t0 = time
        except:
            print('problem extracting image queries from ', a)
    for i in range(len(pairs)):
        if(i!= len(pairs)-1):
            end = pairs[i][0]+ maxTime if (pairs[i+1][0] - pairs[i][0]) > maxTime else pairs[i+1][0]
        else:
            end = pairs[i][0]+ maxTime if (end_audio - pairs[i][0]) > maxTime else end_audio
        pairs[i] = ((pairs[i][0], end), pairs[i][1])
    # print(pairs)
    # print(pairs[-1][0][0])
    return pairs


def getVideoSearchQueriesTimed(captions_timed):
    end = captions_timed[-1][0][1]
    # chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/editing_generate_videos.yaml')
    # chat = chat.replace("<<TIMED_CAPTIONS>>", f"{captions_timed}")
    prompt = """<s>[INST] <<SYS>>
You're a video research expert. The user will give you the timed captions of a video they will make, and you will give back a list of couples of text search queries that will be used to search for background video footage, and the time t1 and t2 when it will be shown in the video.
# Output format
Then is an example of a valid output format, You must make a similar JSON object with the Timed captions given below.
{"Video search queries": [[[0.0, 4.4],["software engineer", "coding", "laptop"]],[[4.4, 8.8],["coffee mug", "desk", "workspace"]],[[8.8, 13.2],["video conference", "team meeting", "laptop"]],[[13.2, 17.6],["bug fixes", "testing", "code"]],[[17.6, 22],["reflection", "accomplishment", "success"]]]

# Time periods t1 and t2
Time periods t1 and t2 must always be consecutive, and last between 4 to 5 seconds, and must cover the whole video.
For example, [0, 2.5] <= IS BAD, because 2.5-0 = 2.5 < 3
[0, 11] <= IS BAD, because 11sec > 5 sec
[0, 4.2] <= IS GOOD

# Query search string list
YOU ALWAYS USE ENGLISH IN YOUR TEXT QUERIES
As you have seen above, for each time period you will be tasked to generate 3 strings that will be searched on the video search engine, to find the appropriate clip to find.
Each string has to be between ONE to TWO words.
Each search string must DEPICT something visual.
The depictions have to be extremely visually concrete, like `coffee beans`, or `dog running`.
'confused feelings' <= BAD, because it doesn't depict something visually
'heartbroken man' <= GOOD, because it depicts something visual. 
The list must always contain 3 query searches.
<</SYS>>
Timed captions: {captions_timed} [/INST] {"Video search queries:": [[[0, """
    prompt= prompt.replace("{captions_timed}", str(captions_timed))
    out = [[[0,0],""]]
    while out[-1][0][1] != end:
        try:
            print("End",end)
            response = gpt_utils.llama_completion(chat_prompt=prompt, temp=0.7, max_tokens=2048, stop=[']]]','}','###','</s>']).replace("'", '"')
            #print(response)
            out = json.loads('{"Video search queries": [[[0, '+response+"]]]}")
            out = out['Video search queries']
            print("FINAL", out)
            out[-1][0][1] = end
        except Exception as e:
            print(e)
            print("not the right format")
    return out