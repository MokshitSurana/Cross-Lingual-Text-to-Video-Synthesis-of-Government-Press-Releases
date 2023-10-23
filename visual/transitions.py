from moviepy.decorators import add_mask_if_none, requires_duration
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


@requires_duration
@add_mask_if_none
def crossfadein(clip, duration):
    clip.mask.duration = clip.duration
    newclip = clip.copy()
    newclip.mask = clip.mask.fx(fadein, duration)
    return newclip


@requires_duration
@add_mask_if_none
def crossfadeout(clip, duration):
    clip.mask.duration = clip.duration
    newclip = clip.copy()
    newclip.mask = clip.mask.fx(fadeout, duration)
    return newclip


def slide_in(clip, duration, side, resolution):
    rw, rh = resolution
    w, h = clip.size
    pos_dict = {'left': lambda t: (min(656, 656+(rw*(t/duration-1))), 80),
                'right': lambda t: (max(656, 656+(rw*(1-t/duration))), 80),
                'top': lambda t: ('center', min(80, h*(t/duration-1))),
                'bottom': lambda t: ('center', max(610, 610+(h*(1-t/duration))))}

    return clip.set_position(pos_dict[side])


@requires_duration
def slide_out(clip, duration, side, resolution):
    rw, rh = resolution
    w,h = clip.size
    ts = clip.duration - duration # start time of the effect.
    pos_dict = {'left' : lambda t: (min(656, 656+(rw*(-(t-ts)/duration))),80),
                'right' : lambda t: (max(656, 656+(rw*((t-ts)/duration))),80),
                'top' : lambda t: ('center',min(80,h*(-(t-ts)/duration))),
                'bottom': lambda t: ('center',max(0,h*((t-ts)/duration))) }

    return clip.set_position(pos_dict[side])


@requires_duration
def make_loopable(clip, cross_duration):
    d = clip.duration
    clip2 = clip.fx(crossfadein, cross_duration).set_start(d - cross_duration)
    return CompositeVideoClip([clip, clip2]).subclip(cross_duration, d)
