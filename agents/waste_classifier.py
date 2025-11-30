from agents.base_agent import BaseAgent

class WasteClassifier(BaseAgent):
    def classify(self, image_path):
        return self.generate(f"Identify agricultural waste type in this image: {image_path}")
