from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in instance._data:
        if i['nome_do_arquivo'] == path_file:
            sys.stderr.write(f'O arquivo {path_file} já foi importado\n')
            return

    archive = txt_importer(path_file)

    if archive is None:
        return
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(archive),
        'linhas_do_arquivo': archive
    }

    instance.enqueue(data)
    print(data)


def remove(instance):
    if len(instance) > 0:
        remove = instance.dequeue()
        print(f'Arquivo {remove["nome_do_arquivo"]} removido com sucesso')
    else:
        print('Não há elementos')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
