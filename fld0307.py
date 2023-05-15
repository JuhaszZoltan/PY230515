from random import randint, seed

# meg kell adnunk tippeket [5db, különböző, 1-90]
# le kell generálni a nyerőszámokat
# ki kell írni a nyerőszámokat növekvő sorrendbe
# meg kell határozni a találatok számát

tippek:list[int] = []
ssz:int = 1
while len(tippek) < 5:
    tipp:int = int(input(f'kérem az {ssz}. tippet: '))
    if tipp not in tippek and 1 <= tipp <= 90:
        ssz += 1
        tippek.append(tipp)
    else: print('nem megfelelő tipp, próbáld újra!')

nyeroszamok:list[int] = []
while len(nyeroszamok) < 5:
    nyszam:int = randint(1, 90)
    if nyszam not in nyeroszamok:
        nyeroszamok.append(nyszam)

talalatok:int = 0
for tipp in tippek:
    if tipp in nyeroszamok:
        talalatok += 1

tippek.sort()
nyeroszamok.sort()
print(f'tippek: {tippek}')
print(f'nyerőszámok: {nyeroszamok}')

if talalatok > 0:
    print(f'gratulálok, nyertél!')
    print(f'találatok száma: {talalatok}')
else: print('nem találtál egy számot sem')