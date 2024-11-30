def start_command(message) -> str:
    return f'Greetings {message.from_user.first_name} {message.from_user.last_name} 👋\n\n' \
        'Start typing and see how the bot works 🤖\n' \
        'I would very much appreciate your feedback, if you have any! 🙏\n' \
        'You can contact me via <a href="https://t.me/The_One_Reborn">Telegram</a> ✉️\n\n' \
        'By the way, this bot only supports English 🇬🇧\n'