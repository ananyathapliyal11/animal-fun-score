from utils.features import bbox_size_ratio, expression_from_posture_and_size
def compute_fun_score(animal, image):
    score = 50

    size_ratio = bbox_size_ratio(animal["bbox"], image.shape)

    posture = animal["posture"]
    expression = expression_from_posture_and_size(posture, size_ratio)

    if posture == "standing": score += 10
    if posture == "sitting": score -= 5     
    if posture == "lying": score -= 15

    if expression == "playful": score += 20
    if expression == "alert": score += 5
    if expression == "calm": score -= 5
    if expression == "shy": score -= 10
    if expression == "sleepy": score -= 20

    return max(0, min(100, score))
