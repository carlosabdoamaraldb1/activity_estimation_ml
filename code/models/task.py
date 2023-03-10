import datetime


class Task:
    def __init__(
        self,
        id: str,
        squad: str,
        link: str,
        stack: str,
        category: str,
        repository_count: int,
        complexity_level: int,
        estimation: float,
        real_time: float,
        start_at: datetime.datetime,
        end_at: datetime.datetime,
        qa_situations_count: int,
        dev_situations_count: int,
        unit_tests_count: int,
    ) -> None:
        self.id = id
        self.squad = squad
        self.link = link
        self.stack = stack
        self.category = category
        self.repository_count = repository_count
        self.complexity_level = complexity_level
        self.estimation = estimation
        self.real_time = real_time
        self.start_at = start_at
        self.end_at = end_at
        self.qa_situations_count = qa_situations_count
        self.dev_situations_count = dev_situations_count
        self.unit_tests_count = unit_tests_count
