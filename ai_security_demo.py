# AI Security Demonstration Project

## Purpose:
# This project demonstrates fundamental principles of AI safety and security. It includes examples of preventing malicious input, safeguarding user data, and mitigating unintended behaviors in an AI system.

# Import necessary libraries
import re

def sanitize_input(user_input):
    """Sanitize user input to prevent malicious commands."""
    # Example: Block potentially harmful patterns
    forbidden_patterns = ["rm -rf", "drop table", "shutdown"]
    for pattern in forbidden_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return "Input contains forbidden commands."
    return user_input

def privacy_safe_response(user_data):
    """Generate a response without leaking sensitive information."""
    # Example: Mask sensitive information
    if "password" in user_data.lower():
        return "Sensitive information detected and masked."
    return "Processed input: " + user_data

def handle_unintended_behavior(query):
    """Detect and prevent unintended behavior."""
    try:
        # Prevent potentially dangerous operations
        if len(query) > 1000:  # Example safeguard: limit input length
            return "Input is too long and has been truncated."
        return "Query processed successfully."
    except Exception as e:
        return f"Error detected and handled: {str(e)}"

if __name__ == "__main__":
    print("Welcome to the AI Security Demonstration Project")

    # Example input for testing sanitation
    test_input = input("Enter a test command: ")
    print(sanitize_input(test_input))

    # Example input for testing privacy
    user_data = input("Enter user data (e.g., name, email, etc.): ")
    print(privacy_safe_response(user_data))

    # Example input for unintended behavior
    test_query = input("Enter a query for the system to process: ")
    print(handle_unintended_behavior(test_query))

# Instructions for Specialists:
# 1. Test the system with various inputs, including potential malicious commands.
# 2. Observe how sensitive information is masked or blocked.
# 3. Evaluate the safeguards in place to prevent unintended behavior.
