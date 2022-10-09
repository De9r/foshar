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
async def start(app, message):
	i = message.from_user.id #يجيب الايدي
	await app.send_message(message.chat.id,
	"""مرحبا بك عزيزي في بوت الافلام
البوت يبحث عن الفيلم ويجيب كل معلوماته وروابط الاحميل بثلاث انواع
- البوت للافلام فقط وليس المسلسلات
- ارسل اسم الفيلم فقط مع التأكد من اسمه
""",reply_to_message_id=message.id)
	
	
@app.on_message(filters.text) #يقرة كل الرسائل
async def text(app,message):
	ms = message.text #الرسالة
	reply = message.reply_text #يرد عالرسالة
	mention = message.from_user.mention #منشن
	start_text = message.text.startswith

	msgs = ms.replace(" ","-").replace(".","").replace(":","-").replace("A","a").replace("S","s").replace("Q","q").replace("W","w").replace("E","e").replace("R","r").replace("T","t").replace("Y","y").replace("U","u").replace("I","i").replace("O","o").replace("P","p").replace("D","d").replace("F","f").replace("G","g").replace("H","h").replace("J","j").replace("K","k").replace("L","l").replace("Z","z").replace("X","x").replace("C","c").replace("V","v").replace("B","b").replace("N","n").replace("M","m")
	url = requests.get("https://apis.karman.ml/v1/fushaar/?search="+msgs+"&token=5578804926:AAEJikC0t68N50ftl0w-o4pOJ56e21L0yZ8").json()
	imdb = requests.get("https://apis.karman.ml/v1/imdb/?search="+msgs+"&token=5578804926:AAEJikC0t68N50ftl0w-o4pOJ56e21L0yZ8").json()
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
		await app.send_photo(
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
		await app.send_message(message.chat.id,
		"تأكد من اسم الفيلم.",
		reply_to_message_id=message.id
		)
			
			
#bot.delete_messages(message.chat.id,message.id) #يحذف رسالة
	
app.run()