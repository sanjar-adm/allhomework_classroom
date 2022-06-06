school = {
    '1а': 24,
    '1б' : 25,
    '2б' : 24,
    '6а' : 33,
    '7в' : 32,
    '8у' : 31
}
print(school)
school['1а'] = 20
print(school)
school['1г'] = 22
print(school)
del school['8у']
print(school)
print(sum(school.values()))
