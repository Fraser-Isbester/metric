# examples/basic/examples.py
from metrics.protocols import Application, ApplicationMetric
import datetime

class ExampleApplication(Application):
    def __init__(self, name):
        self.name = name

class ExampleMetric(ApplicationMetric):
    def __init__(self, application):
        self.application = application
        self.computed_at = None
        self.errors = []
        self._value = None

    @property
    def value(self) -> float | None:
        return self._value

    def compute(self) -> bool:
        try:
            self._value = 42  # An example metric computation
            self.computed_at = datetime.datetime.now()
            return True
        except Exception as e:
            self.errors.append(e)
            return False
