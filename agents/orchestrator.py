from agents.waste_classifier import WasteClassifier
from agents.price_recommender import PriceRecommender
from agents.buyer_matcher import BuyerMatcher
from agents.logistics_planner import LogisticsPlanner
from agents.summary_agent import SummaryAgent

class AgriLoopOrchestrator:
    def __init__(self):
        self.classifier = WasteClassifier()
        self.pricer = PriceRecommender()
        self.matcher = BuyerMatcher()
        self.logistics = LogisticsPlanner()
        self.summary = SummaryAgent()

    def run(self, input_data):
        waste_type = self.classifier.classify(input_data["image_path"])

        price_suggestion = self.pricer.recommend(
            waste_type=waste_type,
            location=input_data["location"]
        )

        buyers = self.matcher.find_buyers(waste_type)

        logistics = self.logistics.plan(
            location=input_data["location"],
            quantity=input_data["quantity_kg"]
        )

        summary = self.summary.create_summary(
    waste_type=waste_type,
    price=price_suggestion,
    buyers=buyers,
    logistics=logistics,
    quantity=input_data["quantity_kg"],
    location=input_data["location"]
)


        return summary
