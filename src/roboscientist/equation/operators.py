import numpy as np


class Operator:
    def __init__(self, func, name, repr, arity):
        self.func = func
        self.name = name
        self.repr = repr
        self.arity = arity


def _SAFE_LOG_FUNC(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(x > 0.01, np.log(np.abs(x)), 0.0)


def _SAFE_SQRT_FUNC(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(x > 0, np.sqrt(np.abs(x)), 0.0)


OPERATORS = {
    'add': Operator(
        func=lambda x, y: x + y,
        name='add',
        repr=lambda x, y: f'({x} + {y})',
        arity=2,
    ),
    'sub': Operator(
        func=lambda x, y: x - y,
        name='sub',
        repr=lambda x, y: f'({x} - {y})',
        arity=2,
    ),
    'mul': Operator(
        func=lambda x, y: x * y,
        name='mul',
        repr=lambda x, y: f'({x} * {y})',
        arity=2,
    ),
    'sin': Operator(
        func=lambda x: np.sin(x),
        name='sin',
        repr=lambda x: f'sin({x})',
        arity=1,
    ),
    'cos': Operator(
        func=lambda x: np.cos(x),
        name='cos',
        repr=lambda x: f'cos({x})',
        arity=1,
    ),
    'safe_log': Operator(
        func=lambda x: _SAFE_LOG_FUNC(x),
        name='safe_log',
        repr=lambda x: f'log({x})',
        arity=1,
    ),
    'safe_sqrt': Operator(
        func=lambda x: _SAFE_SQRT_FUNC(x),
        name='safe_sqrt',
        repr=lambda x: f'sqrt({x})',
        arity=1,
    ),
}


VARIABLES = {
    'x1': 0,
    'x2': 1,
    'x3': 2,
    'x4': 3,
    'x5': 4
}
CONST_SYMBOL = 'const'


if __name__ == '__main__':
    print(_SAFE_LOG_FUNC(np.array([0, 1, -1, 3])))