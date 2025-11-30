class BaseAgent:
    def __init__(self):
        pass

    def generate(self, prompt):
        # simple dummy responses based on keywords
        if "Identify agricultural waste" in prompt:
            return "Rice husk"  # mock waste type
        elif "Suggest fair market price" in prompt:
            return "50 BDT per kg"  # mock price
        elif "Estimate transport options" in prompt:
            return "3 options: local van 500 BDT, truck 800 BDT, pickup 300 BDT"
        elif "Summarize the following Farmer Report" in prompt:
            return "Waste: Rice husk\nPrice: 50 BDT/kg\nBuyers: Buyer A, Buyer B\nLogistics: local van 500 BDT"
        else:
            return "N/A"
