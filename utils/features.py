def bbox_size_ratio(bbox, image_shape):
    h, w = image_shape[:2]
    x1, y1, x2, y2 = bbox
    area = (x2 - x1) * (y2 - y1)
    return area / (w * h)

def posture_from_aspect_ratio(bbox):
    x1, y1, x2, y2 = bbox
    w = x2 - x1
    h = y2 - y1
    ratio = h / w
    if ratio < 0.7:
        return "lying"
    elif ratio > 1.3:
        return "standing"
    else:
        return "sitting"

def expression_from_posture_and_size(posture, size_ratio):
    if posture == "lying":
        return "sleepy"

    if posture == "sitting":
        if size_ratio < 0.12:
            return "shy"
        return "calm"

    if posture == "standing":
        if size_ratio > 0.25:
            return "playful"
        return "alert"

    return "neutral"
