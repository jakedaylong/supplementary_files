# in test_users.py
import pytest

def fake_get_user_data(username, passwprd):
    return [["andy", "xyz"], "fred", "abc"]

@pytest.fixture
def gh_patched(monkeypatch):
    from src.project.lessons.lesson01.extras.users import get_user_data
    monkeypatch.setattr(project.lessons.lesson01.extras.users, get_user_data, fake_get_user_data)

def test_get_user_data(gh_patched):
    from project.lessons.lesson01.extras.users import get_user_data
    assert 'andy' in get_user_data('andy', 'mypw')
