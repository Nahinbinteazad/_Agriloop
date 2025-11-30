from agents.base_agent import BaseAgent

class LogisticsPlanner(BaseAgent):
    def plan(self, location, quantity):
        return self.generate(
            f"Estimate transport options and cost for {quantity}kg waste in {location}."
        )
