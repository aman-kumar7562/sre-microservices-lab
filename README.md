SRE Microservices Lab
Objective

This repository documents my journey transitioning from an operational Incident Commander role to an Engineering-focused SRE / Observability Architect mindset.

The goal of this lab is to understand how distributed services behave under load, failure, and scaling scenarios — not just how to monitor them.

Phase 1 – Service Fundamentals
What I Built

A simple Flask-based HTTP service

Containerized using Docker

Exposed multiple endpoints:

/ → normal response

/slow → simulated latency

/health → health check endpoint

Why This Matters

This setup allows simulation of:

Response time differences

Service degradation

Single instance failure

Single Point of Failure scenarios

It provides a controlled environment to reason about reliability fundamentals before introducing monitoring systems.

What I Learned
Architecture Concepts

Container ≠ Microservice (packaging vs architectural role)

Single Point of Failure (SPOF)

Horizontal scaling principles

Why load balancers are required

Degradation vs full outage

Reliability Signals (Golden Signals)

Latency

Throughput

Error Rate

Understanding how these signals change under load or dependency failure is critical for SRE work.

Next Steps

Add additional service to simulate inter-service communication

Introduce scaling with multiple replicas

Integrate Prometheus for telemetry collection

Define SLO and alerting strategy

Simulate failure scenarios
