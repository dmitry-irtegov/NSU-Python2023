from pathlib import Path
from typing import Dict

NUMBER_NAMES: Dict[int, str] = {
    10: "ten", 9: "nine", 8: "eight", 7: "seven", 6: "six",
    5: "five", 4: "four", 3: "three", 2: "two", 1: "one",
}

RESOURCES = Path(__file__).parent / "resources"
GENERAL_VERSE = (RESOURCES / "general-verse.txt").read_text(encoding="UTF-8")
LAST_VERSE = (RESOURCES / "last-verse.txt").read_text(encoding="UTF-8").strip()


def generate_song() -> str:
    song = ""

    for num in range(10, 1, -1):
        song += GENERAL_VERSE.format(
            now=NUMBER_NAMES[num].capitalize(),
            next=NUMBER_NAMES[num - 1].lower(),
            ending="s" if num - 1 != 1 else "",
        )

    return song + LAST_VERSE
