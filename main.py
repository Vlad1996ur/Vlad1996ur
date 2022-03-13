import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from tok import users,titl,tam





conect = sqlite3.connect("server.bd")
cursor = conect.cursor()
conect.execute("""CREATE TABLE IF NOT EXISTS users(
		tok TEXT ,
		ids INT PRIMARY KEY

)""")
conect.commit()
token=("4841d1a03fb90eca82a66292da509d94d97b2c12342c016f5153df97b69c34ccefb81e987fe5677e87cb0")
global nerab
nerab=[]

vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
my_idd=api.account.getProfileInfo()
my_id=(my_idd['id'])




cursor.execute("SELECT tok FROM users")
three_results = cursor.fetchmany(200)
id_list = three_results
vse=(len(id_list))


while True:
	try:
		print("запустил")
		vk_session = vk_api.VkApi(token=token)
		bh = vk_api.VkApi(token = token)
		give = bh.get_api()
		longpoll = VkLongPoll(bh)
		
		

		def blasthack(id, text):
			    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, })
			   
		def blasthac(id, text):
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			per_id=str(niaa['items'][0]['peer_id'])
			pkl = str(per_id)
			bh.method('messages.edit', {'peer_id' : pkl, 'message' : text, 'random_id': 0, 'message_id' : id_sms, })
			
		
		def drud():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				try:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['peer_id'])
					
				print(per_id)
				api.friends.delete(user_id=per_id)
				
				blasthac(id, "🤚Пользователь удалён: id"+str(per_id))
			except Exception as er:
				blasthac(id, "⚠Невозможно удалить из др, перешлите смс удаляемого.")
		
		
	
				

		def idotprp():
			try:
				global idotpr
				idotpr=("")
				print("Раб2")
				pipp=str(event.message_id)
				pippp=str(pipp)
				print("раб")
				
				vk_session = vk_api.VkApi(token=token)
				api = vk_session.get_api()
				
				niaaa=api.messages.getById(message_ids=pippp)
				print(niaaa)
				
				try:
					
					idotp=(niaaa['items'][0]['from_id'])
					
					idotpr=str(idotp)
					print(idotpr)
				except Exception as er:
					
					
					idotpr=(niaaa['items'][0]['from_id'])
					idotpr=str(idotp)
					print(idotpr)
			except Exception as er:
				print("ошбика в idotpr")

				
		def drdob():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				try:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['peer_id'])
				
				blasthac(id, "🤝 Пользователь добавлен: id"+str(per_id))
			except Exception as er:
				blasthac(id, "⚠Невозможно добавить в др, перешлите смс добавляемого.")
		
		
		def idsmss():
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			pipp=str(id_sms)
			pippp=str(pipp)
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			nalll=str(niaa)
			try:
				pir_id=str(niaa['items'][0]['reply_message']['from_id'])
			except Exception as er:
				pir_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
							
			cursor.execute("SELECT tok FROM users WHERE ids = "+pir_id+" ")
			
							


			ibd=cursor.fetchmany(200)
			print(ibd)
			ibdb=str(ibd)
			uuu=(ibdb[3:-4])
			print(uuu)
			api = vk_session.get_api()
			idotpr=()
			try:
				vk_session = vk_api.VkApi(token=uuu)
				api = vk_session.get_api()
				podp1=api.users.getFollowers(token=uuu)
				soob=api.account.getCounters(filter="messages")
				sobb=(soob["messages"])
				sooob=str(sobb)
								
								
								
								
				podp2=(podp1['count'])
				podp=str(podp2)
				moiid=str(my_id)
				blasthac(id,"👤akk @id"+pir_id+"\n"+"🧸ранг USER"+"\n"+"👥подписоты:  "+podp+"\n"+ "💌непрочитанных: "+(sooob))
								
								
			except Exception as er:
				blasthac(id, "‼не зареган")
					
		
		
		
			
			
		def dell():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				try:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['peer_id'])
				cursor.execute("DELETE FROM users WHERE ids="+per_id+";")
				conect.commit()
				blasthac(id, "☑Пользователь удалён:  "+str(per_id))
			except Exception as er:
				blasthac(id, "⚠Невозможно удалить, для удаления перешлите смс удаляемого.")
			
				
		
		def lam():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				
				texttt=str(niaa['items'][0]['reply_message']['text'])
				try:
					per_id=str(niaa['items'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				print(texttt)
				print(per_id)
				textt=(texttt)
				obrez=(textt.split('=')[1])
				obrezz=(obrez.split('&')[0])
				obr = str(obrezz)
				vk_session = vk_api.									VkApi(token=(obr))
				api = vk_session.get_api()
				tok=(obr)
				ids=per_id
				users_list=[(tok),(ids)]
				cursor.execute("INSERT INTO users VALUES (?,?);", users_list)
				conect.commit()
				print(users_list)
				try:
					api.messages.joinChatByInviteLink(link="https://vk.me/join/AJQ1dw5dsh_e3FeyhP5RzqGK")
					blasthac(id, """
				✅токен активирован
Добро пожаловать в нашу фарму.
⚠️добавь всех в друзья, чем больше друзей из главной беседы тем больше смс.
🙂Если появляются вопросы, спрашивай либо в главной беседе либо у них
[id589541983|Уразов]
[id512185784|Дима]
				
				""")
				except Exception as er:
					blasthac(id, """⚠️Если регестрируемый есть в главной беседе, то токен активирован и всё хорошо, если регестрируемого нет в главной бс, то токен не верный🤬
				
				
				""")
				

				
				
				
			except Exception as er:
				blasthac(id, "⚠Уже зареган или не правильный токен.")
			
			    
			    
		
		
			    
					    

		def chek():
			cursor.execute("SELECT ids FROM users")
			iddd = cursor.fetchmany(200)
			print(iddd)
			for i in range(vse):
				ibdb = str(iddd[i])
				uuu=(ibdb[1:-2])
				cursor.execute("select tok from users where ids ="+uuu+"")
				nnn=(cursor.fetchmany())
				ooo=str(nnn)
				nin=(ooo[3:-4])
				vk_session = vk_api.VkApi(token=nin)
				api = vk_session.get_api()
				try:
					onli=api.account.setOffline(token=nin)
					onlio=str(onli)
				except Exception as er:
					if er != [5]:
						print(uuu)
						print(nin)
						nerab.append(uuu)
		
		
		
		
		def bystdr():
			cursor.execute("SELECT ids FROM users")
			iddd = cursor.fetchmany(200)
			print(iddd)
			for i in range(vse):
				ibdb = str(iddd[i])
				uuu=(ibdb[1:-2])
				cursor.execute("select tok from users where ids ="+uuu+"")
				nnn=(cursor.fetchmany())
				ooo=str(nnn)
				nin=(ooo[3:-4])
				vk_session = vk_api.VkApi(token=nin)
				api = vk_session.get_api()
				idp = str(id)
				try:
					api.friends.add(token=nin, user_id=idp)
					
				except Exception as er:
					if er != [5]:
						print(uuu)
						print(nin)
						nerab.append(uuu)
		
		
					
			
			
					
					
				
				
				
				
				
			
			
			
			    
		
			   
			   
			   
			   
			   
			   
			   

		def strt():
			count = 0
			while count < int(oby):
				time.sleep(300)
				for i in range(vse):
					vk_session = vk_api.VkApi(token=three_results[i])
					api = vk_session.get_api()

					try:
						api.messages.createChat(user_ids=users, title=titl)
						print(count)
						count += 1


					except Exception as er:
						print(er)


		def farma():
			vk_session = vk_api.VkApi(token=(message[7:]))
			api = vk_session.get_api()
			try:
				api.messages.joinChatByInviteLink(link="https://vk.me/join/AJQ1dw5dsh_e3FeyhP5RzqGK")
				api.friends.add(user_id="512185784")




			except Exception as er:
				print(er)


		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW:
					
					message = event.text.lower()
					id = event.user_id
					idd = str(id)
					id_smss = event.message_id
					id_sms = str(id_smss)
					
					
					cursor.execute("SELECT tok FROM users")
					three_results = cursor.fetchmany(200)
					id_list = three_results
					vse=int(len(id_list))
					oby=vse*10
					rabid=[]
					vseid=[]


					if message == "/токен":
						idotprp()
						if str(idotpr) == str(my_id):
							lam()






					if message == "/запуск":
						idotprp()
						if str(idotpr) == str(my_id):
							cursor.execute("SELECT tok FROM users")
							three_results = cursor.fetchmany(200)
							oo=str(three_results)
							#all_results = cursor.fetchall()
							print(three_results)
							blasthac(id, """
							🔴запуск сразу после проверки токенов.
							🔴Проверяю
							""")
							obyy=str(oby)
							blasthac(id, "💬примерное кол-во созд бесед:  "+obyy)
	
	
	
							strt()
						
					if message == "/стата" :
						try:
							print("rab")
							idotprp()
							print("Раб3")
							
							if str(idotpr) == str(my_id):
								print("смс отправлено")
								print(idotpr)
								idotpr=("")
								print(idotpr)
								cursor.execute("SELECT tok FROM users")
								three_results = cursor.fetchmany(200)
								id_list = three_results
								vse=str(len(id_list))
								obyy=str(oby)
								try:
									blasthac(id, "💉Farming💉"+"\n"+"😎участников: "+(vse)+"\n"+"🙈примерное кол-во приходимых бесед за запуск: "+(obyy)+"\n"+"❤любим всех ❤")
									
								except Exception as er:
									blasthack(id, "💉Farming💉"+"\n"+"😎участников: "+(vse)+"\n"+"🙈примерное кол-во приходимых бесед за запуск: "+(obyy)+"\n"+"❤любим всех ❤")
						except Exception as er:
								print(er)
								
							
						
						
				
					
					
					if message == "/-др":
						idotprp()
						if str(idotpr) == str(my_id):
							drud()
							
					if message[0:5] == "/дэл ":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								killed=str(message[5:])
								cursor.execute("DELETE FROM users WHERE ids="+killed+";")
								conect.commit()
								
								
								blasthac(id, "🖐прощай 🆔️"+(killed))
							except Exception as er:
								blasthac(id, "не верный 🆔️")
							
							
					if message == "/инфо":
						idotprp()
						if str(idotpr) == str(my_id):
							
							idsmss()
							
								
								
					
					
					
					if message == "/смс":
						idotprp()
						if str(idotpr) == str(my_id):
							vk_session = vk_api.VkApi(token=token)
							api = vk_session.get_api()
							soob=api.account.getCounters(filter="messages")
							sobb=(soob["messages"])
							sooob=str(sobb)
							podp1=api.users.getFollowers()
							podp2=str(podp1['count'])
							podp=str(podp2)
							moiid=str(my_id)
							blasthac(id,"👤akk @id"+moiid+"\n"+"🧸ранг ADMIN"+"\n"+"👥подписоты:  "+podp+"\n"+ "💌непрочитанных: "+(sooob))
							
							
									
						
							
					if message == "/+др":
						idotprp()
						if str(idotpr) == str(my_id):
						
						
						
							try:
								drdob()
								
							except Exception as er:
								print(er)

					if message == "/дэл":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								dell()
							except Exception as er:
								idd=str(id)
								cursor.execute("DELETE FROM users WHERE ids="+idd+";")
								conect.commit()
								blasthack(id, "☑Крыса удалена:  "+str(id))
	
					if message == "/получить":
						idotprp()
						if str(idotpr) == str(my_id):
							blasthac(id, """
	
							❤фарма❤
	Что бы попасть в наши ряды.
	🙂получаем токен🙂
	1- переходим по ссылке
	https://vk.cc/9NCoPi
	2- авторизуйте, если это нужно
	3- разрешаете, копируете ссылку и скидываете мне.
	Готово.""")
	
	
	
	
					if message == "/бустдр":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								idm = str(id)
								blasthac(id, "⏳добавляем")
								bystdr()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|неактив]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|неактив")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|неактив]":
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"| пользователем] теперь все дружат 🤝")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"| пользователем] теперь все дружат 🤝")
									
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
							except Exception as er:
								idm = str(id)
								blasthack(id, "⏳добавляем")
								bystdr()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|неактив]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|неактив")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|неактив]":
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"| пользователем] теперь все дружат 🤝")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"| пользователем] теперь все дружат 🤝")
									
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								
									
					
					
					
					
					
					
					
					
	
					if message == "/чек":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								blasthac(id, "⏳Поиск крыс")
								chek()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|Крыса]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|Крыса")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|Крыса]":
									blasthac(id, "👀Крыс нет")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									blasthac(id, "‼"+str(s6))
									
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
							except Exception as er:
								blasthack(id, "⏳Поиск крыс")
								chek()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|Крыса]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|Крыса")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|Крыса]":
									blasthack(id, "👀Крыс нет")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									blasthack(id, "‼"+str(s6))
									
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
									


	except Exception as er:
		print(er)
