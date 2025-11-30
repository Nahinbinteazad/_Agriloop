from agents.base_agent import BaseAgent

class PriceRecommender(BaseAgent):
    def recommend(self, waste_type, location):
        return self.generate(
            f"Suggest fair market price for {waste_type} in {location}."
        )
