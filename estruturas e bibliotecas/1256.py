class HashTable:

    def __init__(self, size: int):
        self.table = [
            [] for _ in range(size)
        ]

    def add(self, item: int) -> None:
        hash_value = self._hash(item)
        self.table[hash_value].append(item)

    def _hash(self, item: int) -> int:
        return item % len(self.table)

    def __str__(self):
        positions = []

        for index, row in enumerate(self.table):
            if not row:
                positions.append('{} -> \\'.format(index))
            else:
                arrowed_itens = ' -> '.join(map(str, row))
                positions.append('{} -> {} -> \\'.format(index, arrowed_itens))

        return '\n'.join(positions)


if __name__ == '__main__':
    answers = []
    for question in range(int(input())):
        m = int(input().split()[0])

        hash_table = HashTable(m)

        inputed_items = map(int, input().split())
        for i in inputed_items:
            hash_table.add(i)

        answers.append(str(hash_table))

    print('\n\n'.join(answers))
