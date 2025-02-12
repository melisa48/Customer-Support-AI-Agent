# Customer-Support-AI-Agent
Customer Support AI Agent is an interactive chatbot designed to provide customer support for an e-commerce platform. The chatbot is capable of handling various customer inquiries related to product information, purchasing, feedback, and recommendations. It simulates human-like interaction and assists customers in their shopping experience.

## Features

- **Greeting Customers**: Respond to greetings with various welcome messages.
- **Product Information**: Provides details about available products and their specifications.
- **Purchase Processing**: Handles purchase requests, updates stock, and provides order details including shipping information.
- **Feedback Collection**: Collects and stores customer feedback for future improvements.
- **Product Recommendations**: Recommends products based on user purchase history and ratings.

## Code Structure

The main components of the code are:

- `CustomerSupportAgent`: The main class that simulates a customer support agent.
- `__init__()`: Initializes the agent with predefined greetings, product database, and other necessary attributes.
- `get_chatbot_response(user_query)`: Processes user queries and generates appropriate responses.
- `process_purchase(product_id, payment_method)`: Handles purchase requests, updates stock, and provides order details including estimated delivery.
- `collect_feedback(user_id, product_id, rating, comment)`: Collects customer feedback and stores it in the feedback database.
- `get_product_recommendations(user_id, num_recommendations)`: Provides product recommendations based on user purchase history and product ratings.

## Installation

To run this project, you will need Python installed on your machine. Follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/customersupportagent.git
    ```

2. Navigate to the project directory:
    ```bash
    cd customersupportagent
    ```

3. Run the Python script:
    ```bash
    python customersupportagent.py
    ```

## Usage

Run the script and interact with the chatbot through the console. Example conversation:

=== Customer Support Chatbot ===

Customer: Hello!
Bot: Hello! How can I assist you today?

Customer: What products do you have?
Bot: Here are our available products:
- Gaming Laptop: $1499
- Laptop: $999
- Headphones: $199
- Smartphone: $799
- Tablet: $499

Which product would you like to know more about?

Customer: Tell me about the gaming laptop
Bot: Our Gaming Laptop is a high-end device perfect for gaming and content creation!
Price: $1499
Rating: 4.7/5 (5 in stock)
Specifications:
- Intel i7 12th Gen
- NVIDIA RTX 4060
- 16GB RAM
- 1TB SSD
- 15.6" 144Hz Display

Would you like to buy this product?

Customer: I'd like to buy a gaming laptop with PayPal
Bot: Great news! Your purchase was successful!
Order Details:
- Product: Gaming Laptop
- Order ID: ORD-20250212143400
- Price: $1499
- Payment Method: Paypal
- Estimated Delivery: 2025-02-17

- Your product is going to ship in 3-5 business days.
- Would you like to provide feedback?
- Yes, I would like to provide feedback. 
- We appreciate your interest in providing feedback. Please rate your experience from 1 to 5 stars and leave a comment.
- Thank you for your feedback! Your input helps us improve our services.


## Contributing
- Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.
