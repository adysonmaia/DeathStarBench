FROM adysonmaia/wrk2:latest 
WORKDIR /workspace
COPY scripts/ scripts/
ENTRYPOINT wrk -L -D exp -t 1 -c 1 -d "${DURATION:-600}" -R "${RATE:-10}" -s ./scripts/hotel-reservation/mixed-workload_type_1.lua "http://${FRONTEND_ADDR}" 2>&1
