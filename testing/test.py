from moviepy.editor import ImageClip, TextClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip, CompositeAudioClip
import manimpango
#manimpango.register_font("")
for i in TextClip.list('font'):
    try:
        TextClip(u"હેલો મારું નામ સિદ્ધાર્થ છે", color='white',
                        font=i, method="pango", align='south',fontsize=20).save_frame(f'./delete/{i}.png')
    except:
        pass
