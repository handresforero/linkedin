from queue import PriorityQueue
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
import math
import tkinter as tk

# ###################################################################################################################################
# url_link = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106373116%22%2C%22102927786%22%2C%22100876405%22%2C%22100446943%22%5D&keywords=(Selecci%C3%B3n%20OR%20Reclutamiento%20OR%20cazatalentos%20OR%20Hunting%20OR%20head%20hunter%20)%20AND%20%22open%20to%20work%22&origin=GLOBAL_SEARCH_HEADER&sid=ePx'


PATH = "C:\Program Files (x86)\Google\chromedriver.exe" 
driver = webdriver.Chrome(PATH)

driver.get('https://www.linkedin.com/uas/login?')

driver.find_element_by_id('username').send_keys('andresdw@hotmail.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('NOse113018$')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
driver.maximize_window()
input('press enter if all is ok')

tigo = 'https://www.linkedin.com/in/marcelocataldo/recent-activity/all/'

#driver.find_element_by_xpath('').text

try:
    driver.get(tigo)
    e = '9 meses •'
    f = '10 meses •'
    g = '11 meses •'
    h = '1 año •'
    j = '2 años •'
    k = '3 años •'
    l = '8 meses •'
    d = '9 meses •'             
            

    wait2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div/div/div[4]/div/div[1]/div[2]'))) #espere campo visible

    followers = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div/div/div[4]/div/div[1]/div[2]').text

    try: wait2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li[1]/div/div/div[2]/div/div[2]/a/div[3]/span[3]/div/span/span[1]')))
    except:pass
    x = 1
    wb = load_workbook(filename = "Resultados linkedin actividad usuarios.xlsx")
    ws = wb["Sheet1"]
    while x < 6:
        
        # if (x % 5) == 0:
        #     driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL+Keys.END)    
        wait2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[2]/a/div[3]/span[3]/div/span/span[1]'))) 
        fecha = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[2]/a/div[3]/span[3]/div/span/span[1]').text 
        
        caption = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[4]/div/div/span/span').text
        
        try: likes = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[6]/ul/li[1]').text
        except: likes='NULL'
        try: comments = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[6]/ul/li[2]/button/span').text
        except: comments='NULL'
        try: shares = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[6]/ul/li[3]/button/span').text
        except: shares='NULL'

        #Hacer click en 3 botones para guardar link
        
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[3]/div/button/li-icon').click() #click 3 puntos
        wait2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[3]/div/div/div/ul/li[2]'))) #espere campo visible
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div[3]/div/div/div/ul/li[2]').click() #click guarddar link
        root = tk.Tk()
        root.withdraw()  # to hide the window
        link = root.clipboard_get()    
        
        lalista = []
        lista = []
        lalista.append(followers)
        lalista.append(fecha)
        lalista.append(caption)
        lalista.append(likes)
        lalista.append(comments)
        lalista.append(shares)
        lalista.append(link)
        lista.append(lalista)
        
        print('Registro:', '|',x, '|',fecha, '|', caption, '|', likes , '|',comments, link)
                        
        if fecha == d:
            x+=1000
        elif fecha == e:
            x+=1000
        elif fecha == f:
            x+=1000
        elif fecha == g:
            x+=1000
        elif fecha == h:
            x+=1000
        elif fecha == j:
            x+=1000
        elif fecha == k:
            x+=1000 
        
        df = pd.DataFrame(lista)
        for r in dataframe_to_rows(df, index=False, header=False):
            ws.append(r)
        x+=1
            
        
    while x < 1000:    
        
        if (x % 3) == 0:
            driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL+Keys.END) 
                
        wait2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[2]/a/div[3]/span[3]/div/span/span[1]'))) 
        
        fecha = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[2]/a/div[3]/span[3]/div/span/span[1]').text 
        
        caption = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[4]/div/div/span/span').text
        
        try: likes = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[6]/ul/li[1]').text
        except: likes='NULL'
        try: comments = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[6]/ul/li[2]/button/span').text
        except: comments='NULL'
        try: shares = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[6]/ul/li[3]/button/span').text
        except: shares='NULL'

        #Hacer click en 3 botones para guardar link
        try:
            #wait2 = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[3]/div/button/li-icon'))) 
            
            driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[3]/div/button').click() #click 3 puntos
            #wait2 = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[3]/div/div/div/ul/li[2]'))) #espere campo visible
            driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(x)+']/div/div/div[2]/div/div/div[3]/div/div/div/ul/li[2]').click() #click guarddar link
            root = tk.Tk()
            root.withdraw()  # to hide the window
            link = root.clipboard_get()
        except: link=''    
        
        lalista = []
        lista = []
        lalista.append(followers)
        lalista.append(fecha)
        lalista.append(caption)
        lalista.append(likes)
        lalista.append(comments)
        lalista.append(shares)
        lalista.append(link)
        lista.append(lalista)
        
        print('Registro:', '|',x, '|',fecha, '|', caption, '|', likes , '|',comments, link)
                        
        if fecha == d:
            x+=1000
        elif fecha == e:
            x+=1000
        elif fecha == f:
            x+=1000
        elif fecha == g:
            x+=1000
        elif fecha == h:
            x+=1000
        elif fecha == j:
            x+=1000
        elif fecha == k:
            x+=1000        
    
        df = pd.DataFrame(lista)
        for r in dataframe_to_rows(df, index=False, header=False):
            ws.append(r)
        x+=1
except Exception as error:
    print('\n','############################################','\n',error,'\n','\n',)
    
wb.save("Resultados linkedin actividad usuarios.xlsx")
wb.close()

driver.quit()
print('\n')
print('Programa terminado exitosamente, ¡¡¡You are the best, crack!!!') 
    



        
    
    
    
    
    



