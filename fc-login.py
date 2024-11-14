from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import sys
import os
import time

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')


banner = r'''              _          _             _         _              _ 
             | |        | |           (_)       | |            | |
   __ _ _   _| |_ ___   | | ___   __ _ _ _ __   | |_ ___   ___ | |
  / _` | | | | __/ _ \  | |/ _ \ / _` | | '_ \  | __/ _ \ / _ \| |
 | (_| | |_| | || (_) | | | (_) | (_| | | | | | | || (_) | (_) | |
  \__,_|\__,_|\__\___/  |_|\___/ \__, |_|_| |_|  \__\___/ \___/|_|
                                  __/ |                           
                                 |___/    '''
print("[system] Running . . .")
time.sleep(2)

while True:
    clear()
    print(banner)
    print("made by hamid")
    print("email: hamid@gmail.com\n")
    print("* This project is unfinished,So only google login is activate *")
    print("If it's your first excute, press 1\n")
    print("[#] press 1 to Register an account to auto-login")
    print("[#] press 2 to auto-login")

    usrinput = input("> ")

    if usrinput == "1":
        id = input("ID : ")
        pw = input("PW : ")

        if os.path.exists("userlist.json"):
            with open("userlist.json", "r") as f:
                usr = json.load(f)
        else:
            usr = []  

        newuser = {"id": id, "pw": pw}
        usr.append(newuser)

        with open("userlist.json", "w") as f:
            json.dump(usr, f, indent=1)


    elif usrinput == "2":
        print("getting data . . .")
        time.sleep(1.5)

        if os.path.exists("userlist.json"):
            print("[#] Please enter the number of the account you want [#]")
            n = 0
            with open("userlist.json","r") as f:
                usrlist = json.load(f)
                for lists in usrlist:
                    n += 1
                    print("{} ID :  {}".format(n,lists["id"]))
                usrinput = int(input("> "))

                if 1 <= usrinput <= len(usrlist):
                    select = usrlist[usrinput-1]
                    usrid = select["id"]
                    usrpw = select["pw"]
                          
            option = Options()
            option.add_argument("--start-maximized")
            option.add_experimental_option("detach", True)

            driver = webdriver.Edge(options=option)

            driver.get('https://events.fconline.nexon.com/')

            search = driver.find_element(By.CSS_SELECTOR, ".btn_login")
            search.click()

            google = driver.find_element(By.CSS_SELECTOR, ".btGoogle")
            google.click()

            IDINPUT = driver.find_element(By.ID, "identifierId")
            IDINPUT.send_keys(usrid)
            IDINPUT.send_keys(Keys.ENTER)


            PWINPUT = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"Passwd")))
            PWINPUT.send_keys(usrpw)
            PWINPUT.send_keys(Keys.ENTER)

            exe = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"btn_gamestart")))
            exe.click()

        else:
            print("[!] Please register your account first")
            sys.exit()
    
    else:
        print("[!] please write num 1 or 2")
