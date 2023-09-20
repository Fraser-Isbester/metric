[![Check All](https://github.com/Fraser-Isbester/metric/actions/workflows/check.yaml/badge.svg)](https://github.com/Fraser-Isbester/metric/actions/workflows/check.yaml)

# ✨Abstract✨ metrics
A lightweight framework for defining arbitrary business metrics as Python code.

# Basic Usage

Let's say you want to write a metric that checks if one of your applications follows your organizations application naming standards. Here's how we could write that metric, and calculate compliance:

```python

from metric import Application, ApplicationMetric
from metric.utils import MatrixRunner
from metric.types import OutputFormat
import requests

def main():
    apps = [
        Application(app) for app in [
            "myorg-finance-app", "myorg-marketing-service",
            "myorg-sales-app", "sandbox-dinasour"
        ]
    ]
    metrics = [AppNameCompliance, AppAPIConformaty]

    # This returns ApplicationMetric's, but we'll just read stdout. 
    MatrixRunner(format=OutputFormat.OUTPUT_FORMAT_TABLE).run(apps, metrics)

class AppNameCompliance(ApplicationMetricBoolean):
    """All Applications should be named myorg-<appname>."""

    def compute(self):
        if self.application.name.startswith("myorg-"):
            return True, True
        return False, False

class AppAPIConformaty(ApplicationMetricBoolean):
    """All Applications should have predictable endpoints based on name.
    e.g. - myorg-finance-service -> api.myorg.com/finance
         - sandbox-dinasour -> api.myorg.com/sandbox_dinasour
    """

    def compute(self):
        r = requests.get(f"https://api.myorg.com/{self.app_name_to_method()}")
        if r.ok:
            return True
        return False
    
    def app_name_to_method(self):
        return self.application.name \
            .replace("myorg-", "") \
            .replace("-service", "") \
            .replace("-", "_")
```

If we run this code, we'll get the following output:

```bash
Application             AppNameCompliance       AppAPIConformaty
myorg-finance-app                    True                  False
myorg-marketing-service              True                  False
myorg-sales-app                      True                  False
sandbox-dinasour                    False                  False
```
