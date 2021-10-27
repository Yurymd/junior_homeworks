currencies = [{"Cur_ID":440,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"AUD","Cur_Scale":1,"Cur_Name":"Австралийский доллар","Cur_OfficialRate":1.8082},
			  {"Cur_ID":510,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"AMD","Cur_Scale":1000,"Cur_Name":"Армянских драмов","Cur_OfficialRate":5.1701},
			  {"Cur_ID":441,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"BGN","Cur_Scale":1,"Cur_Name":"Болгарский лев","Cur_OfficialRate":1.4653},
			  {"Cur_ID":449,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"UAH","Cur_Scale":100,"Cur_Name":"Гривен","Cur_OfficialRate":9.4030},
			  {"Cur_ID":450,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"DKK","Cur_Scale":10,"Cur_Name":"Датских крон","Cur_OfficialRate":3.8508},
			  {"Cur_ID":431,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"USD","Cur_Scale":1,"Cur_Name":"Доллар США","Cur_OfficialRate":2.4775},
			  {"Cur_ID":451,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"EUR","Cur_Scale":1,"Cur_Name":"Евро","Cur_OfficialRate":2.8603},
			  {"Cur_ID":452,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"PLN","Cur_Scale":10,"Cur_Name":"Злотых","Cur_OfficialRate":6.2239},
			  {"Cur_ID":508,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"JPY","Cur_Scale":100,"Cur_Name":"Иен","Cur_OfficialRate":2.2147},
			  {"Cur_ID":461,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"IRR","Cur_Scale":100000,"Cur_Name":"Иранских риалов","Cur_OfficialRate":5.8988},
			  {"Cur_ID":453,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"ISK","Cur_Scale":100,"Cur_Name":"Исландских крон","Cur_OfficialRate":1.9235},
			  {"Cur_ID":371,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"CAD","Cur_Scale":1,"Cur_Name":"Канадский доллар","Cur_OfficialRate":1.9754},
			  {"Cur_ID":462,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"CNY","Cur_Scale":10,"Cur_Name":"Китайских юаней","Cur_OfficialRate":3.8428},
			  {"Cur_ID":394,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"KWD","Cur_Scale":1,"Cur_Name":"Кувейтский динар","Cur_OfficialRate":8.2134},
			  {"Cur_ID":454,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"MDL","Cur_Scale":10,"Cur_Name":"Молдавских леев","Cur_OfficialRate":1.4234},
			  {"Cur_ID":448,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"NZD","Cur_Scale":1,"Cur_Name":"Новозеландский доллар","Cur_OfficialRate":1.7155},
			  {"Cur_ID":455,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"NOK","Cur_Scale":10,"Cur_Name":"Норвежских крон","Cur_OfficialRate":2.8957},
			  {"Cur_ID":456,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"RUB","Cur_Scale":100,"Cur_Name":"Российских рублей","Cur_OfficialRate":3.4412},
			  {"Cur_ID":457,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"XDR","Cur_Scale":1,"Cur_Name":"СДР (Специальные права заимствования)","Cur_OfficialRate":3.4956},
			  {"Cur_ID":421,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"SGD","Cur_Scale":1,"Cur_Name":"Сингапурcкий доллар","Cur_OfficialRate":1.8261},
			  {"Cur_ID":458,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"KGS","Cur_Scale":100,"Cur_Name":"Сомов","Cur_OfficialRate":2.9209},
			  {"Cur_ID":459,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"KZT","Cur_Scale":1000,"Cur_Name":"Тенге","Cur_OfficialRate":5.8219},
			  {"Cur_ID":460,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"TRY","Cur_Scale":10,"Cur_Name":"Турецких лир","Cur_OfficialRate":2.7782},
			  {"Cur_ID":429,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"GBP","Cur_Scale":1,"Cur_Name":"Фунт стерлингов","Cur_OfficialRate":3.3753},
			  {"Cur_ID":463,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"CZK","Cur_Scale":100,"Cur_Name":"Чешских крон","Cur_OfficialRate":11.2711},
			  {"Cur_ID":464,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"SEK","Cur_Scale":10,"Cur_Name":"Шведских крон","Cur_OfficialRate":2.8265},
			  {"Cur_ID":426,"Date":"2021-10-11T00:00:00","Cur_Abbreviation":"CHF","Cur_Scale":1,"Cur_Name":"Швейцарский франк","Cur_OfficialRate":2.6671}]

"Курс ВАЛЮТА_АББР на сегодня: КУРС рубля за X ВАЛЮТА_АББР."
curr = "USD"
for kurs in currencies:
	if kurs.get("Cur_Abbreviation") == curr:
		print(f'Курс {curr} на сегодня: {kurs.get("Cur_OfficialRate")} рубля за {kurs.get("Cur_Scale")} {curr}.')