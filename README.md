# gector-client-simulator

```bash
cd gector-client-simulator
source .venv/bin/activate

python3 sentences_correction.py http://104.196.141.119 1 outputs/n2-custom-8-16384

QUERY_MEMORY='(1 - ((avg_over_time(node_memory_MemFree_bytes{job="n2-custom-8-16384"}[30s]) + avg_over_time(node_memory_Cached_bytes{ job="n2-custom-8-16384"}[30s]) + avg_over_time( node_memory_Buffers_bytes{job="n2-custom-8-16384"}[30s])) / avg_over_time(node_memory_MemTotal_bytes{job="n2-custom-8-16384"} [30s])))'

QUERY_CPU='(avg without (mode,cpu) (1 - rate(node_cpu_seconds_total{mode="idle", job="n2-custom-8-16384"}[30s])))'

START_TIMESTAMP='1713625685'
END_TIMESTAMP='1713625879'
ITERATION_ID='10'

python3 prometheus_data.py --url "http://${PROMETHEUS_IP}:9090" --query "${QUERY_MEMORY}" --start "${START_TIMESTAMP}" --end "${END_TIMESTAMP}" --step 5s --metric_title memory --iteration_number "${ITERATION_ID}"
```
