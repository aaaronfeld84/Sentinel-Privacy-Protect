# Sentinel Privacy Protect — Internal API Specification

## 1. Permission Firewall API

### POST /permission/request
Input:
- app_id
- permission_type

Output:
- allow | deny | temp_allow

### GET /permission/logs
Output:
- encrypted log entries

## 2. Network Interception API

### POST /network/inspect
Input:
- domain
- headers
- payload_hash

Output:
- allow | block | warn
- risk_score

## 3. Synthetic Identity API

### GET /identity/current
Output:
- device_profile

### POST /identity/rotate
Output:
- new_profile

## 4. ML Anomaly Engine API

### POST /ml/analyze
Input:
- event_type
- metadata

Output:
- anomaly_score
- classification
