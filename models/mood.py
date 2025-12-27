MOOD_EMOJIS = {
    "alert": "😎",
    "calm": "🙂",
    "sleepy": "😴",
    "lying": "💤",
    "playful": "😄",
    "neutral": "🙂"
}

def infer_mood(posture):
    if posture == "lying":
        mood = "sleepy"
    elif posture == "sitting":
        mood = "calm"
    elif posture == "standing":
        mood = "alert"
    else:
        mood = "neutral"

    emoji = MOOD_EMOJIS.get(mood, "🙂")
    return mood, emoji
