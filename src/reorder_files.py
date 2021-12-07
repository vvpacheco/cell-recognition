#Este codigo serviu apenas para renomear os arquivos e salvar os nomes em um dataset csv

import os
import pandas as pd
import csv

column_names = ['original_name','new_name']
for root, _, files in os.walk("./img_cells_atypical", topdown = False):
    file_number = 100
    nomes = []
    #print(files)
    for name in files:
            extension = name.split('.')
            new_name = 'A'+file_number.__str__()+'.'+extension[-1].lower()
            full_old_name = os.path.join(root,name)
            full_new_name = os.path.join(root,new_name)
            os.rename(full_old_name,full_new_name)
            print(extension[-2])
            file_number += 1
            nomes.append([extension[-2],new_name])
print(nomes)
df = pd.DataFrame(data = nomes, columns=column_names)
df.to_csv('files_atypical.csv',sep=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC,index=False)
#print(df.head())