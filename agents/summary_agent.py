from agents.base_agent import BaseAgent

class SummaryAgent(BaseAgent):
    def create_summary(self, waste_type, price, buyers, logistics, quantity, location):
        # Extract numeric price from string
        price_value = int(price.split()[0])  
        total_value = price_value * quantity

        summary_text = f"""
🌾 Farmer Waste Report
----------------------------
Date: Today
Location: {location}

Waste Type: {waste_type}
Description: {waste_type} is agricultural leftover material that can be sold or reused.

Quantity Available: {quantity} kg
Suggested Price: {price} per kg
Estimated Total Value: {total_value} BDT

Potential Buyers:
{', '.join(buyers)}

Logistics Options:
{logistics}

💡 Recommendation:
- Contact buyers immediately to secure a sale.
- Choose the transport option that balances cost and convenience.
----------------------------
"""
        return summary_text
