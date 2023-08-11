class FlatIterator():

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_counter = 0
        self.element_counter = -1
        return self

    def __next__(self):
        self.element_counter += 1
        while self.list_counter < len(self.list_of_list):
            if self.element_counter >= len(self.list_of_list[self.list_counter]):
                self.list_counter += 1
                self.element_counter = 0
            else:
                return self.list_of_list[self.list_counter][self.element_counter]
        raise StopIteration


class FlatIterator_2():

    def __init__(self, list_of_list):
        self.list_of_list = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_of_list:
            try:
                element = next(self.list_of_list[-1])
                if isinstance(element, list):
                    self.list_of_list.append(iter(element))
                else:
                    return element
            except StopIteration:
                self.list_of_list.pop()
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator_2(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator_2(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()