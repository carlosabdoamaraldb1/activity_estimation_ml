from .dev import Developer
from .task import Task


class Instance:
    def __init__(
            self,
            task: Task,
            developer: Developer,
            rh_cost_estimation: float,
            rh_cost_real: float
    ) -> None:
        self.task = task
        self.dev = developer
        self.rh_cost_estimation = rh_cost_estimation
        self.rh_cost_real = rh_cost_real

    def get_rh_cost_estimation(self):
        return
