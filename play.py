import telegram

token = "5149919236:AAGbSkGDR32-9HxzDf6NJ5TpPaXwyEt7geo"

# 5387730578
# 81980522
bot = telegram.Bot(token)
updates = bot.getUpdates()

for i in updates:
    print(i.message)


#bot = telegram.Bot(token)
#bot.sendMessage(chat_id=5149919236, text="안녕하세요. 저는 봇입니다.")