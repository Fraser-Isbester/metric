# examples/basic/examples.py

from metrics.types import (
    Application,
    ApplicationMetricBoolean,
    ApplicationMetricNumeric,
)
from metrics.utils import MatrixRunner


def main():
    apps = [
        Application("examples-service-1"),
        Application("examples-service-2"),
        Application("silly-service"),
    ]
    metrics = [AppNameCompliance, AppNameLength]
    MatrixRunner().run(metrics, apps)


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


if __name__ == "__main__":
    main()
