# tests/test_application_metric_protocol.py

import datetime
from numbers import Number
from metrics.types import (
    Application,
    ApplicationMetricBoolean,
    ApplicationMetricNumeric,
)


# Test Application: that app.name exists and is a non-empty string
def test_example_application_conforms_to_protocol():
    app = Application("test-app")
    assert isinstance(app.name, str), "Application name must be a string"
    assert app.name == "test-app", "Application name cannot be empty or None"


def test_ApplicationMetricBoolean_instantiation():
    app = Application("test-app")

    class AlwaysTrueMetric(ApplicationMetricBoolean):
        def compute(self):
            return True

    metric = AlwaysTrueMetric(app)

    assert metric.application is not None, "Metric must have an Application"
    assert (
        metric.computed_at is None
    ), "Metric must not have a computed_at value before compute() is called"
    assert (
        metric.errors == []
    ), "Metric must not have any errors before compute() is called"
    assert (
        metric.value is None
    ), "Metric must not have a value before compute() is called"


def test_ApplicationMetricBoolean_compute():
    app = Application("test-app")

    class AlwaysTrueMetric(ApplicationMetricBoolean):
        def compute(self):
            return True

    metric = AlwaysTrueMetric(app)
    metric.value = metric.compute()

    print(metric)

    assert metric.computed_at is not None, "Metric must have a computed_at value."
    assert isinstance(
        metric.computed_at, datetime.datetime
    ), "metric.computed_at must be a datetime."
    assert metric.errors == [], "Metric must not have any errors."
    assert metric.value is True, "Metric must have a value of True."
    assert isinstance(metric.value, bool), "metric.value must be a boolean."


def test_ApplicationMetricNumeric_instantiation():
    app = Application("test-app")

    class Always50pMetric(ApplicationMetricNumeric):
        def compute(self):
            return 0.50

    metric = Always50pMetric(app)

    assert metric.application is not None, "Metric must have an Application"
    assert (
        metric.computed_at is None
    ), "Metric must not have a computed_at value before compute() is called"
    assert (
        metric.errors == []
    ), "Metric must not have any errors before compute() is called"
    assert (
        metric.value is None
    ), "Metric must not have a value before compute() is called"


def test_ApplicationMetricnumeric_compute():
    app = Application("test-app")

    class Always50pMetric(ApplicationMetricNumeric):
        def compute(self):
            return 0.50

    metric = Always50pMetric(app)
    metric.value = metric.compute()

    print(metric)

    assert metric.computed_at is not None, "Metric must have a computed_at value."
    assert isinstance(
        metric.computed_at, datetime.datetime
    ), "metric.computed_at must be a datetime."
    assert metric.errors == [], "Metric must not have any errors."
    assert metric.value == 0.50, "Metric must have a value of True."
    assert isinstance(metric.value, Number), "metric.value must be a numeric."
