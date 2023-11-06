import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priorityQueue = PriorityQueue()
    items = [1, 2, 3, 4, 5]

    for item in items:
        priorityQueue.enqueue({"qtd_linhas": item})

    assert len(priorityQueue) == 5
    assert priorityQueue.high_priority.data.head.item["qtd_linhas"] == 5

    priorityQueue.dequeue()
    data = priorityQueue.search(1)

    assert data["qtd_linhas"] == 4

    with pytest.raises(IndexError):
        priorityQueue.search(10)
