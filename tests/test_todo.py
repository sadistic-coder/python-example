from todo import __version__
from todo.entity import Todo


def test_version():
    assert __version__ == '0.1.0'


def test_create_todo():
    todo = Todo("test todo", "just test instance")
    assert todo is not None
