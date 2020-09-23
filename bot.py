import getopt
import sys

from the42bot.controller import BotController
from the42bot.model import InputBot

HELP_TEXT = "bot.py -t token"


def read_configuration(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:", ["token="])
        token = ''

    except getopt.GetoptError:
        print(HELP_TEXT)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(HELP_TEXT)
            sys.exit(0)
        elif opt in ['-t', '--token']:
            token = arg

    return InputBot(token)


if __name__ == '__main__':
    input_bot = read_configuration(sys.argv[1:])
    thebot = BotController(input_bot)
    thebot.execute()
