from PIL import Image, ImageDraw, ImageFont
import numpy as np

# def TextImage(text, font_path, width=593, fontsize=40, color="#FFFFFF", filename='text.png'):
#     # Load the font
#     font = ImageFont.truetype(font_path,fontsize, layout_engine=ImageFont.LAYOUT_RAQM)

#     # Calculate line width and height
#     line_width, line_height = font.getsize(text)
#     lines = []

#     # If the text width is greater than image width, split it into multiple lines
#     if line_width > width:
#         words = text.split(' ')
#         line = ''
#         for word in words:
#             word_width, word_height = font.getsize(word)
#             if (font.getsize(line + ' ' + word)[0] <= width):
#                 line = line + ' ' + word
#             else:
#                 lines.append(line)
#                 line = ''
#                 line = line + ' ' + word
#         if line:
#             lines.append(line)
#     else:
#         lines.append(text)

#     # Calculate total height of image
#     total_height = len(lines) * line_height

#     # Create a new image with correct width and height
#     img = Image.new('RGBA', (width, total_height), color=(0, 0, 0, 0))

#     d = ImageDraw.Draw(img)

#     # Draw text on image
#     y_text = 0
#     for line in lines:
#         d.text((0, y_text), line, font=font, fill=color)
#         y_text += line_height

#     # Save the image
#     return np.array(img)

def TextImage(text, highlight_word, highlight_word_index, font_path="./assets/fonts/Hindi.ttf", width=593, fontsize=40, color="#FFFFFF", highlight_color="#FF0000"):
    # Load the font
    font = ImageFont.truetype(font_path, fontsize, layout_engine=ImageFont.LAYOUT_RAQM)

    # Calculate line width and height
    line_width, line_height = font.getsize(' '.join(text))
    lines = []

    # If the text width is greater than image width, split it into multiple lines
    if line_width > width:
        words = text
        line = []
        for word in words:
            word_width, word_height = font.getsize(word)
            if (font.getsize(' '.join(line) + ' ' + word)[0] <= width):
                line.append(word)
            else:
                lines.append(line)
                line = [word]
        if line:
            lines.append(line)
    else:
        lines.append(text)

    # Calculate total height of image
    total_height = len(lines) * line_height

    # Create a new image with correct width and height
    img = Image.new('RGBA', (width, total_height), color=(0, 0, 0, 0))

    d = ImageDraw.Draw(img)

    # Draw text on image
    y_text = 0
    i = 0
    highlighted=False
    for line in lines:
        x_text = 0
        for word in line:
            word_color=color
            if word == highlight_word and highlight_word_index==i:
                word_color=highlight_color
                highlighted=True
            d.text((x_text, y_text), word, font=font, fill=word_color)
            x_text += font.getsize(word + ' ')[0]
            i+=1
        y_text += line_height

    if not highlighted: print("NO COLOR HIGHLIGHTED!!!!!!!",text, highlight_word, highlight_word_index)
    # Save the image
    return np.array(img)

def TextImageLegacy(text, font_path, width=593, fontsize=40, color="#FFFFFF"):
    # Load the font
    font = ImageFont.truetype(font_path,fontsize, layout_engine=ImageFont.LAYOUT_RAQM)

    # Calculate line width and height
    line_width, line_height = font.getsize(text)
    lines = []

    # If the text width is greater than image width, split it into multiple lines
    if line_width > width:
        words = text.split(' ')
        line = ''
        for word in words:
            word_width, word_height = font.getsize(word)
            if (font.getsize(line + ' ' + word)[0] <= width):
                line = line + ' ' + word
            else:
                lines.append(line)
                line = ''
                line = line + ' ' + word
        if line:
            lines.append(line)
    else:
        lines.append(text)

    # Calculate total height of image
    total_height = len(lines) * line_height

    # Create a new image with correct width and height
    img = Image.new('RGBA', (width, total_height), color=(0, 0, 0, 0))

    d = ImageDraw.Draw(img)

    # Draw text on image
    y_text = 0
    for line in lines:
        d.text((0, y_text), line, font=font, fill=color)
        y_text += line_height

    # Save the image
    return np.array(img)