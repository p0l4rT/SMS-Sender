import requests, sys, os, time, configparser, urllib.request, threading, string, base64, urllib.parse, random, urllib.parse, datetime


try:
    import requests
except ImportError:
    print('Oops!! : Plase, Install requirements.')
    print('Error Occured!!!\nUse Non-Supported Version')
    input('Press Any Key To Use Non-supported Version')

# START READ KEY FILE
read_config = configparser.ConfigParser()
read_config.read("credentials.ini")

apikey = read_config.get("API KEY", "API")
pageq = read_config.get("QUOTA", "PAGE")

numquota = pageq+apikey
# END READ KEY FILE

# PEDILLOS
def pedillos():
		print(errordog + "\n\n\033[91mWhoops! Unos pedillos.\n\n\033[mMaybe:\n\n1. Your API KEY was not set in credentials.ini\n2. You need buy more credits.\n\nPlease, check the next text to know the error:\n\033[0m")
		print("\033[93m"+resp.text+"\n\n\033[0m")
		print("\033[95m\nFix the issue and restart the script again. :)\n\n\033[0m")
		exit()

# EXIT FUNCTION
def ciao():
	print("\nFollow me on Instagram!\nhttps://www.instagram.com/polartech_wh")
	time.sleep(3)

	print("\nBye Bye!")
	time.sleep(1)

	clr()

	exit()

# OPEN WEBPAGE FUNCTION

def startscript():
	if os.name == 'nt':
		clr()
		os.system("python sendsms.py")
	else:
		clr()
		os.system("python3 sendsms.py")

def createapi():
	if os.name == 'nt':
		os.system("start _sys-api-cmd.bat")
		clr()
		startscript()
	else:
		os.system("bash _sys-api-unix.sh")
		clr()
		startscript()


def buycredits():
	if os.name == 'nt':
		os.system("start _win.bat")
		clr()
		startscript()
	else:
		os.system("bash _unix.sh")
		clr()
		startscript()

# FUNCTIONS
def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()

def nevergonna():
	if os.name == 'nt':
		os.system("start _ngw.bat")
		print ("\n\033[91m Bromita 🤑 \033[0m\n")
	else:
		os.system("bash _ngu.sh")
		print ("\n\033[91m Bromita 🤑 \033[0m\n")

def saveLog():

	log_ = "Number: " + number + "\nText: " + message + "\nResponse from TextBelt API: " + resp.text

	try:
		if not os.path.exists ("logs"):
			os.makedirs ("logs")
			log_file = open("logs/log_{}.txt".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), "a")
			log_file.write("{} - Error: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), log_))
			log_file.close()
		elif os.path.exists ("logs"):
			log_file = open("logs/log_{}.txt".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), "a")
			log_file.write("{} - Error: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), log_))
			log_file.close()
	except IOError as e:
    		print("Error: couldn't write the .log file.: {}".format(e))


#BANNERS
osito = """
\033[93m
 - - - - - - - - - - - - - - - - - - °(-u-)° - - - - - - - - - - - - - - - - - -
\033[0m"""

errordog = """
\033[91m
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&%%%%%&&%%%%&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&&%%%%%%%%%%%%#%%%%##%%%#%%%%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%#%################((%@@@@@@@@
@@@@@@@@@@@@#(((########%%%#######################(/((#@@@@@
@@@@@@@@#(#((///(#######%%%%%######################//((((#@@
@@@@@@&((((#**///#%%%%%%%%%%################(######(/(((((((
@@@@@#((#(((////(##%%%%%%%%%%%%%%################%#(#######@
@@@%(#####(((((##%%%%&&&%%%%%%#####%#############%%&@@@@@@@@
@@%#######((#####%%%%%%%%%%####(((############(##%%&@@@@@@@@
@@@@#######((##(###%%##/,,**//****(#######%%%##/...%@@@@@@@@
@@@@@@####(((######%%%%#(/*  .,*((####%%%%#%%%%#//@@@@@@@@@@
@@@@@@@@@#(##########%%%################((((###%%@@@@@@@@@@@
@@@@@@@@@@@&((((((####%%%##########((((*,... .,/#@@@@@@@@@@@
@@@@@@@@@@@@@//////((############(/**,**,      ,(@@@@@@@@@@@
@@@@@@@@@@@@**//(/((((((#####(#((/****,,,.    .*(@@@@@@@@@@@
@@@@@@@@@@@/**//(((((((((((((/*,*////**,,,,,,*/@@@@@@@@@@@@@
@@@@@@@@@&/***///((((#(((((((((///////////(((//@@@@@@@@@@@@@
@@@@@@@@//*****///((((((####((##((#######((#(//&@@@@@@@@@@@@
@@@@@@////******/(((((((#####################((((@@@@@@@@@@@
@@@@%///////////////((((########%#%%%%%%%%%%%#((((@@@@@@@@@@
\033[0m"""

mainlogo = """

\033[92m
MMX:       .'c0WMMMMNOc.    .'oXMMMWo.   .lWMMMMMMMMMO'    .xMMMMM0,       ..;kN
MMO.          .xWMNx;.         ,kWMX;     dMMMMMMMMM0,      cNMMMMx.          .l
MWo    'll.    ;X0;    .;:;.    .kMO.    .OMMMMMMMMO'       '0MMMNc    'lc'    .
MX;    cKO,    l0,    cKWMM0'    oWo     :NMMMMMMWk.   ''    dMMM0'   .oK0c    ;
Mk.     .    .cKo    ;XMMMMK,    dX;   ..dMMMMMMWk.   ,0d    ;XMMd.    ..    .cK
Wl     ...';lOWWc    'OWMW0:    ;Xk.   'o0MMMMMWx.    ,c,    .OMN:         .oKWM
K,   .oKKXNWMMMMk.    .,;,.    cKWl    .coddxKWd.             lWO.   .l'    oNMM
k.   '0MMMMMMMMMWO,         .:kNMK,         .dd.   'odddd;    ,Kd    ;Xx.   .xWM
d.   cNMMMMMMMMMMMXd,.   .,l0WMMMO'       . ;o' . .kMMMMMk. . 'kl   .oWX:    :XM
\033[96m
\n
			<< SEND SMS Anonymously >>\n
			     IG: polartech_wh
				     \n
\033[92m--------------------------------------------------------------------------------\033[0m
	"""

# START
print(mainlogo)
time.sleep(1)
print(" Instructions:\n\n   1. Buy an API on https://textbelt.com/purchase\n   2. Write your API Key in credentials.ini\n   3. Restart the script.\n   4. Set number with + symbol. Example: +19794641245\n   5. Write and send your message.\n")


print("\033[92m--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------\033[0m\n")


## MENU
print ("  What do you want to do?\n\n")

for i in range(1):

    print('    \033[92m0. Generate an API (Only new users)\n\033[0m')

    print('    \033[92m1. Buy credits\n\033[0m')

    print('    \033[92m2. Send message\n\033[0m')

    print('    \033[92m3. Check your SMS quota.\n\033[0m')

    print('    \033[92m4. Restart script\n\033[0m')

    print('    \033[92m5. Send SMS for free\n\033[0m')

    print('    \033[92m99. Exit\n\033[0m')

option = int(input("\n\n\033[0m Option » "))

if option == 0:
	createapi()

if option == 1:
	buycredits()


if option == 2:
	print(osito)

	number = input("	Set phone number:\n	» ")
	if len(number) > 5:
		print("\033[92m \n	>>>	"+number+"\033[0m")

	while len(number) <= 6:
		print('\n\033[91m>>>>>> Please, check your number. <<<<<<\033[0m\n')
		number = input("	Set phone number:\n	» ")


	print("\n")

	message = input("	Set message:\n	» ")


## SCRIPT WORKING + API
	resp = requests.post('https://textbelt.com/text', {
				'phone' : number,
				'message' : message,
				'key' : apikey,
				})
	print(resp.text)
	if '"success":true' in resp.text:
		saveLog()
		print("\033[92m Ready!, message was sent. \033[0m\n")
		time.sleep(2)
		clr()
		startscript()

	if '"success":false' in resp.text:
		saveLog()
		pedillos()
		startscript()

	if '"error":false' in resp.text:
		saveLog()
		print("\033[92m The message was not sent \033[0m\n")
		time.sleep(2)
		clr()
		startscript()

if option == 3:
	print("\nTo check your quota visit:\n" + numquota+"\n\n")
	time.sleep(20)

if option == 3:
	input("\nPress any key to ontinue...")
	clr()
	startscript()


if option == 4:
	clr()
	startscript()

if option == 5:
	nevergonna()

if option == 99:
	ciao()

if option > 5:
	print ("\n\n  That option doesn't exist.\n\n")
	time.sleep(2)
	clr()
	startscript()