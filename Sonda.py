#!/usr/bin/env python3

import socket, sys, os
import Comandos


class Menu:
	Fold, Batt, Prop, Dump,Exit = range( 1, 6 )
	Options = ( "Desplegar o Plegar las Placas", "Nivel de Carga", "Accionar Propulsor", "Mediciones","Salir" )

	def menu():
		print( "+{}+".format( '-' * 30 ) )
		for i,option in enumerate( Menu.Options, 1 ):
			print( "| {}.- {:<25}|".format( i, option ) )
		print( "+{}+".format( '-' * 30 ) )

		while True:
			try:
				selected = int( input( "Selecciona una opción: " ) )
			except:
				print( "Opción no válida." )
				continue
			if 0 < selected <= len( Menu.Options ):
				return selected
			else:
				print( "Opción no válida." )

#def iserror( message ):
#	if( message.startswith( "ER" ) ):
#		code = int( message[2:] )
#		print( ER_MSG[code] )
#		return True
#	else:
#		return False
#
#def int2bytes( n ):
#	if n < 1 << 10:
#		return str(n) + " B  "
#	elif n < 1 << 20:
#		return str(round( n / (1 << 10) ) ) + " KiB"
#	elif n < 1 << 30:
#		return str(round( n / (1 << 20) ) ) + " MiB"
#	else:
#		return str(round( n / (1 << 30) ) ) + " GiB"
#





if __name__ == "__main__":
	if len( sys.argv ) > 3:
		print( "Uso: {} [<servidor> [<puerto>]]".format( sys.argv[0] ) )
		exit( 2 )

	if len( sys.argv ) >= 2:
		SERVER = sys.argv[1]
	if len( sys.argv ) == 3:
		PORT = int( sys.argv[2])

	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.connect( (SERVER, PORT) )


		password = input( "Introduce el codigo de seguridad: " )

	while True:
		option = Menu.menu()


		if option == Menu.Fold:
			

		elif option == Menu.Batt:
			

		elif option == Menu.Prop:
			

		elif option == Menu.Dump:
			
		elif option == Menu.Exit:
			message = "{}\r\n".format( szasar.Command.Exit )
			s.sendall( message.encode( "ascii" ) )
			message = szasar.recvline( s ).decode( "ascii" )
			break
	s.close()















