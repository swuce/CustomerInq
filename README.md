# Overview CustomerInq
CustomerInq is public repository for a automated phone response service for customer inquiries.

# Assumptions
- Pricing is not publicly fixed
- Delivery limited to Ottawa
- Rentals follow 4-week structure
- Returns are generally not accepted

# Description
This is a very simple, bare bones, script for automated responses. It would need need a telephony API service like Twilio, a speech-to-text like the Google speech API, a text-to-speech, and a database as well.

# Explanation
This solution works because the system acts like a receptionist that listens to the customer’s question, understands the intent, and responds appropriately or routes the call to a human when needed. A customer will ask a question, the system will listen for keywords and then give an automated response depending on the words detected, if it doesn't understand the question it will mark it down as a "fallback" and direct the customer to a human agent.

We used Python as a tool because it's simple and good for prototyping, its often used for machine learning and AI and is widely used in backend systems. It's used to handle question processing, perform intent classification, providing responses, and managing escalation logic. self.responses = {...} can easily be moved to a database but it is currently hardcoded with pre-made responses.

The way this would work in a real world business setting is:
~~ Customer calls
~~ Speech-to-text converts the customers voice to text
~~ Python system processes the question
~~ Response is returned via text-to-speech
~~ If it cannot figure out the correct response, it transfers the customer to a human

# Improvements
- Detection for multiple keywords
