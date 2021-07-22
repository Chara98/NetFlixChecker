import requests; from tkinker import filedialog
def main():
  url = 'http://httpbin.org/ip'
  proxy = filedialog.askopenfile(mode='r', title='Load Ip:Port',filetype=((".txt","*.txt"),("All files","*.txt")))
  working = []
  for i in proxy:
    i=i.replace('\n','')
    try:
      res = requests.get(url,proxies={'http':i,'https':i})
      print(f'[+]Vaild Proxy {i}')
      working.append(i)
    except:
      print(f'[-]Invaild Proxy {i}')
  
  for i in working:
    pro = open('Working_Proxies.txt','w')
    pro.write(i)
    
main()
