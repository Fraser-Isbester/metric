# Contains various metric runners

from enum import Enum
from typing import List, Union

from metrics.types import OutputFormat
from metrics.types import base as t


class BaseRunner:
    r"""Defines the base-runner for metrics generation."""


class MatrixRunner(BaseRunner):
    r"""A runner that builds & computes every metric for every application specified."""

    def run(
        self,
        metrics: List[t.ApplicationMetric],
        applications: Union[List[t.Application], List[str]],
        format: Enum = OutputFormat.OUTPUT_FORMAT_LOG,
    ) -> List[t.ApplicationMetric]:
        r"""Builds & Runs metric generation."""

        if not isinstance(format, OutputFormat):
            raise TypeError(
                f"Expected type to be `{type(OutputFormat)}`, got `{type(format)}`"
            )

        application_metrics = []
        for application in applications:
            # If string passed, convert to Application object.
            if isinstance(application, str):
                application = t.Application(name=application)

            for Metric in metrics:
                metric = Metric(application)  # type: ignore
                metric.compute_and_set()
                application_metrics.append(metric)

                if format == OutputFormat.OUTPUT_FORMAT_LOG:
                    metric_name = metric.__class__.__name__
                    app_name = metric.application.name
                    print(f"{app_name}/{metric_name:<20}: {metric.value:.1f}")

        return application_metrics
