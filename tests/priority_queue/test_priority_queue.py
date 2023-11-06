import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()
    test1 = {
        "nome_do_arquivo": "name1",
        "qtd_linhas": 6,
        "linhas_do_arquivo":
            ['line1', 'line2', 'line3', 'line4', 'line5', 'line6']
    }
    test2 = {
        "nome_do_arquivo": "name2",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['line1', 'line2', 'line3']
    }
    test3 = {
        "nome_do_arquivo": "name3",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ['line1', 'line2']
    }
    pq.enqueue(test1)
    assert len(pq) == 1
    assert pq.is_priority(test1) is False
    assert pq.search(0) == test1

    pq.enqueue(test2)
    assert len(pq) == 2
    assert pq.is_priority(test2) is True
    assert pq.search(0) == test2

    pq.enqueue(test3)
    assert len(pq) == 3
    assert pq.is_priority(test3) is True
    assert pq.search(1) == test3

    pq.dequeue()
    assert len(pq) == 2

    pq.dequeue()
    assert len(pq) == 1

    pq.dequeue()
    assert len(pq) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(-1)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(4)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(len(pq))
