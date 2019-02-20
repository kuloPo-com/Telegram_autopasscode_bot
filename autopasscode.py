import time
import telepot
from telepot.loop import MessageLoop

dic = {}
result = {}

def output(data):
	res = ''
	res += 'var jq = document.createElement(\'script\');\njq.src = "https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js";\ndocument.getElementsByTagName(\'head\')[0].appendChild(jq);\n\n'
	res += 'pass = [\n'
	for input in data:
		for code in input:
			if code != '':
				res += "'"
				res += code
				res += "',\n"
	res += '];\n\n'
	res += 'pass.forEach(function(pass,i) {\n  setTimeout(function() {\n    console.log(\'enter passcode:\', pass, i);\n    $(\'#passcode\').val(pass);\n    $(\'#submit\').click()\n  },i*3000);\n});'
	return res
	
def handle(msg):
	try:
		content_type, chat_type, chat_id = telepot.glance(msg)
	except:
		print("Network Error")
		return
	if content_type == 'text':
		txt = msg['text']
		if (txt=='/start'):
			if (dic.get(chat_id) == True):
				bot.sendMessage(chat_id, 'Already started!')
			else:
				dic[chat_id] = True
				bot.sendMessage(chat_id, 'Now please forward the codes. If finished , type /end')
				result[chat_id] = []
				print(msg['from']['username'], " ",msg['from']['last_name'], " ", chat_id)
		elif (txt=='/end'):
			if (dic.get(chat_id) != True):
				bot.sendMessage(chat_id, 'Not started!')
			else:
				bot.sendMessage(chat_id, output(result[chat_id]))
				result.pop(chat_id)
				dic.pop(chat_id)
		elif (dic.get(chat_id) == True):
			result[chat_id].append(txt.split('\n'))

TOKEN = 'YOUR TOKEN HERE'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
	time.sleep(1)