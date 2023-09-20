# examples/basic/examples.py

import time
from random import randint

from metrics.types import (
    Application,
    ApplicationMetricBoolean,
    ApplicationMetricNumeric,
)
from metrics.utils import MatrixRunner


def main():
    applications = [
        Application("examples-service-1"),
        Application("examples-service-2"),
        Application("silly-service"),
    ]
    metrics = [AppNameCompliance, AppNameLength, CallTime]
    runner = MatrixRunner()
    runner.run(metrics, applications)


class AppNameCompliance(ApplicationMetricBoolean):
    r"""All Application names should start with 'examples-'."""

    def compute(self):
        if self.application.name.startswith("examples-"):
            return True
        return False


class AppNameLength(ApplicationMetricNumeric):
    """All Application names must be <= 35 characters long."""

    def compute(self) -> bool:
        return len(self.application.name)


class CallTime(ApplicationMetricNumeric):
    """Captures a fake api call time."""

    def compute(self) -> bool:
        sleeptime = randint(0, 100) / 100
        time.sleep(sleeptime)
        return sleeptime


if __name__ == "__main__":
    main()
