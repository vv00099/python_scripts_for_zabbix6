import os
import json

'''
Zabbix запускает этот скрипт как внешную проверку
с интервалом 20-30с и реагирует на ответ "ALERT"
Скрипт ищет в указанном лог файле rsyslog сервера
строку "Failed to send SIP message", означающую
проблемы в его работе sip телефона, 
что требует перезагрузки телефона.
В этом случае передается значение "ALERT"
Пока телефон не будет презагружен, дальнейшие подобные
ошибки систему монтиоринга не интересуют, поэтому
следующие сообщение с ошибкой отправляются с другим значением.
Это состояние сохраняется во внешнем json файле
'''
#Нужно перед использованием отредактировать пути

state = { 'found_sip_error' : None,
          'sent_alert' : False}
try:
	with open("/home/user/last_state.json") as file_load:
		state = json.load(file_load)
except FileNotFoundError:
	pass
	
last_data_log = os.popen("tail -n 5 /home/user/sip.log")

for line in last_data_log:
	if "Failed to send SIP message" in line:
		state["found_sip_error"] = True		
	if "System will reboot" in line:
		state["found_sip_error"] = False
		state["sent_alert"] = False
		
if state.get("found_sip_error") == True:
	if state.get("sent_alert") == False:
		print("ALERT")
		state["sent_alert"] = True
	else:
		print("REPEAT ALERT")
else:
	print("OK")

try:
	with open ("/home/user/last_state.json", "w") as file_save:
		json.dump(state, file_save)
except FileNotFoundError:
	os.system("touch /home/user/last_state.json")
	with open ("/home/user/last_state.json", "w") as file_save:
		json.dump(state, file_save)
