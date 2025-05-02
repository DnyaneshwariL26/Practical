import random

class PersonalAssistant:
    def __init__(self):
        self.user_name = ""
        self.interests = []
        self.goal = ""
        
    def greet(self):
        print("Hello! I'm your Personal Assistant Bot.")
        print("What's your name?")
        self.user_name = input("Your name: ")
        print(f"Nice to meet you, {self.user_name}! 😊")
        
    def ask_interest(self):
        print("Tell me about your interests. What do you enjoy doing?")
        interests = input("Your interests (comma-separated): ").split(',')
        self.interests = [interest.strip() for interest in interests]
        print(f"That's great! I see you love {', '.join(self.interests)}.")

    def set_goal(self):
        print("Let's set a personal goal for you!")
        self.goal = input("What is one goal you want to achieve? ")
        print(f"Awesome! Your goal is: {self.goal}. Stay focused and work towards it!")

    def motivation(self):
        quotes = [
            "Don't stop when you're tired. Stop when you're done!",
            "Every expert was once a beginner.",
            "You have everything it takes to succeed!",
            "Push yourself, because no one else will do it for you."
        ]
        print(f"Here's a motivational boost for you: \n\"{random.choice(quotes)}\"")

    def farewell(self):
        print(f"Great chatting with you, {self.user_name}! Keep chasing your dreams. 😊")

# Running the chatbot
assistant = PersonalAssistant()
assistant.greet()
assistant.ask_interest()
assistant.set_goal()
assistant.motivation()
assistant.farewell()
