from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.types import Message
import asyncio,os,requests

# filters.private              #بالخاص
# filters.supergroup     #بالكروب

###################################
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
token = os.environ.get("TOKEN")
app = Client("movie", bot_token=token, api_id = api_id, api_hash = api_hash)
###################################

@app.on_message(filters.command('start')) #يقرة الاوامر
async def start(bot, message):
	i = message.from_user.id #يجيب الايدي
	await msg = bot.send_message(message.chat.id,"اهلا بك في بوت البحث في موقع فشار",reply_to_message_id=message.id)
	msg.edit("اهلا بك في بوت البحث في موقع فشار..")
	msg.edit("""اهلا بك في بوت البحث في موقع فشار... 
اكتب /movie وبعده اسم الفيلم بأحرف سمول فقط
وانتبه اذا بالاسم فراغ خلي بدل الفراغ - 
""")
	
	
@app.on_message(filters.text) #يقرة كل الرسائل
async def text(bot,message):
	ms = message.text #الرسالة
	reply = message.reply_text #يرد عالرسالة
	mention = message.from_user.mention #منشن
	start_text = message.text.startswith
	
	if start_text("/movie "):
		msgs = message.text.split()[1]
		url = requests.get("https://apis.karman.ml/v1/fushaar/?search="+msgs+"&token=5578804926:AAEJikC0t68N50ftl0w-o4pOJ56e21L0yZ8").json()
		imdb = requests.get("https://apis.karman.ml/v1/imdb/?search="+msgs+"&token=5578804926:AAEJikC0t68N50ftl0w-o4pOJ56e21L0yZ8").json()
		print(msgs)
		try:
			photo = url["photo"][0]
			title = url["title"][0]
			cap = url["des"]
			q240 = url["q240"]
			q480 = url["q480"]
			q1080 = url["q1080"]
			year = imdb["Year"]
			runtime = imdb["Runtime"]
			tqyam = imdb["Genre"]
			rate = imdb["imdbRating"]
			titl = imdb["Title"]
			me_ch = [
				[
					InlineKeyboardButton("مشاهدة بدقة q240",url=q240),
					InlineKeyboardButton("مشاهدة بدقة q480",url=q480)
				],
				[
					InlineKeyboardButton("مشاهدة بدقة q1080",url=q1080)
				],
				[
					InlineKeyboardButton("المطور",url="t.me/jj8jjj8")
				]
			]
			markup = InlineKeyboardMarkup(
			me_ch
			)
			bot.send_photo(
			message.chat.id,
			photo,caption=
			f"""اسم الفيلم: {titl}
النوع: {tqyam}
تقييم: {rate}
المدة: {runtime}
سنة: {year}

القصة: {cap}


@cn_world
""",
reply_to_message_id=message.id,reply_markup=markup)
		except:
			bot.send_message(message.chat.id,
			"تأكد من اسم الفيلم.",
			reply_to_message_id=message.id
			
			)
			
			
#bot.delete_messages(message.chat.id,message.id) #يحذف رسالة
	
bot.run()