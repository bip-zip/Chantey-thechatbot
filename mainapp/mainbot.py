import re
import random

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}
    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Namaste, Sanchai Hunuhuncha?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!.', ['bye', 'goodbye'], single_response=True)
    response('I love you more.', ['love', 'you'], single_response=True)
    response('Bachekai chu', ['k', 'cha'], single_response=True)
    response('bip-zip created me. I am so greatful to exist.', ['who','creator', 'made','you'],required_words=['who'], single_response=True)
    response('I am chantey. Your comrade your chatbot.', ['who', 'are', 'you'], required_words=['you'],single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing',], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'bip', 'zip'], required_words=['bip', 'zip'])


    # Longer responses
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    return unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
