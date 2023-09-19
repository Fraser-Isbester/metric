# metric
A lightweight framework for defining arbitrary business metrics as Python code.

# Basic Usage

Let's say you want to write a metric that checks if one of your applications follows your organizations application naming standards. Here's how we could write that metric, and calculate compliance:

```python

from metric import Application, ApplicationMetric
from metric.utils import MatrixRunner
from metric.types import OutputFormat

def main():
    apps = ["myorg-finance-app", "myorg-marketing-service", "myorg-sales-app", "sandbox-dinasour"]
    metrics = [AppNameCompliance]

    # This returns ApplicationMetric's, but we'll just read stdout. 
    MatrixRunner(format=OutputFormat.OUTPUT_FORMAT_TABLE).run(apps, metrics)

class AppNameCompliance(ApplicationMetricBoolean):
    """All Applications should be named myorg-<appname>"""

    def compute(self):
        try:
            self.value = False
            if self.application.name.startswith("myorg-"):
                self.value = True
            return True, self.value
        except Exception as e:
            self.errors.append(e)
            return False, None
```

If we run this code, we'll get the following output:

```bash
Application             AppNameCompliance
myorg-finance-app                    True
myorg-marketing-service              True
myorg-sales-app                      True
sandbox-dinasour                    False
```
