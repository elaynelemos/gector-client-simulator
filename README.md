# gector-client-simulator

```bash
QUERY_MEMORY='(1 - ((avg_over_time(node_memory_MemFree_bytes{job="local_node"}[30s]) + avg_over_time(node_memory_Cached_bytes{ job="local_node"}[30s]) + avg_over_time( node_memory_Buffers_bytes{job="local_node"}[30s])) / avg_over_time(node_memory_MemTotal_bytes{job="local_node"} [30s])))'

QUERY_CPU='(avg without (mode,cpu) (1 - rate(node_cpu_seconds_total{mode="idle", job="local_node"}[30s])))'

python3 prometheus_data.py --url "http://${PROMETHEUS_IP}:9090" --query "${QUERY_MEMORY}" --start "${START_TIMESTAMP}" --end "${END_TIMESTAMP}" --step 5s --metric_title memory --iteration_number "${ITERATION_ID}"
```
