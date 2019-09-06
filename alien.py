aliens=[]

for color in range(20):
    alien={'color':'green','speed':'slow','Number':color}
    aliens.append(alien)
for i in aliens[:5]:
    print(f"{i}\n")
