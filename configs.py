# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

from dotenv import load_dotenv
load_dotenv()
class Config(object):
    API_ID = int(os.environ.get("API_ID", "18860540"))
    API_HASH = os.environ.get("API_HASH", "22dd2ad1706199438ab3474e85c9afab")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5995955628:AAHUCApxLZh2wjvEc8E2JTsw-Alo1bPYwTY")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID",5123176772))
    PRO_USERS = list({int(x) for x in os.environ.get("PRO_USERS", "0").split()})
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://abc:abc@cluster01.98xu6iz.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001877778076))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    FROM_CHANNEL = int(os.environ.get("FROM_CHANNEL", -1001877778076 ))
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL",-1001841380840))
    CH_USERNAME = os.environ.get("CH_USERNAME", "@seaofallmovies")
    TAG = os.environ.get("TAG", "💥Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ💥 ❤️ @seaofallmovies❤️")
    REMOVE_WORD = os.environ.get("REMOVE_WORD", "💥|TeamCinepleX|MKVMAX|🫀|MovieKhorMovieSeriesZone|HINDI_HD_MOVIES24|mkvMax|akatsuki|media|OmfooMoviesNetwork|Sun|George|Eliteflix|New_Movies_1stOnTG|BOB_FILES|BOB|Saurabh|saurabh_1710|❣|Akatsuki_Media|TapOrginals|YourDemandZone|GoblinInHindi|The_4x_Team|🎯|𝗝𝗼𝗶𝗻|Saurabh_Gadre9096|\[|\]|\~|FILMY_MEN|Gmovies_Hub|Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ|❤️|SIDHUU5911|BuLMoviee|Join Us On Telegram|JESSEVERSE|Jesseverse|_Join_Us_On_Telegram_|Theprofffesorr|Latest_Movies_Reborn|@|Latest_Movies_1stOnNet|Hindi_Fhd_Movies|Backup channel|File Uploaded Here|https|http|:|/|t.me|Quality_HD|Hindi_FHd_Movies|Latest_Movies_FreeOnNet|Uploaded by|🔰|Uᴘʟᴏᴀᴅᴇᴅ Bʏ|JOIN|SUPPORT|♻️|F-Press|Movies_1stOnTG|https|For New Movies|Most_popular_movies|Grand_Release|seaofallmovies|Netflix_Villa_Original|Latest_Movies|Latest|Movies|Reborn|🎗|✯|𝑈𝑃𝐿𝑂𝐴𝐷𝐸𝐷 𝐵𝑌|➩|MAPOriginals|⚡️|Join|:-|BlackDeath_0|Enjoy Guys & Share Your Friends!|Movie Request Group|Mix_Cinema_Box|Backup")#multiple word is must be seperated by |
    REMOVE_CAPTION = os.environ.get("REMOVE_CAPTION", "💥|TeamCinepleX|MKVMAX|🫀|MovieKhorMovieSeriesZone|HINDI_HD_MOVIES24|mkvMax|akatsuki|media|@OmfooMoviesNetwork|Sun|George|Eliteflix|New_Movies_1stOnTG|BOB_FILES|BOB|Saurabh|saurabh_1710|❣|Akatsuki_Media|TapOrginals|YourDemandZone|GoblinInHindi|The_4x_Team|🎯|𝗝𝗼𝗶𝗻|💥|\[|\]|\~|Saurabh_Gadre9096|Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ|FILMY_MEN|Gmovies_Hub|❤️|SIDHUU5911|BuLMoviee|Join Us On Telegram|JESSEVERSE|Jesseverse|_Join_Us_On_Telegram_|Theprofffesorr|Latest_Movies_Reborn|@|Latest_Movies_1stOnNet|Hindi_Fhd_Movies|Backup channel|File Uploaded Here|https|http|:|/|t.me|Quality_HD|Hindi_FHd_Movies|Latest_Movies_FreeOnNet|Uploaded by|🔰|Uᴘʟᴏᴀᴅᴇᴅ Bʏ|JOIN|SUPPORT|♻️|F-Press|Movies_1stOnTG|https|For New Movies|Most_popular_movies|Grand_Release|seaofallmovies|Netflix_Villa_Original|Latest_Movies|Latest|Movies|Reborn|🎗|✯|𝑈𝑃𝐿𝑂𝐴𝐷𝐸𝐷 𝐵𝑌|➩|MAPOriginals|⚡️|Join|:-|BlackDeath_0|Enjoy Guys & Share Your Friends!|Movie Request Group|Mix_Cinema_Box|Backup")#multiple word is must be seperated by |
    DP_PASTE = os.environ.get("DP_PASTE",True)#do True if u want paste ur thumnail on video default thumbnail
    START_FROM = int(os.environ.get("START_FROM",28370))
    DB_NAME = os.environ.get("DB_NAME","Rename-Bot")
    BOTTOM_HEIGHT_CROP = int(os.environ.get("BOTTOM_HEIGHT_CROP",60))
    RIGHT_WIDTH_CROP = int(os.environ.get("RIGHT_WIDTH_CROP",0))          
    LEFT_WIDTH_CROP = int(os.environ.get("LEFT_WIDTH_CROP",0))
    TOP_HEIGHT_CROP = int(os.environ.get("TOP_HEIGHT_CROP",0))
