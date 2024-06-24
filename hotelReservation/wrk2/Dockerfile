FROM adysonmaia/wrk2:latest 
WORKDIR /workspace
COPY scripts/ scripts/
ENTRYPOINT wrk -D exp -t 4 -c 4 -d "${DURATION:-600}" -s ./scripts/hotel-reservation/mixed-workload_type_1.lua "http://${FRONTEND_ADDR}" -R "${RATE:-10}" 2>&1
