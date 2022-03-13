import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import vk


token ="c063e76ac3008240b9a5d941fb5b6a0165d2e8d7973c4a987faa633a85374989188a7f68c86ddd2e3d50c"

vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
t = api.messages.getChat(chat_id="49291")
p = (t["users"])
q = str(p)
users=(q[1:-1])

titl="❤❤❤"



tam=1800
print(users)