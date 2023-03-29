# dagjespeelhal

x = ticket = 745
y = VIPveenmin = round(37 / 5)

totaaltickets = int(input('Totaal Aantal Tickets: '))
bedragtickets = totaaltickets * x
print('Totaal bedrag tickets: ', bedragtickets, 'cent')

totaaltijdVIP = int(input('Totale Min in VIP-VR-GameSeat: '))
bedragtijdVIP = totaaltijdVIP * y
print('Totaal VIP-VR-GameSeat', bedragtijdVIP, 'cent') 

totalekosten = bedragtickets + bedragtijdVIP
print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar', totalekosten , 'cent!' )
