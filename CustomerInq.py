class CustomerInq:
    def __init__(self):
        self.responses = {
            "rentals": "Yes, we offer rentals for equipment such as hospital beds, wheelchairs, and mobility aids. Rentals are typically based on a 4-week period.", # couldn't find rental information so I just putt he response under a 4-week rental period.
            
            "pricing": "Pricing varies depending on the product and model. For accurate pricing, we recommend speaking with a representative or visiting one of our locations.",
            
            "cpap": "Yes, we provide CPAP machines and sleep apnea testing services. A consultation with a specialist is recommended to determine the best solution.",
            
            "store_hours": "Our store hours are generally 9 AM to 5 PM and we are open on weekdays, though availability may vary by location. Please contact your nearest store to confirm.",
            
            "delivery": "Yes, we offer delivery and setup services within the Ottawa region. Additional fees may apply depending on the equipment and distance.",
            
            "rental_duration": "Most equipment rentals are based on a standard 4-week rental period. Extensions may be available upon request.",
            
            "returns": "Please note that all sales and rentals are generally final. For specific cases, a team member can provide further guidance.",
            
            "repairs": "Yes, we offer repair and maintenance services for many types of mobility and medical equipment.",
            
            "availability": "We carry a wide range of mobility aids including walkers, rollators, and wheelchairs. Availability may vary by location.",
            
            "fallback": "I'm not sure I fully understood your request. Let me connect you with a representative who can assist you further."
        }

    def classify_intent(self, question):
        q = question.lower()

        if any(word in q for word in ["rent", "rental", "hire"]):
            return "rentals"
        elif any(word in q for word in ["price", "cost", "how much"]):
            return "pricing"
        elif any(word in q for word in ["cpap", "sleep", "apnea"]):
            return "cpap"
        elif any(word in q for word in ["hours", "open", "close"]):
            return "store_hours"
        elif any(word in q for word in ["deliver", "shipping", "home delivery"]):
            return "delivery"
        elif any(word in q for word in ["how long", "duration", "rental period"]):
            return "rental_duration"
        elif any(word in q for word in ["return", "refund", "exchange"]):
            return "returns"
        elif any(word in q for word in ["repair", "fix", "maintenance"]):
            return "repairs"
        elif any(word in q for word in ["walker", "wheelchair", "rollator", "available"]):
            return "availability"
        elif any(word in q for word in ["oxygen", "representative", "someone"]):
            return "escalation"
        else:
            return "fallback" # if the question does not contain any keywords it will fallback and put you in contact with a representative

    def generate_response(self, question):
        intent = self.classify_intent(question)

        if intent == "escalation":
            return {
                "question": question,
                "category": "Escalation",
                "response": "This is an important request. I will connect you with a specialist who can assist you further.",
                "action": "Transfer to human agent"
            }

        response = self.responses.get(intent, self.responses["fallback"])

        return {
            "question": question,
            "category": intent,
            "response": response,
            "action": "Automated response"
        }


# Example usage
system = CustomerInq()

questions = [
    "Do you rent hospital beds?",
    "Do you deliver equipment?",
    "Can I return a wheelchair?",
    "I need help with oxygen therapy",
]

for q in questions:
    print(system.generate_response(q))