import requests
import pyfiglet

def domain_scanner(domain_name,sub_domnames):
    print('----URL Scan----')
      
    
    for subdomain in sub_domnames:
        
        
        url = f"https://{subdomain}.{domain_name}"
          
        
        try:
            
            requests.get(url)
              
            
            print(f'[+] {url}')
              
            
        except requests.ConnectionError:
            pass
  
# main function
if __name__ == '__main__':
    banner = pyfiglet.figlet_format("""IDSEC
SHARKIN""")
    print(banner)
    dom_name = input("Domain Name Giriniz:")
  
    
    with open('domain.txt','r') as file:
        
        
        name = file.read()
          
        
        sub_dom = name.splitlines()
          
    
    domain_scanner(dom_name,sub_dom)
     