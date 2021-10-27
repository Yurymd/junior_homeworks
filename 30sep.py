userinfo = {"name": "Oleg", 
			"email": "superoleg@gmail.com",
			"premium": False,
			"lat" : 53.48484,
			"lon" : 104.9990
			}

#print(userinfo["name"])
username = userinfo["name"]
#print(userinfo[1])
#print(userinfo["lat"])
userinfo["lat"] = 54.4545
#print(userinfo["lat"])
#print(userinfo["age"])
userinfo["age"] = 99
print(userinfo)
del userinfo["age"]
print(userinfo)