from ai import accept, reject, first, nextBoard, isValidRectangle, Board, Problem


def test(name, num):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print(f'{name} test {num}')
            func(*args, **kwargs)
        return wrapped_func
    return decorator


@test('first()', 1)
def first_test1():
    problem = Problem(n=5, init_board=[(4, 2)])
    expected = [(4, 2), (0, 0)]
    actual = first(P=problem, c=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('first()', 2)
def first_test2():
    problem = Problem(n=5, init_board=[(0, 0)])
    expected = [(0, 0), (0, 1)]
    actual = first(P=problem, c=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('first()', 3)
def first_test3():
    problem = Problem(n=5, init_board=[(0, 0), (3, 4)])
    expected = [(0, 0), (3, 4), (0, 1)]
    actual = first(P=problem, c=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")

# nextBoard() tests


@test('nextBoard()', 1)
def nextBoard_test1():
    problem = Problem(n=5, init_board=[(0, 0), (3, 4), (0, 1)])
    expected = [(0, 0), (3, 4), (0, 2)]
    actual = nextBoard(P=problem, s=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('nextBoard()', 2)
def nextBoard_test2():
    problem = Problem(n=5, init_board=[(0, 0), (3, 4), (2, 3)])
    expected = [(0, 0), (3, 4), (2, 4)]
    actual = nextBoard(P=problem, s=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('nextBoard()', 3)
def nextBoard_test3():
    problem = Problem(n=5, init_board=[(2, 1), (0, 0), (0, 1)])
    expected = [(2, 1), (0, 0), (0, 2)]
    actual = nextBoard(P=problem, s=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('nextBoard()', 4)
def nextBoard_test4():
    problem = Problem(n=5, init_board=[(0, 0), (1, 2), (1, 3)])
    expected = [(0, 0), (1, 2), (1, 4)]
    actual = nextBoard(P=problem, s=problem.init_board)
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('isValidRectangle()', 1)
def isValidRectangle_test1():
    expected = False
    actual = isValidRectangle((1, 1), (1, 1))
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('isValidRectangle()', 2)
def isValidRectangle_test2():
    expected = False
    actual = isValidRectangle((1, 1), (1, 2))
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('isValidRectangle()', 3)
def isValidRectangle_test3():
    expected = False
    actual = isValidRectangle((3, 2), (1, 2))
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('isValidRectangle()', 4)
def isValidRectangle_test4():
    expected = True
    actual = isValidRectangle((3, 2), (4, 4))
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('isValidRectangle()', 5)
def isValidRectangle_test5():
    expected = True
    actual = isValidRectangle((2, 1), (4, 2))
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('isValidRectangle()', 6)
def isValidRectangle_test6():
    expected = True
    actual = isValidRectangle((4, 1), (0, 2))
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('accept()', 1)
def accept_test1():
    problem = Problem(n=5, init_board=[(0, 0)])
    expected = True
    actual = accept(P=problem, c=[(0, 0), (3, 1), (1, 2), (4, 3), (2, 4)])
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('accept()', 2)
def accept_test2():
    problem = Problem(n=5, init_board=[(0, 3)])
    expected = False
    actual = accept(P=problem, c=[(0, 3), (3, 0), (1, 1), (2, 4), (4, 2)])
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('reject()', 1)
def reject_test1():
    problem = Problem(n=5, init_board=[(0, 0)])
    expected = False
    actual = reject(P=problem, c=[(0, 0), (3, 1), (1, 2), (4, 3), (2, 4)])
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('reject()', 2)
def reject_test2():
    problem = Problem(n=5, init_board=[(0, 3)])
    expected = True
    actual = reject(P=problem, c=[(0, 3), (3, 0), (1, 1), (2, 4), (4, 2)])
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


@test('reject()', 3)
def reject_test3():
    problem = Problem(n=5, init_board=[(0, 0)])
    expected = False
    actual = reject(P=problem, c=[(0, 0), (3, 1), (1, 2)])
    print(f"{'passed' if expected == actual else 'failed'}")
    if not expected == actual:
        print(f"expected {expected}, actual: {actual}")


first_test1()
first_test2()
first_test3()

nextBoard_test1()
nextBoard_test2()
nextBoard_test3()
nextBoard_test4()

isValidRectangle_test1()
isValidRectangle_test2()
isValidRectangle_test3()
isValidRectangle_test4()
isValidRectangle_test5()

accept_test1()
accept_test2()

reject_test1()
reject_test2()
reject_test3()
