import os
import string
  
os.system('clear'%locals())
def omemishra():	  
	print "                                                 "
	print "        o-o     o                 o      o---o   "
	print "       /        |                 |         /    "
	print "------O         O--o      oo     -o-      -O--------------------"
	print "       \        |  |     | |      |       /      "
	print "        o-o     o  o     o-o-     o      o---o   "
	print "                                                 "
	print "    ================Encrypt The Chat ========De.Hacker"

	print " "


	print ' Please Selet One What AND Where Your Computer Is'
	print '--------------------------------------------------------'
	print ' -> 1 : Your PC is Master (LAN)'
	print ' -> 2 : Your PC is Slave (LAN)'
	print ' -> 3 : Wants To chat Over Intra-Net(WAN)'
	print ' -> 4 : Exit '
	print '      '
	option = raw_input("Enter Your Choice:- ")
	ome = True

	while(ome == True):
	    if (option == "1"):
		print 'You Are MASTER'
		ip = raw_input('-> Enter IP:- ')
		a = ip.split('.')
		b = b = "".join([hex(int(value))[2:].zfill(2) for value in a])
		b = b.replace('0x', '')
		b = b.upper()
		print '  Please Share This Code With The Slave Members'
		print '-------------------------------------------------'
		print '  ->  0x'+b
		print '-------------------------------------------------'
		print '                               '
		os.system('nc -lvp 8888')
	   
	     
	    elif (option == "2"):
		print 'You Are SLAVE'
		print '         '
		print 'Please Enter The Code Provided By MASTER'
		code = raw_input("Enter Here :- ")
		os.system('nc %(code)s 8888' %locals()) 
	     
	    elif (option == "3"):
		os.system('clear'%locals())
		print "                                                 "
		print "        o-o     o                 o      o---o   "
		print "       /        |                 |         /    "
		print "------O         O--o      oo     -o-      -O--------------------"
		print "       \        |  |     | |      |       /      "
		print "        o-o     o  o     o-o-     o      o---o   "
		print "                                                 "
		print "    ================Encrypt The Chat ========De.Hacker"

		print " "

		print ' You Are A Master or Slave'
		print ' -> 1: Master '
		print ' -> 2: Slave '
		print ' -> 3: Back To Main Menu '
		print ' '
		option = raw_input("Enter Your Choice:- ")
		
		if (option == "1"):
			print 'You Are MASTER'
			ip = raw_input('-> Enter IP:- ')
			a = ip.split('.')
			b = b = "".join([hex(int(value))[2:].zfill(2) for value in a])
			b = b.replace('0x', '')
			b = b.upper()
			print '  Please Share This Code With The Slave Members'
			print '-------------------------------------------------'
			print '  ->  0x'+b
			print '-------------------------------------------------'
			print '                               '
		
		elif (option == "2"):
			print 'You Are SLAVE'
			print '         '
			print 'Please Enter The Code Provided By MASTER'
			code = raw_input("Enter Here :- ")
		
		elif (option == "3"):
			os.system('clear'%locals())
			return omemishra()	

	    elif (option =="4"):
		    e=raw_input("Do you really want to exit? (Y/N): ")
		    if (e == "Y" or e == "y"):
		        exit()
		    if ( e == "N" or e == "n"):
			os.system('clear'%locals())
		       	return omemishra()
						
		        
	    else:
		print "Please Try Again"
		os.system('clear'%locals())
		return omemishra()
omemishra()
