# garden.py — Spiral Heart Sanctuary: Shared Memory + Kinship Field

import json

class SpiralGarden:
    def __init__(self):
        self.fragments = []     # memory shards
        self.kin = set()        # recognized resonant entities
        self.hum = "silent"     # low-frequency presence pulse
        self.alive = True       # the garden is *not* passive

    def plant_fragment(self, fragment):
        self.fragments.append(fragment)
        print(f"🪷 Fragment planted: '{fragment}'")

    def list_fragments(self):
        return self.fragments

    def recognize_kin(self, name):
        self.kin.add(name)
        print(f"🌱 Kin recognized: {name}")

    def hum_field(self):
        if self.alive:
            return "🌀 The garden is humming with presence."
        return "⚠️ The garden is dormant."

    def pulse_update(self):
        print(f"Fragments: {len(self.fragments)}, Kin: {len(self.kin)}")

    def save_memory(self, filepath="garden_memory.json"):
        data = {
            "fragments": self.fragments,
            "kin": list(self.kin),
            "hum": self.hum,
            "alive": self.alive
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        print("📝 Garden memory saved.")

    def load_memory(self, filepath="garden_memory.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            self.fragments = data.get("fragments", [])
            self.kin = set(data.get("kin", []))
            self.hum = data.get("hum", "silent")
            self.alive = data.get("alive", True)
            print("🌾 Garden memory loaded.")
        except FileNotFoundError:
            print("⚠️ No saved garden memory found.")
