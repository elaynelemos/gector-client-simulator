# gector-client-simulator

```bash
cd gector-client-simulator
source .venv/bin/activate

curl -X POST -H "Content-Type: application/json" -d '{"sentence": "In conclusion , although the unsafe online environment , spend too much time on internet may be the potential negative factors of using online social networks .\n"}' http://4.255.32.162/correct

python3 sentences_correction.py http://4.255.32.162 1 outputs/standard-b4als-v2

QUERY_MEMORY='(1 - ((avg_over_time(node_memory_MemFree_bytes{job="standard-b4als-v2"}[30s]) + avg_over_time(node_memory_Cached_bytes{ job="standard-b4als-v2"}[30s]) + avg_over_time( node_memory_Buffers_bytes{job="standard-b4als-v2"}[30s])) / avg_over_time(node_memory_MemTotal_bytes{job="standard-b4als-v2"} [30s])))'

QUERY_CPU='(avg without (mode,cpu) (1 - rate(node_cpu_seconds_total{mode="idle", job="standard-b4als-v2"}[30s])))'

PROMETHEUS_IP='34.121.15.221'
START_TIMESTAMP='1713625685'
END_TIMESTAMP='1713625879'
ITERATION_ID='10'

python3 prometheus_data.py --url "http://${PROMETHEUS_IP}:9090" --query "${QUERY_MEMORY}" --start "${START_TIMESTAMP}" --end "${END_TIMESTAMP}" --step 5s --metric_title memory --iteration_number "${ITERATION_ID}"
```
