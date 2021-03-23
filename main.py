
import os
import shutil

caminho_original = r'D:\IMGcelular'
caminho_novo = r'D:\IMGcelularSreenshot'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existente.')


for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if 'Screenshot' in file:
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} movido com sucesso.')
