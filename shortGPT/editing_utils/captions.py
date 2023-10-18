import re, string

def getSpeechBlocks(whispered, silence_time=2):
    text_blocks, (st, et, txt) = [], (0,0,"")
    for i, seg in enumerate(whispered['segments']):
        if seg['start'] - et > silence_time:
            if txt: text_blocks.append([[st, et], txt])
            (st, et, txt) = (seg['start'], seg['end'], seg['text'])
        else: 
            et, txt = seg['end'], txt + seg['text']

    if txt: text_blocks.append([[st, et], txt]) # For last text block

    return text_blocks

def cleanWord(word):
    return re.sub(r'[^\w\s\-_"\'\']', '', word)

def interpolateTimeFromDict(word_position, d):
    for key, value in d.items():
        if key[0] <= word_position <= key[1]:
            return value
    return None

def getTimestampMapping(whisper_analysis):
    index = 0
    locationToTimestamp = {}
    for segment in whisper_analysis['segments']:
        for word in segment['words']:
            newIndex = index + len(word['text'])+1
            locationToTimestamp[(index, newIndex)] = word['end']
            index = newIndex
    return locationToTimestamp


def splitWordsBySize(words, maxCaptionSize):
    halfCaptionSize = maxCaptionSize / 2
    captions = []
    while words:
        caption = words[0]
        words = words[1:]
        while words and len(caption + ' ' + words[0]) <= maxCaptionSize:
            caption += ' ' + words[0]
            words = words[1:]
            if len(caption) >= halfCaptionSize and words:
                break
        captions.append(caption)
    return captions

def getCaptionsWithTime(whisper_analysis, maxCaptionSize=15, considerPunctuation=False):
    wordLocationToTime = getTimestampMapping(whisper_analysis)
    position = 0
    start_time = 0
    CaptionsPairs = []
    text = whisper_analysis['text']
    
    if considerPunctuation:
        sentences = re.split(r'(?<=[.!?]) +', text)
        words = [word for sentence in sentences for word in splitWordsBySize(sentence.split(), maxCaptionSize)]
    else:
        words = text.split()
        words = [cleanWord(word) for word in splitWordsBySize(words, maxCaptionSize)]
    
    for word in words:
        position += len(word) + 1
        end_time = interpolateTimeFromDict(position, wordLocationToTime)
        if end_time and word:
            CaptionsPairs.append(((start_time, end_time), word))
            start_time = end_time

    return CaptionsPairs

def replaceWithScript(_script, CaptionPairs):
    script = _script.translate(str.maketrans('', '', string.punctuation))
    script = script.split()
    print(CaptionPairs)
    newCaptionPairs = []
    for i in range(len(CaptionPairs)):
        wordCount = CaptionPairs[i][1].count(' ')+1
        if len(script[:wordCount]):
            if i+1 == len(CaptionPairs):
                newCaptionPairs.append((CaptionPairs[i][0], ' '.join(script)))
            else:
                newCaptionPairs.append((CaptionPairs[i][0], ' '.join(script[:wordCount])))
        #print(script[:wordCount])
        script = script[wordCount:]
    print(newCaptionPairs)
    return newCaptionPairs

def adjust_timing(timed_image_urls, init_length, new_length):
    ratio = init_length/new_length
    new_timed_image_urls=[]
    for ele in timed_image_urls:
        start = round(ele[0][0]/ratio,2)
        end = round(ele[0][1]/ratio,2)
        new_timed_image_urls.append(((start,end),ele[1]))
    return new_timed_image_urls