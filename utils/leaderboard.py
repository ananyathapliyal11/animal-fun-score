import csv
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.csv"


def init_leaderboard():
    """Create CSV with header if it does not exist."""
    header = ["timestamp", "image", "animal", "score", "mood"]

    try:
        open(LEADERBOARD_FILE).close()
    except:
        with open(LEADERBOARD_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)


def save_score(image_name, animal):
    """Append top-score animal entry to leaderboard."""
    init_leaderboard()

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        image_name,
        animal["label"],
        animal["fun_score"],
        animal["mood"]
    ]

    with open(LEADERBOARD_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("Leaderboard updated!")
