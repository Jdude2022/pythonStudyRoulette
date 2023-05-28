"""Subject Object."""


class Subject:
    """class for subjects"""
    def __init__(self, name:str, num_topics: int) -> None:
        self.__name: str = name
        self.__num_topics: int = num_topics
        self.__topic_list: list = []
        while self.num_topics != len(self.topic_list) + 1:
            self.add_topic()

    @property
    def name(self):
        return self.__name

    @property
    def num_topics(self):
        return self.__num_topics


    @property
    def topic_list(self):
        return self.__topic_list

    def add_topic(self):
        """Adds a topic to the topic bank"""
        # Topic is (Name, Perentage, min_time)
        # new_topic = topicBuilder.build_topic(Name, Percentage, Min_time)
        # self.topic_list.append(new_topic)
        pass

    def edit_topic(self):
        """Searches through topic_list"""
        # new_list
        # for i, name in enumerate(topic list):
            #new_list.add((name, i))
        # print new list to edit the topic
        pass
