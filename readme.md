
gdy w gui nadejdzie jakies zdarzenie to client opakowujacy gui wysyla rzadanie pod adres localhost:5000/request
request trafia do flaska ktory w widoku tworzy nowe zdarzenie i pakuje je do kolejki zdarzen
kontroler biegajacy w watku wyjmuje z kolejki i updateuje model

www.py odpali kontroler i bedzie obslugiwalo flaska, zainicjuje kontroler kolejka zdarzen

uruchamianie programu:
$ python www.py
w drugiej konsoli:
$ python client/client.py

