"""Builds Subject Object when User Requests."""
from src.roulette.data.subject.Subject import Subject

class SubjectBuilder:
    """Builds subjects."""
    @staticmethod
    def build_subject():
        subject_name = input("Please input subject name ")
        number_of_topics = input(" Please input the number of topics must be" +
                                 "a number ")
        while number_of_topics.isdigit() is False:
                print("invalid input Please input a whole number.")
                number_of_topice = input(" Please input the number of topics" + 
                                         "must be a number ")

        new_subject = Subject(subject_name, int(number_of_topics))
        print(new_subject.name)
        print(new_subject.num_topics)
        """Builds the subject."""
        # gets name of the subject
        # gets num of topics
        # creats new subject with name and number of topics
        # for i in num of topics:
            # calls new_subject.add_topic
