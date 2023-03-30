import yaml
from csv import writer
import os

file_names = os.listdir(os.curdir+'/packs')

for file_name in file_names: 
    with open('packs/'+file_name, 'r') as file:
        text = yaml.safe_load(file)
        with open('tag.csv',mode = 'a', newline='') as file2:
            writer_object = writer(file2) 
            for i in text['tags']:
                if('currency' in text):
                    if(text['currency']!='BTC'):
                        break
                elif('currency' in i):
                    if(i['currency']!='BTC'):
                        continue
                category = ''
                if('category' in text):
                    category = text['category']
                elif('category' in i):
                    category = i['category']

                abuse = ''
                if('abuse' in text):
                    abuse = text['abuse']
                elif('abuse' in i):
                    abuse = i['abuse']
                
                    
                temp = [i['address'],category,abuse]
                writer_object.writerow(temp)
            writer_object.writerow([])