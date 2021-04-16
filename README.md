# Kafka_Fraud_Detector

Fraud Detection System With Kafka And Python.

Prerequisites:

 1) A Kafka broker.
 2) A Zookeeper instance.
 3) A Python instance.

Introduction:

A simple fraud detection mechanism which produces fake transactions on one end, and filters and logs those that look suspicious on the other end.
This will involve a transaction generator and a fraud detector. 

![image](https://user-images.githubusercontent.com/74184047/115011402-4217ec80-9eb7-11eb-8cec-d2fcecafa9cb.png)


Technologies:

Flask --> is a micro-framework used by python developers.

Apache Kafka --> is a streaming data platform that works by ingesting, transforming and distributing data on the fly.

Zookeeper --> is a coordination software, distributed as well, used by Apache Kafka to keep track of the cluster state and members. 

SSE --> Server-Sent Events is a mechanism for sending updates from a server to a client.

Requirements.txt

1) Flask 1.1.2

2) Jinja2 2.11.2

3) Kafka-python 2.0.2

