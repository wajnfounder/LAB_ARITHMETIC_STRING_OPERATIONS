sentence:str = "I hope this camp brings me a lot of opportunities to grow, learn new skills, and achieve my goals"
word:str = "opportunities"
print(len(sentence))
index = sentence.index(word)
print(index)
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
print(sentence.replace("opportunities", "good things"))
print(sentence[-1])