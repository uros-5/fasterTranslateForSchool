import pyperclip,webbrowser,cyrtranslit,time,os
#print(os.getcwd())
while(True):
    try:
        n = int(input(">>>"))
        break
    except:
        temp_a = pyperclip.paste()
        a = pyperclip.paste()
        a = a.replace("\r\n"," ")
        webbrowser.open("https://translate.google.rs/#view=home&op=translate&sl=en&tl=sr&text="+str(a))
        #pyperclip.copy(a)
        while(True):
            time.sleep(1)
            if(temp_a != pyperclip.paste()):
                a = pyperclip.paste()
                a = a.replace("\r\n"," ")
                a = cyrtranslit.to_latin(a)
                pyperclip.copy(a)
                if("dokk.txt" not in os.listdir(".")):
                    fajl = open("dokk.txt","w",encoding="utf-8")
                    fajl.write(pyperclip.paste()+"\n")
                    fajl.close()
                else:
                    fajl = open("dokk.txt","a+",encoding="utf-8")
                    fajl.write(pyperclip.paste()+"\n")
                    fajl.close()
                break
            
        continue
