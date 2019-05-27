if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "750842214:AAFf3Y8p-VZH21CD7H1RfFCe5z_ISOgXWLU"
    OWNER_ID = "656268508"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "shivamkchoudhary"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://qroenkltmcayaa:ec5a1f35cea2730cc1c71be5f844baa13ca4010636e6ecbc6b545d818b365c70@ec2-23-21-234-53.compute-1.amazonaws.com:5432/dbqft2v7jbq49o'  # needed for any database modules
    MESSAGE_DUMP = -1001326118005  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = ANYTHING
    URL = "https://thanosbots1.herokuapp.com/"

    # OPTIONAL
    SUDO_USERS = [810714359 649156353 686956429 768326378 759400881]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [686956429]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [810714359 649156353 686956429 768326378 759400881]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADBQADDQADjR\_yKCDDBtuwTt59Ag'  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = 'ed529683f29bb1bfe7a0392b81e37ff8' # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
