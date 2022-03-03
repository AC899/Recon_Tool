import pyfiglet
import sys
import socket
import time
import os
import requests
from ping3 import ping, verbose_ping
from console_progressbar import ProgressBar
import time
import json
from colorama import init, Fore


ascii_banner = pyfiglet.figlet_format("RECON TOOL", font = "slant")
print(ascii_banner + "Automating Enumeration since 2022")
time.sleep(0.5)

class Main:

    def __init__(self):
        pass


    def NSIP(self):
        while True:
            try:
                global nsip
                global resolvedip
                nsip = input("\nEnter your target website [example: google.com]: ")
                # if nsip == "s" or nsip == "skip":
                #     break
                resolvedip = socket.gethostbyname(nsip)
                pingresult =ping(resolvedip)
            except socket.error:
                print("Host appears to be down. Couldn't lookup: " + nsip)
                continue
            print("IP address: " + resolvedip +"\nHost is LIVE and responded to our PING within %.5s" % str(pingresult) + " per seconds")
            Object.dirbuster()

    def dirbuster(self):
        while True:
            try:
                global filename
                filename = input("\nWe are now moving onto Directory Busting ..... enter the path of the wordlist "
                                 "you want to use for directory busting \n(press b to go back a step) : ")
                if not os.path.exists(filename):
                    print("This directory does not exist - please enter the full file path i.e. C:/Desktop/wordlist.doc")
                if filename == 'b' or filename == 'back':
                    Object.NSIP()
                    break
            except:
                continue
            if not os.path.exists(filename) == False:
                print("This is a valid file")
                Object.word_checker()
                break
        #nsip = 'google.com'
        #/Users/anilcarrier/Desktop/common.txt
    def word_checker(self):
        with open(filename, 'r') as file:
            full_url = []
            for line in file:
                linefinal = line.rstrip()
                full_url.append("https://" + nsip + '/' + linefinal)
            validating_words = input("\nIs this the right format you had in mind for directory busting ? SAMPLE FROM WORDLIST: " + full_url[3]
                                     + "\nif the wordlist or URL shown above is wrong: press 'b' or 'back' to go back a step; otherwise press any key to continue")
            if validating_words == 'b' or validating_words == 'back':
                Object.dirbuster()
            else:
                print("\nLet's get busting these directories ....... output will be blank if there were no status code(s) 200, 301 or 403.")
            for i in full_url:
                r = requests.get(i)
                if r.status_code == 200:
                    print("FOUND: Status Code 200: " + str(i))
                    if r.status_code == 403:
                        print("FORBIDDEN: Status Code 403:" + str(i))
                        if r.status_code == 301:
                            print("REDIRECTION: Status Code 301: " + str(i))
            Object.port_scan()

    def port_scan(self):
        ports_and_services_file = open('/Users/anilcarrier/PycharmProjects/Recon_tool/test1.json', )
        data = json.load(ports_and_services_file)
        confirmingresolvedip = input("\nPort Scanning our target :" + nsip
                                          + "\nIf the web adresss is wrong: press 'b' or 'back' to go back a step "
                                            "otherwise press press any key to continue")
        if confirmingresolvedip == 'b' or confirmingresolvedip == 'back':
            Object.NSIP()
        else:
            try:
                for common_port_num, port_service in data.items():
                    ports_iterable = list(map(int, common_port_num.split(' ')))  # made ports intergers and iterable
                    for intergers in ports_iterable:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1)
                        result = s.connect_ex((resolvedip, intergers))
                        if result == 0:
                            print("Port {}:({}) is open".format(intergers, port_service))
                        s.close()
                        print("RECON COMPLETE")

            except socket.gaierror:
                print("Hostname Could Not Be Resolved !!!!")
                sys.exit()
            except socket.error:
                print("Server not responding !!!!")
                sys.exit()


Object = Main()
Object.NSIP()


#TO DO LIST:
#open JSON from an online location to run as the wordlist
#add progress bars to functions
















    #nslookup function
# def NSIP(nsip):
#     while True:
#         try:
#             nsip = input("\nEnter your target website [example: Google.com] (s to skip onto the next step) : ")
#             if nsip == "s" or nsip == "skip":
#                 break
#             resolvedip = socket.gethostbyname(nsip)
#             pingresult =ping(resolvedip)
#         except socket.error:
#             print("Host appears to be down. Couldn't lookup: " + nsip)
#             continue
#         print("IP address: " + resolvedip +"\nHost is LIVE and responded to our PING within %.5s" % str(pingresult) + " per seconds")
#
# print(NSIP(""))
# #
# def dirbuster(filename):
#     while True:
#         try:
#             filename = input("Enter the path of the wordlist you want to use for directory busting (s to skip onto the next step) : ")
#             if not os.path.exists(filename):
#                 print("This directory does not exist - please enter the full file path i.e. C:/Desktop/wordlist.doc")
#             if filename == "s" or filename == "skip":
#                 break
#         except:
#             continue
#         if not os.path.exists(filename) == False:
#             return("This is a valid file")
#             break
#
# print(dirbuster(''))

# filename = '/Users/anilcarrier/Desktop/common.txt'
# def word_checker(filename):
#     nsip = 'google.com'
#     with open(filename, 'r') as file:
#         full_url = []
#         for line in file:
#             linefinal = line.rstrip()
#             full_url.append("https://" + nsip + '/' + linefinal)
#         validating_words = input("Is this the right format you had in mind ? SAMPLE FROM WORDLIST: " + full_url[3]
#                                  + "\nif the wordlist you entered is wrong: press 'b' or 'back' to go back a step"
#                                    "\notherwise press 's' or 'skip' to start discovering directories""")
#         if validating_words == 'b' or validating_words == 'back':
#             print(dirbuster(''))
#         if validating_words == 's' or validating_words == 'skip':
#             print("Let's get busting these directories .......")
#         for i in full_url:
#             r = requests.get(i)
#             if r.status_code == 200:
#                 print("FOUND: Status Code 200: " + str(i))
#                 if r.status_code == 403:
#                     print("FORBIDDEN: Status Code 403:" + str(i))
#                     if r.status_code == 301:
#                         print("REDIRECTION: Status Code 301: " + str(i))
#
# print(word_checker(filename))

# nsip = 'google.com'
# resolvedip = socket.gethostbyname(nsip)
#
# def port_scan(resolvedip):
#     ports_and_services_file = open('/Users/anilcarrier/PycharmProjects/Recon_tool/test1.json', )
#     data = json.load(ports_and_services_file)
#     confirmingresolvedip = input("We are now scanning for commomn ports / srevices running on the target :" + nsip
#                                       + "\nif the web adresss is wrong: press 'b' or 'back' to go back a step"
#                                         "\nOtherwise press press any key to start port scanning""")
#     if confirmingresolvedip == 'b' or confirmingresolvedip == 'back':
#         print(NSIP(''))
# #     else:
# #         try:
# #             for common_port_num, port_service in data.items():
# #                 ports_iterable = list(map(int, common_port_num.split(' ')))  # made ports intergers and iterable
# #                 for intergers in ports_iterable:
# #                     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #                     socket.setdefaulttimeout(1)
# #                     result = s.connect_ex((resolvedip, intergers))
# #                     if result == 0:
# #                         print(Fore.GREEN + "Port {}:({}) is open".format(intergers, port_service))
# #                     s.close()
# #
# #         except socket.gaierror:
# #             print("\n Hostname Could Not Be Resolved !!!!")
# #             sys.exit()
# #         except socket.error:
# #             print("\ Server not responding !!!!")
# #             sys.exit()
#
# print(port_scan(resolvedip))






# Original code (no function)

# nsip = 'google.com'
# filename = '/Users/anilcarrier/Desktop/common.txt'
# with open(filename, 'r') as file:
#     full_url = []
#     for line in file:
#         linefinal = line.rstrip()
#         full_url.append("https://" + nsip + '/' + linefinal)

# for i in full_url:
#     r = requests.get(i)
#     if r.status_code == 200:
#         print("FOUND: Status Code 200: " + str(i))
#         if r.status_code == 403:
#             print("FORBIDDEN: Status Code 403:" + str(i))
#             if r.status_code == 301:
#                 print("REDIRECTION: Status Code 301: " + str(i))

#
# nsip = 'google.com'
# resolvedip = socket.gethostbyname(nsip)
# ports_and_services_file = open('/Users/anilcarrier/PycharmProjects/Recon_tool/test1.json',)
# data = json.load(ports_and_services_file)
# try:
#     for common_port_num, port_service in data.items():
#         ports_iterable = list(map(int,common_port_num.split(' '))) #made ports intergers and iterable
#         for intergers in ports_iterable:
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             socket.setdefaulttimeout(1)
#             result = s.connect_ex((resolvedip, intergers))
#             if result == 0:
#                 print("Port {}:({}) is open".format(intergers,port_service))
#             s.close()
#
# except socket.gaierror:
#         print("\n Hostname Could Not Be Resolved !!!!")
#         sys.exit()
# except socket.error:
#         print("\ Server not responding !!!!")
#         sys.exit()