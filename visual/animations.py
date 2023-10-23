from moviepy.editor import ImageClip
import smartcrop
from PIL import Image

import cv2
import numpy as np

def crossfade_in(image, duration, resolution, crossfade=0.5):
    return ImageClip(image).set_duration(duration).resize(width=resolution[0]-10).set_position(('center', 60)).crossfadein(crossfade).crossfadeout(crossfade)

def normal_zoom_in(image, duration, resolution):
    image =  ImageClip(image).set_duration(duration).set_position(('center', 60))
    image = image.resize(width=resolution[0]+26)
    image = image.resize(lambda t: 1 + 0.04 * t)
    return image

def get_position(image):
    image = Image.open(image).convert('RGB')
    cropper = smartcrop.SmartCrop()
    result = cropper.crop(image, 100, 100)

    top = result['top_crop']
    x, y = int(top['x']+top['width']/2), int(top['y']+top['height']/2)
    width = image.size[0]/3
    height = image.size[1]/3
    position = ''

    if y<height:
        position='top'
    elif y>height*2:
        position='bottom'

    if x<width:
        position+='left'
    elif x<width*2:
        position='center' if position=='' else position
    else:
        position+='right'
    return position


def Zoom(image, duration, resolution, mode='in',position='center',speed=1, fps = 24):
    clip = ImageClip(image).set_duration(duration).set_position(('center', 80)).resize(width=resolution[0])
    total_frames = int(duration*fps)
    def main(getframe,t):
        frame = getframe(t)
        h,w = frame.shape[:2]
        i = t*fps
        if mode == 'out':
            i = total_frames-i
        zoom = 1+(i*((0.1*speed)/total_frames))
        positions = {'center':[(w-(w*zoom))/2,(h-(h*zoom))/2],
                     'left':[0,(h-(h*zoom))/2],
                     'right':[(w-(w*zoom)),(h-(h*zoom))/2],
                     'top':[(w-(w*zoom))/2,0],
                     'topleft':[0,0],
                     'topright':[(w-(w*zoom)),0],
                     'bottom':[(w-(w*zoom))/2,(h-(h*zoom))],
                     'bottomleft':[0,(h-(h*zoom))],
                     'bottomright':[(w-(w*zoom)),(h-(h*zoom))]}
        tx,ty = positions[get_position(image)]
        M = np.array([[zoom,0,tx], [0,zoom,ty]])
        frame = cv2.warpAffine(frame,M,(w,h))
        return frame
    return clip.fl(main)

from skimage.filters import gaussian
def blur(image):
    return gaussian(image.astype(float), sigma=10)