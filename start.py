# lista = [2, 4, 7]
# print (lista)
#
# lista = [2,
#          4,
#          7]
# print (lista)

#lista = [2, 4, 7, "aaa", "true", ]
# zmienna = 30
# print(zmienna)
# print(type(zmienna))

# zmienna = 30.4
# print(zmienna)
# print(type(zmienna))

# zmienna = False
# print(zmienna)
# print(type(zmienna))

# zmienna = "abc"
# print(zmienna)
# print(type(zmienna))

# zmienna = [1, 7]
# print(zmienna)
# print(type(zmienna))

# zmienna = {1, 7}
# print(zmienna)
# print(type(zmienna))
# lista = [2, 4, 7.2,
#          "aaa", True ]
# print(lista)

# slownik = {"liczba": 2,
#            "tekst": "aaa",
#            "prawda": True,
#            "falsz": False
#            }
# print (slownik)

# litery = ["a", "b"]
# slownik = {"liczba": 2,
#            "lista": litery,
#            "prawda": True,
#            "falsz": False}
# print(slownik)

# litery = {"pierwsza": "a", "druga": "b"}
# slownik = {"liczba": 2,
#            "lista": litery,
#            "prawda": True,
#            "falsz": False}
# print(slownik)

# import json
# litery = {"pierwsza": "a", "druga": "b"}
# slownik = {"liczba": 2,
#            "lista": litery,
#            "prawda": True,
#            "falsz": False}
# print(slownik)
# json_string = json.dumps(slownik)
# print (json_string)


# import json
# litery = {"pierwsza": "a", "druga": "b"}
# slownik = {"liczba": 2,
#            "lista": litery,
#            "prawda": True,
#            "falsz": False}
# print(slownik)
# json_string = json.dumps(slownik, indent=4)
# print (json_string)

# import json
# litery = {"pierwsza": "a", "druga": "b"}
# slownik = {"liczba": 2,
#            "lista": litery,
#            "prawda": True,
#            "falsz": False}
# print(slownik)
# json_string = json.dumps(slownik, indent=4, sort_keys=True)
# print (json_string)

# import json
# litery = {"pierwsza": "a", "druga": [7, 77, 777, 7777]}
# slownik = {"liczba": 2,
#            "owoc": "gruszka",
#            "warzywo": "pomidor",
#            "lista": litery,
#            "prawda": True,
#            "falsz": False,
#            "numery": [3, 4, 5, 100]}
# json_string = json.dumps(slownik, indent=4, sort_keys=True)
# print (json_string)


# import json
# litery = {"pierwsza": "a", "druga": [7, 77, 777, 7777]}
# slownik = {"liczba": 2,
#            "owoc": "gruszka",
#            "warzywo": "pomidor",
#            "lista": litery,
#            "prawda": True,
#            "falsz": False,
#            "numery": [3, 4, 5, 100]}
# json_string = json.dumps(slownik, indent=4, sort_keys=True)
# with open ("slownik.json", "w") as f:
#     f.write (json_string)

# print(slownik["liczba"])



# litery = {"pierwsza": "a", "druga": [7, 77, 777, 7777]}
# slownik = {"liczba": 2,
#            "owoc": "gruszka",
#            "warzywo": "pomidor",
#            "lista": litery,
#            "prawda": True,
#            "falsz": False,
#            "numery": [3, 4, 5, 100]}
#
# # drugi_znak = litery["druga"]
# # print(drugi_znak[1])
#
# # print(litery["druga"][1])
# print(slownik["numery"][3])

# lista = ["a", "b", "c", "d"]
# print(lista[2])


# #petla
# lista = ["a", [1, 2, 3], "c", "d"]
# for litera in lista:
#     print(litera)

slownik = {"klucz": "wartosc",
           "pomidor": 3,
           "zgoda": True,
           "truskawka": 1000,
           "lista": [3, 5, 7]}

for cokolwiek, moge in slownik.items():
    print(cokolwiek)
    print(moge)

