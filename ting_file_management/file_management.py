import sys


def txt_importer(path_file):
    try:
        if '.txt' in path_file:
            with open(path_file, 'r') as file:
                return file.read().split('\n')
        else:
            sys.stderr.write('Formato inválido\n')
            return None
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return None
