#!/bin/bash

TODAY=$(date +%F)

ps aux > "process_log_$TODAY.log"

echo "Checking for processes using more than 30% memory..."
HIGH_MEM=$(ps aux --sort=-%mem | awk '$4 > 30')

if [ ! -z "$HIGH_MEM" ]; then
  echo "⚠️ Warning: High memory usage detected!"
  echo "$HIGH_MEM" >> high_mem_processes.log
fi

ROOT_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ "$ROOT_USAGE" -gt 80 ]; then
  echo "⚠️ Warning: Root partition usage is above 80% ($ROOT_USAGE%)"
fi

TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM" | wc -l)

echo "✅ Summary:"
echo "Total running processes: $TOTAL_PROCESSES"
echo "Processes using >30% memory: $HIGH_MEM_COUNT"
echo "Disk usage on / : $ROOT_USAGE%"
