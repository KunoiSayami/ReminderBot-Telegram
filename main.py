# -*- coding: utf-8 -*-
#
#This source code was published under GPL v3
#
#Copyright (C) 2017 Too-Naive
#
import telepot
import time
from config import botToken,sqlhost,sqlport,sqluser,sqlpwd,sqlname
import sys
from mysqlmodule import mysqlModule as mm
import datetime

bot = None

regular = re.compile(ur"(\(1\/2\))?订单E\d{9},.+您已购(\d+)月(\d+)日([CGDTZK]?\d+)次(\d+)车(\d+[A-F])号(、\d+[A-F]号)?(、\d+[A-F]号)?(、\d+[A-F]号)?(、\d+[A-F]号)?(.+)(\d+:\d+)开")

def datetimeFromNow(timestamp):
	return datetimeFromNowEx(datetime.datetime.now(),timestamp)

def datetimeFromNowEx(timestampnow,timestamp):
	return (timestampnow.replace(microsecond=0)-timestamp.replace(microsecond=0)).total_seconds()


def main():
	global bot
	bot = telepot.Bot(botToken)
	bot.message_loop(onMessage)
	while True:
		bot.getMe()
		time.sleep(10)


def init():
	reload(sys)
	sys.setdefaultencoding('utf8')


def onMessage(msg):
	global bot

	content_type, chat_type, chat_id = telepot.glance(msg)
	if chat_type != 'private' or content_type!= 'text':
		return
''' code for test
	ret = bot.sendMessage(chat_id,'Plz, wait')
	time.sleep(3)
	ret = bot.editMessageText((chat_id,ret['message_id']),msg['text'])
	time.sleep(3)
	bot.deleteMessage((chat_id,ret['message_id']))
	print(ret)
'''


if __name__ == '__main__':
	init()
	main()