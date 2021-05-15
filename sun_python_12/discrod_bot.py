import discord

TOKEN = 'ODM1ODA5NjI2NTY0ODUzNzcx.YIU2Xw.2fzVEi9OxF_8_zJ9JjJWdNzxcws'
# какие сообщения могут прийти от человека
message_1 = ['привет', 'ку', 'hello', 'hi']

# хранится наш бот
client = discord.Client()

# отслеживает событие "сообщение"
@client.event
async def on_message(message):
	# не отвечает на сообщения ботов
	if message.author.bot == True:
		return
	
	# печатает в консоль сообщения
	print(f'--- автор: {message.author} | сообщение: {message.content} | канал: {message.guild} ---')
	
	if set(message_1) & set(message.content.split()):
		# отправляет сообщения
		await message.channel.send('КУ-КУ')
		
	elif 'как дела' in message.content:
		# отправляет сообщения
		await message.channel.send('норм')
		
	else:
		await message.channel.send('Ошибкка понимания сов... 404')

# запускаем бота
client.run(TOKEN)
