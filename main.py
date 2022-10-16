

class Stack(list):

    def is_empty(self):
        """Проверка стека на пустоту"""
        return self == []

    def size(self):
        """Возвращает количество элементов в стеке"""
        return len(self)

    def push(self, new_element):
        """Добавляет новый элемент на вершину стека"""
        self.append(new_element)

    def pop(self, **kwargs):
        """Удаляет верхний элемент стека"""
        if self.size() >= 2:
            self.remove(self[-1])
            return self[-1]
        elif self.size() == 1:
            self.remove(self[0])
            return self
        else:
            return self

    def peek(self):
        """Возвращает верхний элемент стека, но не удаляет его"""
        return self[-1]


def is_balanced(qqq):
    """Проверка сбалансированности скобок"""
    stack = Stack()
    for el in qqq:
        if el == '(' or el == '[' or el == '{':
            stack.push(el)
        else:
            if el == ')' and stack.peek() == '(':
                stack.pop()
            elif el == ']' and stack.peek() == '[':
                stack.pop()
            elif el == '}' and stack.peek() == '{':
                stack.pop()
    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == '__main__':
    pass
