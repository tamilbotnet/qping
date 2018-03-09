import requests
import sys
print""" 
             _             
            (_)            
  __ _ _ __  _ _ __   __ _ 
 / _` | '_ \| | '_ \ / _` |
| (_| | |_) | | | | | (_| |
 \__, | .__/|_|_| |_|\__, |
    | | |             __/ |
    |_|_|            |___/ 
                        
                      by TamilBotNet

 [SYSNTAX]  python qping.py target.txt
     """


with open(sys.argv[1]) as f:
	file = open("up_{}".format(sys.argv[1]), "w+")
	file.write("")
	file.close()

	for line in f:
		url = "http://{}".format(line.strip())
		try:
			res = requests.get(url, timeout=5)
			if res.ok:
				print("[+] Up! ({})".format(url))
				file = open("up_{}".format(sys.argv[1]), "a+")
				file.write("{}\n".format(url))
				file.close()
			else:
				print("[-] Down! ({})".format(url))
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			print("[-] Down! ({})".format(url))
