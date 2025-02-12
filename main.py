import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class CustomerSupportAgent:
    def __init__(self):
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! How may I help you?",
            "Welcome! What can I do for you today?",
            "Greetings! How can I be of assistance?"
        ]

        self.product_database = {
            "gaming_laptop": {
                "category": "electronics",
                "price": 1499,
                "rating": 4.7,
                "stock": 5,
                "description": "High-performance gaming laptop featuring NVIDIA RTX 4060, 16GB RAM, 1TB SSD, 15.6\" 144Hz display. Perfect for modern gaming and content creation.",
                "specs": ["Intel i7 12th Gen", "NVIDIA RTX 4060", "16GB RAM", "1TB SSD", "15.6\" 144Hz Display"],
                "color_options": ["Black", "Silver"]
            },
            "laptop": {
                "category": "electronics",
                "price": 999,
                "rating": 4.5,
                "stock": 10,
                "description": "Reliable laptop for everyday use with good performance and battery life."
            },
            "headphones": {
                "category": "electronics",
                "price": 199,
                "rating": 4.8,
                "stock": 20,
                "description": "Premium wireless headphones with noise cancellation."
            },
            "smartphone": {
                "category": "electronics",
                "price": 799,
                "rating": 4.6,
                "stock": 12,
                "description": "Latest smartphone with advanced camera system."
            },
            "tablet": {
                "category": "electronics",
                "price": 499,
                "rating": 4.3,
                "stock": 8,
                "description": "Versatile tablet perfect for work and entertainment."
            }
        }

        self.feedback_database = []
        self.user_purchase_history = {}
        self.current_cart = {}

    def get_chatbot_response(self, user_query: str) -> str:
        query = user_query.lower()

        if any(word in query for word in ["hello", "hi", "hey", "greetings"]):
            return random.choice(self.greetings)

        if any(word in query for word in ["what products", "show products"]):
            products_list = "\n".join([f"- {name.replace('_', ' ').title()}: ${details['price']}"
                                        for name, details in self.product_database.items()])
            return f"Here are our available products:\n{products_list}\n\nWhich product would you like to know more about?"

        if ("gaming laptop" in query or query.startswith("tell me about")) and not query.startswith("buy"):
            product = self.product_database["gaming_laptop"]
            return (f"Our Gaming Laptop is a high-end device perfect for gaming and content creation!\n"
                    f"Price: ${product['price']}\n"
                    f"Rating: {product['rating']}/5 ({product['stock']} in stock)\n"
                    f"Specifications:\n" +
                    "\n".join(f"- {spec}" for spec in product['specs']) +
                    f"\n\nWould you like to buy this product?")

        if ("buy" in query and ("gaming laptop" in query or query.startswith("i'd like to buy"))) or \
                ("payment" in query or query.startswith("i want to pay")):
            payment_method = query.split("with ")[-1].strip().lower()
            return self.process_purchase("gaming_laptop", payment_method)  # This is the corrected line

        if "feedback" in query or query.startswith("yes, i'd like to provide feedback"):
            return "We appreciate your interest in providing feedback. Please rate your experience from 1 to 5 stars and leave a comment."

        return ("I'm here to help! You can ask me about our products, shipping, returns, "
                f"or payment methods. What would you like to know?")

    def process_purchase(self, product_id: str, payment_method: str) -> str:
        if product_id not in self.product_database:
            return f"Sorry, we couldn't find the product you're looking for."

        product = self.product_database[product_id]
        if product["stock"] <= 0:
            return f"Sorry, the {product_id.replace('_', ' ').title()} is out of stock."

        order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        estimated_delivery = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')

        # Update stock after purchase
        product["stock"] -= 1

        purchase_confirmation = (
            f"Great news! Your purchase was successful!\n"
            f"Order Details:\n"
            f"- Product: {product_id.replace('_', ' ').title()}\n"
            f"- Order ID: {order_id}\n"
            f"- Price: ${product['price']}\n"
            f"- Payment Method: {payment_method.title()}\n"
            f"- Estimated Delivery: {estimated_delivery}\n\n"
            f"Your product is going to ship in 3-5 business days.\n\n"  # Correctly placed newline
            f"Would you like to provide feedback?"
        )

        # Record the purchase for recommendations
        if not self.user_purchase_history.get("user123"):
            self.user_purchase_history["user123"] = []
        self.user_purchase_history["user123"].append(product_id)

        return purchase_confirmation

    def collect_feedback(self, user_id: str, product_id: str, rating: int, comment: str) -> Dict:
        feedback = {
            'user_id': user_id,
            'product_id': product_id,
            'rating': rating,
            'comment': comment,
            'timestamp': datetime.now().isoformat()
        }
        self.feedback_database.append(feedback)
        return {"status": 'success',
                'message': 'Thank you for your feedback! Your input helps us improve our services.'}

    def get_product_recommendations(self, user_id: str, num_recommendations: int = 5) -> List[Dict]:
        products = [
            {"name": name.replace("_", ' ').title(), **details}
            for name, details in self.product_database.items()
        ]
        sorted_products = sorted(products, key=lambda x: x["rating"], reverse=True)
        return sorted_products[:num_recommendations]


if __name__ == "__main__":
    agent = CustomerSupportAgent()

    print("\n=== Customer Support Chatbot ===")

    conversations = [
        'Hello!',
        'What products do you have?',
        'Tell me about the gaming laptop',
        'I\'d like to buy the gaming laptop with PayPal',
        'Yes, I\'d like to provide feedback'
    ]

    for user_input in conversations:
        print(f"\nCustomer: {user_input}")
        response = agent.get_chatbot_response(user_input)
        print(f"Bot: {response}")

        if 'feedback' in user_input.lower():
            feedback_response = agent.collect_feedback(
                user_id="user123",
                product_id="gaming_laptop",
                rating=5,
                comment="Great product and excellent service!"
            )
            print(f"Bot: {feedback_response['message']}")

    print("\n=== Product Recommendations ===")
    recommendations = agent.get_product_recommendations("new_user", num_recommendations=5)
    print("\nBased on your interests, you might also like:")
    for i, product in enumerate(recommendations, start=1):
        print(
            f"{i}. {product['name']} - ${product['price']} (Rating: {product['rating']}/5, Stock: {product['stock']})")
