aliens=[]

for i in range(30):
    alien={"color":"green","speed":"slow","id":i}
    aliens.append(alien)
n=0
for f in aliens[:10]:
    if f["id"] % 2:
        f["color"]="yelow"
        f["speed"]="medium"
    print(f"\n{aliens[n]}")
    n+=1
