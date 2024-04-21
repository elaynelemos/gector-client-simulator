# gector-client-simulator

```bash
cd gector-client-simulator
source .venv/bin/activate

python3 sentences_correction.py http://34.73.53.229 1 outputs/c3-highcpu-8

QUERY_MEMORY='(1 - ((avg_over_time(node_memory_MemFree_bytes{job="c3-highcpu-8"}[30s]) + avg_over_time(node_memory_Cached_bytes{ job="c3-highcpu-8"}[30s]) + avg_over_time( node_memory_Buffers_bytes{job="c3-highcpu-8"}[30s])) / avg_over_time(node_memory_MemTotal_bytes{job="c3-highcpu-8"} [30s])))'

QUERY_CPU='(avg without (mode,cpu) (1 - rate(node_cpu_seconds_total{mode="idle", job="c3-highcpu-8"}[30s])))'

PROMETHEUS_IP='52.237.133.255'
START_TIMESTAMP='1713625685'
END_TIMESTAMP='1713625879'
ITERATION_ID='10'

python3 prometheus_data.py --url "http://${PROMETHEUS_IP}:9090" --query "${QUERY_MEMORY}" --start "${START_TIMESTAMP}" --end "${END_TIMESTAMP}" --step 5s --metric_title memory --iteration_number "${ITERATION_ID}"
```
