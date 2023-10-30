"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without -
it clears the cache.

Homework is solved if solution has more than 5 symbols.


Check file with tests to see how all these classes are used. You can create any additional classes
you want.
"""
import datetime


class Name:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class Homework:
    # arguments
    def __init__(self, name_hw, deadline):
        self.name_hw = name_hw
        self.deadline = datetime.datetime.now() + datetime.timedelta(deadline)
    #deadline
    @staticmethod
    def is_expired(deadline):
        if deadline < datetime.datetime.now():
            return True
        else:
            return False


class DeadlineError(Exception):

    def __init__(self, message='You are late'):
        self.message = message
        super().__init__(self.message)


class Student(Name):

    # method
    def do_homework(self, homework: Homework, solution):
        if Homework.is_expired(homework.deadline):
            raise DeadlineError()
        else:
            return Result(homework, solution, self)


class Result:
    def __init__(self, hw: Homework, text, author: Student):
        self.hw = hw
        self.text = text
        self.author = author


class Teacher(Name):
    homework_done = {}
    # method

    @staticmethod
    def create_homework(text_mess: str, deadline: int):
        return Homework(text_mess, deadline)

    @classmethod
    def check_homework(cls, result: Result):
        if len(result.text) > 5:
            if result.hw in cls.homework_done:
                if result not in cls.homework_done[result.hw]:
                    cls.homework_done[result.hw].append(result)

            else:
                cls.homework_done[result.hw] = [result]
            return True
        else:
            cls.homework_done[result.hw] = [result.hw]
            return False

    @classmethod
    def reset_results(cls, hw: Homework = None):
        if hw:
            cls.homework_done[hw] = []
        else:
            cls.homework_done = {}
