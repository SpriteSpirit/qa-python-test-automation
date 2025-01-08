import pytest
from lesson_09.student import Student, session


@pytest.fixture
def new_student():
    return Student(name="Пётр Пустота", age=20)


def test_add_student(new_student):
    # Добавление студента
    session.add(new_student)
    session.commit()

    # Проверка, что студент добавлен
    student = session.query(Student).filter_by(name="Пётр Пустота").first()
    assert student is not None
    assert student.name == "Пётр Пустота"
    assert student.age == 20

    # Удаление студента после теста
    session.delete(student)
    session.commit()


def test_update_student(new_student):
    # Добавление студента
    session.add(new_student)
    session.commit()

    # Изменение студента
    student = session.query(Student).filter_by(name="Пётр Пустота").first()
    student.age = 21
    session.commit()

    # Проверка, что студент обновлен
    updated_student = session.query(Student).filter_by(name="Пётр Пустота").first()
    assert updated_student.age == 21

    # Удаление студента после теста
    session.delete(updated_student)
    session.commit()


def test_delete_student(new_student):
    # Добавление студента
    session.add(new_student)
    session.commit()

    # Удаление студента
    student = session.query(Student).filter_by(name="Пётр Пустота").first()
    session.delete(student)
    session.commit()

    # Проверка, что студент удален
    deleted_student = session.query(Student).filter_by(name="Пётр Пустота").first()
    assert deleted_student is None
