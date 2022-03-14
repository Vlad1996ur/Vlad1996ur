import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import vk


token ="76ac68762b76aced60a8136369e2006ed1610806edf9c6f3eb8b244d26cd3783d924b4304610ba42b6a9e")"

vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
t = api.messages.getChat(chat_id="49291")
p = (t["users"])
q = str(p)
users=(q[1:-1])

titl="❤❤❤"



tam=1800
print(users)
