aruuke = [['algebra', 100], ['biologia', 84], ['fizika',61],['fizra',92],['trud',99],['anatomiya',100],['musica',100]]
malika = [['algebra', 100], ['biologia', 100], ['fizika',56],['fizra',100],['trud',100],['anatomiya',88],['musica',97]]
aida = [['algebra', 100], ['biologia', 84], ['fizika',78],['fizra',77],['trud',87],['anatomiya',96],['musica',100]]

aruuke_dict = dict((x[0],x[1])for x in aruuke)
print(aruuke_dict)
malika_dict = dict((x[0], x[1]) for x in malika)
print(malika_dict)
aida_dict = dict((x[0], x[1]) for x in aida)
print(aida_dict)
srednee_aruuke = sum(aruuke_dict.values()) / len(aruuke_dict)
print(srednee_aruuke)
srednee_malika = sum(malika_dict.values()) / len(malika_dict)
print(srednee_malika)
srednee_aida = sum(aida_dict.values()) / len(aida_dict)
print(srednee_aida)



