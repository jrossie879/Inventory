def filter_spam(messages, banned_word):
    return[message for message in messages if banned_word.lower() not in message.lower()]
    