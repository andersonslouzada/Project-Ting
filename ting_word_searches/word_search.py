def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        data = instance.search(i)
        name = data['nome_do_arquivo']
        ocurrences = []

        for number, line in enumerate(data['linhas_do_arquivo'], start=1):
            if word.lower() in line.lower():
                ocurrences.append({'linha': number})

        if ocurrences:
            result.append({'palavra': word,
                           'arquivo': name,
                           'ocorrencias': ocurrences})

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
