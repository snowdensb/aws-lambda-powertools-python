from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

metrics = Metrics(namespace="ExampleApplication", service="booking")


@metrics.log_metrics
def lambda_handler(evt, ctx):
    metrics.add_metric(name="SuccessfulBooking", unit=MetricUnit.Count, value=1)
    metrics.add_metadata(key="booking_id", value="booking_uuid")
