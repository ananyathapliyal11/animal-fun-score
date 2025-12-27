import os
import cv2
from models.detector import detect_animals
from utils.features import posture_from_aspect_ratio
from models.mood import infer_mood
from models.fun_score import compute_fun_score
from utils.visualization import draw_results
from utils.leaderboard import save_score

IMAGE_DIR = "data/images"   

print("\n🚀 Pet / Animal Fun Score Predictor")
print("📂 Reading images from:", IMAGE_DIR)


for file in os.listdir(IMAGE_DIR):

    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGE_DIR, file)
    print(f"\n📸 Processing: {file}")

    image, animals = detect_animals(image_path)

    if not animals:
        print("⚠ No animals detected — skipping")
        continue

    for a in animals:
        a["posture"] = posture_from_aspect_ratio(a["bbox"])
        a["mood"], a["emoji"] = infer_mood(a["posture"])
        a["fun_score"] = compute_fun_score(a, image)

    best = max(animals, key=lambda a: a["fun_score"])
    save_score(file, best)

    result = draw_results(image, animals)

    out_name = f"output_{file}"
    cv2.imwrite(out_name, result)

    print(f"Output saved as: {out_name}")

print("\nLeaderboard updated (leaderboard.csv)")
print("All images processed successfully!")
