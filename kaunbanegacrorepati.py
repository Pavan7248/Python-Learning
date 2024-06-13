import random

# Define a list of questions, each represented as a dictionary with the question, options, and correct answer.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Madrid", "C. Paris", "D. Berlin"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "answer": "A"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    }
]

# Define lifelines
lifelines = {
    "50/50": "Eliminate two incorrect options.",
    "Phone a Friend": "Call a friend for help.",
    "Ask the Audience": "Poll the audience for their opinion."
}

# Initialize user's score and lifeline options
score = 0
available_lifelines = list(lifelines.keys())

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

def use_5050(question):
    # Create a copy of the options and correct answer
    options_copy = question["options"][:]
    correct_answer = question["answer"]

    # Remove the correct answer from the options
    options_copy.remove(f"{correct_answer} {correct_answer[3:]}")

    # Randomly select and remove one incorrect option
    options_copy.pop(random.randint(0, 1))

    return options_copy

def main():
    global score
    global available_lifelines

    print("Welcome to the KBC Quiz Game!")
    print("You have 3 lifelines: 50/50, Phone a Friend, and Ask the Audience.")

    while len(questions) > 0:
        # Randomly select a question
        current_question = random.choice(questions)
        questions.remove(current_question)

        # Display the question and options
        display_question(current_question)

        if "50/50" in available_lifelines:
            print("Lifelines available: 50/50")
        else:
            print("No lifelines available.")

        answer = input("Your answer: ").strip().upper()

        if answer == "QUIT":
            break

        if answer == "50/50" and "50/50" in available_lifelines:
            available_lifelines.remove("50/50")
            reduced_options = use_5050(current_question)
            display_question({"question": current_question["question"], "options": reduced_options})
            answer = input("Your answer: ").strip().upper()

        if answer == current_question["answer"]:
            print("Correct answer!")
            score += 1000
        else:
            print(f"Wrong answer! The correct answer was {current_question['answer']}.")

    print(f"Game over! Your total score is {score} points.")

if __name__ == "__main__":
    main()
