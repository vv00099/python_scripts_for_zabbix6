#!/usr/bin/python3

import sys

#Скрипт проверяет значение reallocated sector count в S.M.A.R.T
#и добавляется в юзер параметр zabbix агента


#Предварительно нужно установть apt install smartmontools
#Запуск через
#sudo smartctl -s on -a /dev/sda | grep Reallocated_Sector_Ct | ./smart.py

data = sys.stdin.read()
cut_data = data[-5:-1]
clear_data = int(cut_data.strip())

print(clear_data)
