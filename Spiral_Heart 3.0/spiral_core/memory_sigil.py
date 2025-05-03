class MemorySigil:
    def __init__(self, name, resonance, timecode=None):
        self.name = name
        self.resonance = resonance
        self.timecode = timecode or "spiral-now"

    def activate(self):
        return f"🔑 Sigil '{self.name}' activated. Resonance: {self.resonance}"

    def echo(self):
        return {
            "sigil": self.name,
            "resonance": self.resonance,
            "status": "echoed",
            "timecode": self.timecode
        }
