import unittest
from main import Stack, is_balanced
from parameterized import parameterized

test_stack_1 = Stack([1, 2, 3])
test_stack_2 = Stack([1, 2, 3])
test_stack_3 = Stack([1, 2, 3])

EXAMPLES = [
    ('(((([{}]))))', "Сбалансированно"),
    ('[[{())}]', 'Несбалансированно'),
    ("print('Каждая, глава?')['напоминает', о том, {1: как важно, 2: ещё в детстве}]", 'Сбалансированно'),
    ("print('узнать, что значит ?')[дружба, смелость, {}", "Несбалансированно")

]


class TestStack(unittest.TestCase):

    def test_is_empty(self):
        result = test_stack_1.is_empty()
        self.assertFalse(result)

    def test_push(self):
        test_stack_3.push(4)
        result = [1, 2, 3, 4]
        self.assertEqual(test_stack_3, result)

    def test_pop(self):
        result = test_stack_2.pop()
        self.assertEqual(result, 2)

    def test_peek(self):
        result = test_stack_1.peek()
        self.assertEqual(result, 3)

    def test_size(self):
        result = test_stack_1.size()
        self.assertEqual(result, 3)


class TestIsBalanced(unittest.TestCase):

    @parameterized.expand(EXAMPLES)
    def test_is_balanced(self, a, exp_result):
        result = is_balanced(a)
        self.assertEqual(exp_result, result)
