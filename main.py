import time
from music_bot import telegram_bot_helper


def main():
    last_update_id = None
    while True:
        updates = telegram_bot_helper.get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = telegram_bot_helper.get_last_update_id(updates) + 1
            telegram_bot_helper.echo_all(updates)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
