from function import Stack, check_balance
from data import BALLANCED_LIST, UNBALLANCED_LIST


if __name__ == '__main__':
    s = Stack()
    print(f'функция is_empty - {s.is_empty()}')
    s.push(1)
    s.push(2)
    s.push(6)
    print(f'функция size - {s.size()}')
    print(f'функция peek - {s.peek()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция size - {s.size()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция pop - {s.pop()}')

    for row in UNBALLANCED_LIST:
        print(check_balance(row))

    print()
    for row in BALLANCED_LIST:
        print(check_balance(row))
