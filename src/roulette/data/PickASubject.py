"""The main pick a subject script."""
from src.roulette.data.subject.SubjectBuilder import SubjectBuilder


class PickASubject:
    """Basic starting logic"""
    @staticmethod
    def main():
        subject_list = []
        if len(subject_list) != 0:
            pass
        else:
            print("No subjects detected, Moving to create a subject.")
            new_subject = SubjectBuilder.build_subject()
            # call build subject

        # if subjects in db:
            # if edit subjects selected:
                # edit the subjects

            # Select a subject or all subjects
            # if topics in Subject:
                # if edit:
                    # edit the topics

                # if play:
                    # Start roullete
                    # update Graph and stats
                    # ask to spin again, or pick new subject

            # if No topics:
                # Call Topic builder

        # if No subjects in db:
            # Call build Subject
