# PLEASE STOP!
# DO NOT EDIT THIS FILE
# Create a new config.py file in same dir and import, then extend this class.
import os
from distutils.util import strtobool as sb


class Config:
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    # string session for running on Heroku
    # some people upload their session files on GitHub or other third party hosting
    # websites, this might prevent the un-authorized use of the
    # confidential session files
    HU_STRING_SESSION = os.environ.get("HU_STRING_SESSION", None)
    # for alive
    ALIVE_PIC = os.environ.get(
        "ALIVE_PIC", "https://telegra.ph/file/ba9acea0064aaed188195.jpg"
    )
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Send .get_id in any group to fill this value.
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    # Send .g_id in any channel to fill this value.
    PRIVATE_CHANNEL_BOT_API_ID = os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", None)
    if PRIVATE_CHANNEL_BOT_API_ID:
        PRIVATE_CHANNEL_BOT_API_ID = int(PRIVATE_CHANNEL_BOT_API_ID)
    # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./pepe/")
    # This is required for the speech to text module. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # This is required for the hash to torrent file functionality to work.
    HASH_TO_TORRENT_API = os.environ.get(
        "HASH_TO_TORRENT_API", "https://example.com/torrent/{}"
    )
    # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Kirito")
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
    if G_BAN_LOGGER_GROUP:
        G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)
    # TG API limit. An album can have atmost 10 media!
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    # Telegram BOT Token from @BotFather
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # set blacklist_chats where you do not want userbot's features
    UB_BLACK_LIST_CHAT = {
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    }

    # specify LOAD and NO_LOAD
    LOAD = []
    # Remove This To Make Them Work But Would Make Bot Unstable AF...⚡
    NO_LOAD = [
        "pmpermit",
    ]
    # Get your own API key from https://www.remove.bg/ or
    # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # Set to True if you want to block users that are spamming your PMs.
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
    NO_LOG_P_M_S = bool(os.environ.get("NO_LOG_P_M_S", True))
    # send .get_id in any channel to forward all your NEW PMs to this group
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    DB_URI = os.environ.get("DATABASE_URL", None)
    # number of rows of buttons to be displayed in .helpme command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5)
    )
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
    # specify list of users allowed to use bot
    # WARNING: be careful who you grant access to your bot.
    # malicious users could do ".exec rm -rf /*"
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    # Temp
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    CHANNEL_ID = os.environ.get("CHANNEL_ID", None)
    # Google Drive ()
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    # Google Photos ()
    G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
    G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
    G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
    if G_PHOTOS_AUTH_TOKEN_ID:
        G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)
    #
    TELE_GRAM_2FA_CODE = os.environ.get("TELE_GRAM_2FA_CODE", None)
    #
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    # Google Chrome Selenium Stuff
    # taken from
    # https://github.com/jaskaranSM/UniBorg/blob/9072e3580cc6c98d46f30e41edbe73ffc9d850d3/sample_config.py#L104-L106
    GOOGLE_CHROME_DRIVER = os.environ.get(
        "GOOGLE_CHROME_DRIVER", "/usr/bin/google-chrome"
    )
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/chromedriver")
    #
    LYDIA_API = os.environ.get("LYDIA_API", None)
    # Heroku Miscellaneous
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    UPSTREAM_REPO_URL = os.environ.get(
        "UPSTREAM_REPO_URL", "https://github.com/prono69/PepeBot"
    )
    #
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    CHROME_BIN = os.environ.get("CHROME_BIN", None)
    # define "heroku_link" in conig_vars
    HEROKU_LINK = os.environ.get("HEROKU_LINK", None)
    # define "repo_link" in conig_vars
    REPO_LINK = os.environ.get("REPO_LINK", None)
    # define "repo_link" in conig_vars
    PACKS_CONTENT = os.environ.get("PACKS_CONTENT", None)
    #
    PACK_NAME = os.environ.get("PACK_NAME", None)
    # define "pack_name" in config_vars
    ANIM_PACK_NAME = os.environ.get("ANIM_PACK_NAME", None)
    # MIRRORACE STUFF
    MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
    MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_TOKEN", None)
    #
    RAVANA_LEELA = os.environ.get("RAVANA_LEELA", None)
    # spotify stuff
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)
    SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    # MongoDB
    MONGO_URI = os.environ.get("MONGO_URI", None)
    # define the "types" that should be uplaoded as streamable
    TL_VID_STREAM_TYPES = ("MP4", "WEBM")
    TL_MUS_STREAM_TYPES = ("MP3", "WAV", "FLAC", "M4A")
    TL_FF_NOAQ_TYPES = "WEBP"
    # Uthob
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    # For Lol
    API_TOKEN = os.environ.get("API_TOKEN", None)
    THUMB_IMG = os.environ.get(
        "THUMB_IMG", "https://telegra.ph/file/c9377de879b53bc72b4ed.jpg"
    )
    # BOTLOG
    BOTLOG = os.environ.get("BOTLOG", None)
    if BOTLOG:
        BOTLOG = int(BOTLOG)
    # For a Shitty Module
    KUTT_IT_API_KEY = os.environ.get("KUTT_IT_API_KEY", None)
    # lyrics plugin
    GENIUS = os.environ.get("GENIUS_API_TOKEN", None)
    #
    USER = os.environ.get("USER", None)
    # For watch module
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", None)
    # Deeer ARL Token
    DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))
    BOTLOOG = sb(os.environ.get("BOTLOOG", "True"))
    # SpamWatch Api
    SPAM_WATCH_API = os.environ.get("SPAM_WATCH_API", None)
    SPAM_WATCHAPI = os.environ.get("SPAM_WATCHAPI", None)
    # Uptobox
    USR_TOKEN = os.environ.get("USR_TOKEN_UPTOBOX", None)
    # for video trimming and screenshot plugins
    LT_QOAN_NOE_FF_MPEG_CTD = os.environ.get("LT_QOAN_NOE_FF_MPEG_CTD", None)
    LT_QOAN_NOE_FF_MPEG_URL = os.environ.get("LT_QOAN_NOE_FF_MPEG_URL", None)
    #Deep AI
    DEEP_AI = os.environ.get("DEEP_AI", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
