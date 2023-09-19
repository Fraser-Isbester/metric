# tests/test_application_metric_protocol.py

import datetime

from examples.basic.examples import ExampleApplication, ExampleMetric


# Test Application: that app.name exists and is a non-empty string
def test_example_application_conforms_to_protocol():
    app = ExampleApplication(name="TestApp")
    assert isinstance(app.name, str), "Application name must be a string"
    assert app.name not in [None, ""], "Application name cannot be empty or None"


# Test Metric: Default "good" state of a metric
def test_example_metric_conforms_to_protocol():
    app = ExampleApplication(name="TestApp")
    metric = ExampleMetric(app)
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


# Test Metric: that compute() sets computed_at, value, and errors
def test_example_metric_computation():
    app = ExampleApplication(name="TestApp")
    metric = ExampleMetric(app)
    assert metric.compute() is True
    assert metric.value == 42
    assert isinstance(metric.computed_at, datetime.datetime)
    assert metric.errors == []
