# SRE Microservices Lab

## 🎯 Objective

This repository documents my transition from an operational Incident Commander role to an engineering-focused **SRE / Observability Architect** mindset.

The goal of this lab is to understand how distributed services behave under load, failure, and scaling — not just how to monitor them.

---

## 🚀 Phase 1 – Service Fundamentals

### 🔧 What I Built

- A simple Flask-based HTTP service
- Containerized using Docker
- Exposed multiple endpoints:
  - `/` → Normal response
  - `/slow` → Simulated latency
  - `/health` → Health check endpoint

---

## 🧠 Why This Matters

This setup allows simulation of:

- Response time differences (Latency)
- Service degradation
- Single instance failure
- Single Point of Failure (SPOF)

It provides a controlled environment to reason about reliability fundamentals before introducing monitoring systems.

---

## 📊 Reliability Concepts Practiced

### Golden Signals

- **Latency**
- **Throughput**
- **Error Rate**

Understanding how these signals change under load or dependency failure is core SRE knowledge.

---

## 🏗 Architectural Thinking Developed

- Container ≠ Microservice (packaging vs architectural role)
- Horizontal scaling principles
- Need for load balancing
- Degradation vs full outage
- Dependency impact on availability

---

## 🔜 Next Steps

- Add a second service (inter-service communication)
- Introduce scaling with multiple replicas
- Integrate Prometheus for telemetry collection
- Define SLO and alerting strategy
- Simulate failure scenarios
