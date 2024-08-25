from app.objs import Person


def test_person():
    person = Person(name='Danny', age=16, address='unknown')
    assert person.age == 16