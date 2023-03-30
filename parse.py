import yaml
from csv import writer

def aft_alqaeda_forfeit_vc():
    with open('packs/aft-alqaeda-forfeit_vc.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                temp = [i['address'],'crime','terrorism']
                writer_object.writerow(temp)
            writer_object.writerow([])
            
        
def alt_right():
    with open('packs/Alt-Right.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                if(i['currency']=='BTC'):
                    temp = [i['address'],'crime','extremism']
                    writer_object.writerow(temp)
            writer_object.writerow([])
            
def binance_hack():
    with open('packs/binance_hack.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                temp = [i['address'],'crime','binance hack']
                writer_object.writerow(temp)
            writer_object.writerow([])    
            
def blender_io():
    with open('packs/blender_io.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                temp = [i['address'],'service','mixing service']
                writer_object.writerow(temp)
            writer_object.writerow([])           

def chaininfo():
    with open('packs/chaininfo.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                temp = [i['address'],'service','exchange']
                writer_object.writerow(temp)
            writer_object.writerow([])  
            

def electrum_phishing():
    with open('packs/electrum_phishing.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                if(i['currency']=='BTC'):
                    temp = [i['address'],'hack','phishing']
                    writer_object.writerow(temp)
            writer_object.writerow([])

def etherscamdb_tagpack():
    with open('packs/etherscamdb_tagpack.yaml', 'r') as file:
        text = yaml.safe_load(file)['tags']
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2)
            for i in text:
                if(i['currency']=='BTC'):
                    temp = []
                    if(i['abuse']=='scam'):
                        temp = [i['address'],'crime','scam']
                    else:
                        temp = [i['address'],'hack','phishing']
                    writer_object.writerow(temp)
            writer_object.writerow([])
            

        
    
    
