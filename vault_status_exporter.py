import socket
import json
import time
import urllib2
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

class VaultSealStatusCollector(object):
  def collect(self):
    metric = GaugeMetricFamily(
        'vault_seal_status',
        'Vault Seal Status',
        labels=["vault_seal_status"])

    url = 'https://{}:$PORT/v1/sys/seal-status'.format(socket.gethostname())
    result = json.load(urllib2.urlopen(url))

    status = {}
    if result['sealed']:
      status = 1
    elif not result['sealed']:
      status = 0
    metric.add_metric('vault_seal_status', status)

    yield metric

if __name__ == "__main__":
  REGISTRY.register(VaultSealStatusCollector())
  start_http_server($HTTP_PORT)
  while True: time.sleep(1)

