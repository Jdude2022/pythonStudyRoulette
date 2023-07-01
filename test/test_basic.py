from src.roulette.data.subject.Subject import Subject
import pytest


class TestClass:

    @pytest.mark.parametrize("name", ["Math", "Science", "Bob", "Art"])
    def test_subject(self, name):
        new_subject = Subject(name, 1)
        assert new_subject.name == name 

    @pytest.mark.parametrize("topic_num", [1, 2, 3, 4, 5, 50])
    def test_subject_topics(self, topic_num):
        new_subject = Subject("Math", topic_num)
        assert new_subject.num_topics == topic_num
