import requests, random, re, time, os
from fake_useragent import UserAgent
from colorama import Fore, init
ua = UserAgent(browsers=['chrome'])
init()
red = Fore.RED; reset = Fore.RESET; green = Fore.GREEN; yellow = Fore.YELLOW

class Dork:
    tmp = []; result = []
    def __init__(self):
        self.proxy = []
        self.search_engine = ""
        self.type_proxy = ""

    def save_file(self):
        try:
            if self.result:
                file_name = input('[?] Save AS : ')
                if file_name: file_name = file_name
                else: print("Using Default : fiola_dorking.txt"); file_name = "fiola_dorking.txt"
                open(file_name, 'a+', encoding='utf8').write('\n'.join(list(dict.fromkeys(self.result))))
                print(f"Total Domain : {len(list(dict.fromkeys(self.result)))}\n{green}[+]{reset} Save on {file_name}"); exit()
            else:
                print(f"{red}Error: {reset}Result Empty.. Cannot Save!"); exit()
        except KeyboardInterrupt: print(f"{red}Error: {reset}File Not Saving"); exit()
        except Exception as e: print(f"{red}Error: {reset}{e}")

    def search(self, dork):
        try:
            se = open(self.search_engine, 'r', encoding='utf8').read().splitlines()
            for searcheng in se:
                if self.proxy:
                    proxies = {
                        self.type_proxy: random.choice(self.proxy)
                    }
                else: proxies = None
                req = requests.get(searcheng.replace('{FiolaDork}', dork), headers={'User-Agent': ua.random}, proxies=proxies).text
                if 'captcha' in req:
                    input(f"\n{red}Error:{reset} Captcha Detected, Please Change You IP Using VPN Or Use Good Proxies. Press Enter For Continue... ")
                regx = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', req)
                if regx:
                    for domain in regx:
                        self.result.append(domain)
                        #print(green+'\n'.join(list(dict.fromkeys(self.result)))+reset)
                    print(green+'\n'.join(list(dict.fromkeys(regx)))+reset)
                else: print(f"{red}[-]{reset} Can't Get Domain")
        
        except FileNotFoundError:
            print(f"\n{red}Error: {reset}File {self.search_engine} Was NotFound..."); exit()

    def main(self):
        try:
            if os.name == 'nt': os.system('cls')
            else: os.system('clear')
            banner = f'''
\tCreated by {green}fooster1337 {reset}& {green}@GrazzMean{reset} | {red}github.com/fooster1337{reset}            
            '''
            print(banner)
            #print(banner)
            dork = open(input("\t   Dork List --> "), 'r', encoding='utf8').read().splitlines()
            self.search_engine = input("\t   Search Engine (Default : FiolaDork.txt) --> ")
            if self.search_engine: self.search_engine = self.search_engine
            else: print("\t   Using Default : FiolaDork.txt"); self.search_engine = "FiolaDork.txt"
            proxyI = input("\t   Proxy List (Blank If You Not Use Proxy) --> ")
            if proxyI:
                self.type_proxy = input("\t   Proxy Type (http|https|tcp) --> ")
                type = ['http', 'https', 'tcp']
                if self.type_proxy not in type: print(f"{red}Error: {reset}Only Accept http/https/tcp Proxy"); exit()
                else: self.type_proxy = self.type_proxy; lproxy = open(proxyI, 'r', encoding='utf8').read().splitlines(); self.proxy.extend(lproxy)
            else: pass
            # self.thread = input("\t   Thread (Default : 10) --> ")
            # if self.thread: self.thread = int(self.thread)
            # else: self.thread = 10
            print(f"\nDork : {len(dork)} \nProxy : {len(self.proxy)}")
            print("[!] Starting Dorking...")
            #signal.signal(signal.SIGTERM, signal_handler)
            try:
                for dork1 in dork:
                    self.search(dork1)
            except KeyboardInterrupt:
                print(f"\n{red}Error: {reset}Ctrl+C Detected..., Save File...")
                    #exiting.set()
                time.sleep(1)
                self.save_file()


        except FileNotFoundError: print(f"\n{red}Error: {reset}The file you entered doesn't exist..., Try Again."); exit()
        except Exception as e: print(f"\n{red}Error: {reset}{e}"); pass
    
if __name__ == "__main__":
    Dork().main()
