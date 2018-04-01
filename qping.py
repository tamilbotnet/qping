#!/usr/bin/env python
#
# Updated by Crazy Danish Hacker

import requests
import sys

timeout = 3
verbose = True
version = "1.0.1"
banner = """
             _             
            (_)            
  __ _ _ __  _ _ __   __ _ 
 / _` | '_ \| | '_ \ / _` |
| (_| | |_) | | | | | (_| |
 \__, | .__/|_|_| |_|\__, |
    | | |             __/ |
    |_|_|            |___/ 

                      by TamilBotNet
                      version: {}
      Updated by Crazy Danish Hacker
""".format(version, sys.argv[0])

usage = "\n [SYNTAX]  python {} target.txt"

# Check if any args have been set.
if len(sys.argv) <= 1:
    print(banner)
    print(usage)
    exit(1)

# Set the output filename to be used globally
filename = "OnlineDomains_{}".format(sys.argv[1])


def create_file(user_file):
    with open(user_file, "w") as output_file:
        output_file.close()


def main():
    print(banner)
    global filename  # This could be an arg to main() if we wanted to.
    with open(sys.argv[1], "r") as input_file:
        create_file(filename)

        for line in input_file:
            url = "http://{}".format(line.strip())  # Note: Strip only works at the beginning or end of a string.
            try:
                req = requests.get(url, timeout=timeout)
                if req.status_code == 200:
                    extra = "- HTTP 200 OK" if verbose else ""
                    print("[+] Domain is online! ({}) {}".format(url, extra))
                    with open(filename, "a") as output_file:
                        output_file.write("{}\n".format(url))
                        output_file.close()  # Not sure if we need to call close() here as "with open" may handle that.
                else:
                    extra = "HTTP {}".format(req.status_code) if verbose else ""
                    print("[-] Domain did not return 200 OK! ({}) {}".format(url, extra))
            except KeyboardInterrupt:
                exit()
            except requests.exceptions.Timeout:
                print("[-] Domain timed out! ({})".format(url))
            except requests.exceptions.ConnectionError:
                print("[-] Domain may not exist! ({})".format(url))


if __name__ == "__main__":
    main()
