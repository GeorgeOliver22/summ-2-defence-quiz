def validate_name(name):
    clean_name = name.strip()
    return len(clean_name) >= 2

def check_answer(user_choice, correct_answer):
    return user_choice == correct_answer 