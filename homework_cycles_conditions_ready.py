"""
Дан список видеоигр, как и всегда, дополняйте своими, при желании.
Сделайте скрипт, который проходиться по этому списку и рассортировывает их по году выпуска, 
от более раннх к более поздним.

Сделайте еще один скрипт, который рассортировывает игры по колличеству продложений (поле sequels)
"""

games = [
		{"name": "Fallout", 
		"sequels":["Fallout 2", "Fallout: Tactics", "Fallout. Brotherhood of the steel"], 
		"studio": "Black Isle", 
		"year": 1997},
		{"name": "Dragon Age: Origin", 
		"sequels":["Dragon Age 2", "Dragon Age 3"], 
		"studio": "Bioware", 
		"year":2009},
		{"name": "Cyberpunk 2077", 
		"sequels":[], 
		"studio": "CD Project", 
		"year": 2020},
		{"name": "Death Stranding", 
		"sequels":[], 
		"studio":"Kodjima Production", 
		"year":2018},
		{"name": "Deus Ex", 
		"sequels":["Deus Ex: Invisible War", "Deus Ex: Human Revolution", "Deus Ex: Mankind Divided"], 
		"studio":"ION Storm", 
		"year":2000},
		{"name": "Red Alert 2", 
		"sequels":["Red Alert 2: Yuri's revenge"], 
		"studio":"Westwood studio", 
		"year":2001}
		]

######################################################################

"""
Используйте  профиль поользователя и список песен, чтобы было интереснее добавьте свои.
Напишите скрипт, который пройдеться по списку песен (songs), и переделает поле songs_for_me из списка в словарь
устроенный так: Ключом будет группа пользователя, которая есть у него в списке my_artists
а значениями - списки из песен, принадлежащих этим исполнителям.

Т.е вместо

me = {"name": "Egor",
	  "my_artists": ["Bon Jovi", "Ben Nichols"],
	  "songs_for_me":[]
	  }

Скрипт должен преобразовывать этот дикт в вот такой:

{"name": "Egor",
	  "my_artists": ["Bon Jovi", "Ben Nichols"],
	  "songs_for_me":{"Bon Jovi": [	{"artist":"Bon Jovi",
	  								 "name": "The Distance", 
	  								 "long": 3.24, 
	  								 "band":True, 
	  								 "album": "Bounce"},
									{"artist":"Bon Jovi", 
									 "name": "Open All Night", 
									 "long": 3.24, 
									 "band":True, 
									 "album": "Bounce"},
									 ]}
	  }

{'name': 'Egor',
 'my_artists': ['Bon Jovi', 'Ben Nichols'],
  'songs_for_me': {'Ben Nichols': {'artist': 'Ben Nichols', 'name': 'The last pale light in the west', 'long': 3.24, 'band': False, 'album': None}, 'Bon Jovi': {'artist': 'Bon Jovi', 'name': 'Open All Night', 'long': 3.24, 'band': True, 'album': 'Bounce'}}}

Это сделает сервис более гибким и даст возможности для более вариативной группировки данных для нашего юзера.
"""

# Профиль пользователя
me = {"name": "Egor",
	  "my_artists": ["Bon Jovi", "Ben Nichols"],
	  "songs_for_me":[]
	  }

# список песен
songs = [
		{"name": "Сгораю", "band":"Noise MC"},
		{"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"},
		{"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"},
		{"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False, "album": None},
		{"name": "Сгораю", "band":"Noise MC"},
		{"name": "", "band":"", "long": 8.42},
		{"artist":"Bon Jovi", "name": "The Distance", "long": 3.24, "band":True, "album": "Bounce"},
		{"artist":"Bon Jovi", "name": "Open All Night", "long": 3.24, "band":True, "album": "Bounce"},
		{"artist":"Bon Jovi", "name": "The Distance", "long": 3.24, "band":True, "album": "Bounce"},
		# {"artist":"Bon Jovi", "name": "111", "long": 3.24, "band":True, "album": "Bounce"},
		# {"artist":"Bon Jovi", "name": "222", "long": 3.24, "band":True, "album": "Bounce"},
		# {"artist":"Bon Jovi", "name": "333", "long": 3.24, "band":True, "album": "Bounce"},
		]


# Вот тут над ними колдовать:

# print(game)
# print("Игры по годам:")
# games_by_year = sorted(games, key=lambda k: k["year"])
# print(games_by_year)
# print("\n")

# print("Игры по годам в обратном порядке:")
# games_by_year_reverse = sorted(games, key=lambda k: k["year"], reverse=True)
# print(games_by_year_reverse)
# print("\n")

# print("Игры по количеству сиквелов:")
# games_by_sequels = sorted(games, key=lambda k: len(k["sequels"]))
# print(games_by_sequels)
# print("\n")

# print("Новый профиль для музыки:")

# me["songs_for_me"] = {}
# print(me["songs_for_me"])
# for song in songs:
# 	if song.get("artist") in me["my_artists"]:
# 		me["songs_for_me"][song.get("artist")] = 
# print(me["songs_for_me"])

song_list = [song for song in songs if song.get("artist") in me["my_artists"]]
print(song_list)


вв
а
а
а