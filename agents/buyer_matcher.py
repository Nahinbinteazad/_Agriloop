import json
from agents.base_agent import BaseAgent

class BuyerMatcher(BaseAgent):
    def __init__(self):
        super().__init__()
        with open("tools/buyers_list.json", "r") as f:
            self.buyers = json.load(f)

    def find_buyers(self, waste_type):
        return self.buyers.get(waste_type.lower(), [])
