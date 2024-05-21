import subprocess

#Скрипт проверяет значение reallocated sector count в S.M.A.R.T
#и добавляется в юзер параметр zabbix агента


#Предварительно нужно установть smartmontools

cmd = ("C:\\smartmontools\\bin\\smartctl.exe -s on -a /dev/sda | findstr Reallocated_Sector")
data = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
#Считываем последнее число в строке вывода
cut_data = data.stdout[-5:-1]
clear_data = int(cut_data.strip())

print(clear_data)
