nevek:list[str] = []
beirt_nev:str = '---'

while len(nevek) < 10 and beirt_nev != '':
    beirt_nev = input('írj be egy nevet: ')
    if beirt_nev != '': nevek.append(beirt_nev)