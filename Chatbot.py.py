def rule_based_chatbot():
    print("==================================================")
    print("  DecodeLabs AI Chatbot (Logic Engine V1.0)       ")
    print("  System Status: ONLINE [Deterministic Mode]     ")
    print("==================================================")
    print("Bot: Hello! I am your rule-based AI assistant.")
    print("     How can I help you today? (Type 'exit' or 'bye' to quit)\n")

    # Core Execution Requirement: Continuous Digital Loop
    while True:
        # Phase 1: Input Gathering (Raw Feed)
        raw_input_data = input("You: ")
        
        # Phase 1: Sanitization & Normalization Process
        # Removes leading/trailing whitespaces and converts to lower-case
        clean_input = raw_input_data.lower().strip()
        
        # Phase 2 & 3: Process (Logic Skeleton) & Output (Feedback Loop)
        
        # Handling Exit Commands
        if clean_input == "exit" or clean_input == "bye":
            print("Bot: Goodbye! Have a wonderful day ahead. Shutting down loop.")
            print("==================================================")
            break  # Terminates the continuous loop safely
            
        # Handling Greetings
        elif clean_input in ["hello", "hi", "hey", "greetings"]:
            print("Bot: Hello there! Hope you are doing great. What's on your mind?")
            
        # Handling Help/Inquiries
        elif "help" in clean_input or "support" in clean_input:
            print("Bot: I am fully trained with deterministic guardrails. I can assist you with basic logic routes.")
            
        # Project Phase Inquiry
        elif "project" in clean_input or "decodelabs" in clean_input:
            print("Bot: This is Project 1: The Logic Engine phase. It is a mandatory foundation for all interns.")
            
        # Handling "System 1 vs System 2" Concept
        elif "system" in clean_input or "logic" in clean_input:
            print("Bot: System 1 is a probabilistic Artist. System 2 is a deterministic Engineer. I am currently running on System 2!")
            
        # Catch-all Route for Unrecognized Inputs (Fallback)
        else:
            print("Bot: I understand your input is sanitized, but it does not match my current pre-defined hard-coded rules. Please try asking something else!")
        
        print("-" * 50)  # Visual divider for readability in the loop

# Execute the application
if __name__ == "__main__":
    rule_based_chatbot()