from sesong import Sesong
from lagliste import lagliste
from statistikk import Statistikk

antall_simuleringer = 10000         # antallet sesonger vi skal simulere
statistikk = Statistikk(lagliste)

for i in range(antall_simuleringer):
    sesong = Sesong(lagliste)
    sesong.simuler()
    tabell = sesong.tabell().hent_rangering()
    rangering = statistikk.lagre_rangering(tabell)
statistikk.print_plasseringer()

# Print the number of times each team achieved each position