import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

TEXT_FONT_PATH  = r"C:\Windows\Fonts\arial.ttf"
EMOJI_FONT_PATH = r"C:\Windows\Fonts\seguisym.ttf"
TEXT_FONT  = ImageFont.truetype(TEXT_FONT_PATH, 24)
EMOJI_FONT = ImageFont.truetype(EMOJI_FONT_PATH, 30)
TEXT_COLOR   = (0, 0, 0)         
STROKE_COLOR = (255, 255, 255)  

def draw_outline_text(draw, pos, text, font):
    x, y = pos
    draw.text((x-1, y-1), text, font=font, fill=STROKE_COLOR)
    draw.text((x+1, y-1), text, font=font, fill=STROKE_COLOR)
    draw.text((x-1, y+1), text, font=font, fill=STROKE_COLOR)
    draw.text((x+1, y+1), text, font=font, fill=STROKE_COLOR)
    draw.text((x, y), text, font=font, fill=TEXT_COLOR)

def draw_results(image, animals):
    if not animals:
        return image

    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    best = max(animals, key=lambda a: a["fun_score"])

    for a in animals:
        x1, y1, x2, y2 = a["bbox"]


        if a is best:
            color = (0, 0, 0)  
            title = "MOST PLAYFUL"
        else:
            color = (50, 50, 50)

        cv2.rectangle(image, (x1, y1), (x2, y2), color, 3)
        mood_line = f"{a['emoji']}  {a['label']} | {a['fun_score']}"

        if a is best:
            draw_outline_text(draw, (x1, y1 - 48), title, TEXT_FONT)

        draw_outline_text(draw, (x1, y1 - 22), mood_line, EMOJI_FONT)

    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
