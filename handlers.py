#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################
#                         BovineBot                               #
#                        Aman  Kumar                              #
###################################################################


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import logging
import random
from datetime import datetime
import config
import util

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    # Updated timesince
    util.timesince_updater(update.message.from_user['username'])

    # Handle /start
    logger.info('/start: Handling /start response')
    logger.info("Request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    update.message.reply_text(util.random_reply())

def error(bot, update, error):
    # Handle erros
    logger.warning('Update "%s" caused error "%s"', update, error)

def hi(bot, update):
    
    logger.info("/hi: Handling /hi request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    update.message.reply_text(util.random_reply())

def all_text(bot, update):
    # Handle all text messages received

    logger.info("all_text: Received text message from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
   
    message_text = update.message.text

    util.timesince_updater(update.message.from_user['username'])
    
    # TODO: Handle this through custom filters
    if(message_text == 'hi' or message_text == 'Hi'):
        hi(bot, update)

def all_sticker(bot, update):
    # Handle all text messages received
    logger.info("all_sticker: Received Sticker Message from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    util.timesince_updater(update.message.from_user['username'])

def superpower(bot, update):
    # Handle /timesince
    logger.info("/superpower: Handling /superpower request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    response = "🇮🇳🙏 Time Until Super Power™️: " + util.superpower_countdown_calc() + " 🙏🇮🇳"
    update.message.reply_text(response)

def lenny(bot, update):
    # Handle /lenny
    logger.info("/lenny: Handling /lenny request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    response = "( ͡° ͜ʖ ͡°)"
    update.message.reply_text(response)

def lazypay(bot, update):
    # Handle /lazypay
    logger.info("/lazypay: Handling /lazypay request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    response = "Lazypay Leaderboard:\nKesava: 7000 \nAjay: 5050 \nNikhil: 3000 \nAvi: 2500 but won't KYC \nAkshay: 1200 \nDV & Sherlock: Rejected \nTerra and Rahul: Won't apply \nArthur: Too lazy to apply "
    update.message.reply_text(response)
def credit(bot, update):
    # Handle /credit
    logger.info("/credit: Handling /credit request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)
    response = "Experian Leaderboard:\nArthur: 876 \nSherlock: 856 \nKesava: 840 \nAvi: 800 \nAkshay: BPL \nAjay: BPL"
    update.message.reply_text(response)

def slap(bot, update):
    # Handle /slap
    logger.info("/slap: Handling /slap request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)

    query_username = update.message.text
    query_username = query_username[6:]

    response = query_username + " got slapped really hard and wet his bed like Ajay."
    update.message.reply_text(response)

def timesince(bot, update):
    # Handle /timesince
    logger.info("/timesince: Handling /timesince request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)

    query_username = update.message.text
    query_username = query_username[11:]

    if len(query_username) == 0:
        logger.info('/timesince: Input format was wrong.')
        update.message.reply_text("Reply with a username - /timesince @themusketeer")
    else:
        logger.info("/timesince: Query for: " + query_username)
        response = util.timesince_query(query_username)

        if response == "404":
            logger.info("/timesince: Couldn't find user")
            file_id = 'CAADAQADfAEAAp6M4Ah03h6oF-p4GwI'
            sticker_to_send = file_id
            update.message.reply_sticker(sticker=sticker_to_send)
        else:
            logger.info("/timesince: Sending response " + response)
            update.message.reply_text(response)
    
    # Updating timesince
    util.timesince_updater(update.message.from_user['username'])

#def tts(bot, update):
    # Handle /timesince
    #logger.info("/tts: Handling /tts request from user '%s' in group '%s'", update.message.from_user['username'], update.message.chat.title)

    #query = update.message.text
    #query = query[5:]
 #   logger.info('/tts query size: %s. query text: %s', len(query), query)

 #   if len(query) == 0:
 #       query = "Hey " + str(update.message.from_user['username']) + " I need an input!"

 #   if len(query) < 1000:

#        file_to_send = util.tts_util(query)

 #       if file_to_send is not None:
 #           update.message.reply_voice(voice=open(file_to_send, 'rb'), timeout=5000)

 #   else:
 #       logger.warn('/tts: tts query is too long!')
 #       update.message.reply_text("HAAAAAT! Your tts query is too long!")