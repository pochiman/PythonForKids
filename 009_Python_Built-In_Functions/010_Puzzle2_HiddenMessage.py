# s = 'this if is you not are a reading very this good then way you \
# to have hide done a it message wrong'
# print(dir(s))

# help(s.split)

message = 'this if is you not are a reading very this good then \
way you to have hide done a it message wrong'
words = message.split()
for x in range(0, len(words), 2):
    print(words[x])