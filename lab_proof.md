# HomeGuard Security System - Lab Proof

## Project Overview
Welcome to the HomeGuard Security System lab!
The system simulates sensors, processes readings, detects abnormal conditions,
generates alerts, and logs security events.

The project demonstrates:

- Python data structures (dictionaries)
- Conditional logic (if/else)
- Functions
- Object-oriented programming (Sensor class)
- Simulation loops
- Testing different security modes


---

## System Requirements
The simulator must handle these scenarios:

Security Alerts:

Motion detected when house is in "away" mode
Door opened when house is in "away" mode
Multiple sensors triggered simultaneously (possible break-in)

Safety Alerts:
Temperature below 35°F (frozen pipe risk)
Temperature above 95°F (equipment failure)
Smoke detected (fire risk)

Comfort Notifications:
Temperature outside comfort range (65-75°F) when home is in "home" mode
Unusual patterns (like a door left open for >5 minutes)

