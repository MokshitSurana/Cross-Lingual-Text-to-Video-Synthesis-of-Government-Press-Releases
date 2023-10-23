import webvtt

def parse_webvtt(file_path):
    captions = []
    for caption in webvtt.read(file_path):
        start_time = caption.start
        end_time = caption.end
        text = caption.text.strip()
        captions.append(((start_time, end_time), text))
    
    return captions

file_path = './captions.vtt'
parsed_captions = parse_webvtt(file_path)

print(parsed_captions)
