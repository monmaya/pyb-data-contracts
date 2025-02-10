# Practical Implementation of Data Contracts

While data contract theory is appealing, their practical implementation raises numerous technical and organizational challenges. In this article, I share my concrete implementation experience, with code examples and proven implementation patterns.

## Infrastructure and Tooling

### Contract Registry

The core of our implementation relies on a centralized registry of data contracts. Here's an example structure:

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

@dataclass
class DataContract:
    name: str
    version: str
    owner: str
    schema: Dict
    quality_rules: List[Dict]
    sla: Dict
    created_at: datetime
    updated_at: datetime
    status: str  # draft, active, deprecated
    
class ContractRegistry:
    def register_contract(self, contract: DataContract) -> str:
        """Registers a new contract or a new version"""
        validation_result = self.validate_contract(contract)
        if not validation_result.is_valid:
            raise ValidationError(validation_result.errors)
            
        contract_id = self.store_contract(contract)
        self.notify_stakeholders(contract)
        return contract_id
        
    def get_contract(self, name: str, version: Optional[str] = None) -> DataContract:
        """Retrieves the latest version or a specific version of a contract"""
        return self.load_contract(name, version)
```

### Validation Pipeline

Contract validation is automated via a CI/CD pipeline:

```yaml
# .github/workflows/validate-contracts.yml
name: Validate Data Contracts

on:
  pull_request:
    paths:
      - 'contracts/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
          
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          
      - name: Validate contracts
        run: |
          python -m pytest validation/contract_tests.py
          
      - name: Check backward compatibility
        run: |
          python scripts/check_compatibility.py
```

## Implementation Examples

### REST API Contract

For REST APIs, we use a combination of OpenAPI and data contracts:

```yaml
# contracts/api/customer_api.yaml
openapi: 3.0.0
info:
  title: Customer API
  version: 2.0.0
paths:
  /customers/{customer_id}/profile:
    get:
      parameters:
        - name: customer_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Customer profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomerProfile'
components:
  schemas:
    CustomerProfile:
      $ref: '../customer-domain/customer_profile_events.yaml#/schema'
```

### Event Schema Contract

For events, we use Apache Avro with contract metadata:

```json
{
  "type": "record",
  "name": "CustomerEvent",
  "namespace": "com.example.events",
  "doc": "Customer event schema with contract metadata",
  "fields": [
    {"name": "event_id", "type": "string"},
    {"name": "customer_id", "type": "string"},
    {"name": "event_type", "type": "string"},
    {"name": "timestamp", "type": "long"},
    {"name": "data", "type": "bytes"},
    {"name": "contract_version", "type": "string"},
    {"name": "schema_version", "type": "string"}
  ],
  "contract": {
    "owner": "customer-team",
    "sla": {
      "latency": "5m",
      "availability": 99.9
    }
  }
}
```

### Tests and Validation

Our testing framework combines multiple levels of validation:

```python
import pytest
from pydantic import BaseModel, validator
from typing import List, Dict

class ContractValidator:
    def test_schema_compatibility(self):
        """Checks compatibility with previous versions"""
        old_schema = self.load_previous_version()
        compatibility_issues = self.check_compatibility(
            old_schema, 
            self.current_schema
        )
        assert not compatibility_issues
        
    def test_quality_rules(self):
        """Validates quality rules"""
        test_data = self.generate_test_data()
        validation_results = self.apply_quality_rules(test_data)
        assert all(result.is_valid for result in validation_results)
        
    def test_performance(self):
        """Verifies processing performance"""
        with self.measure_processing_time() as metrics:
            self.process_test_batch()
        assert metrics.p95_latency < self.sla_target
```

## Monitoring and Observability

Monitoring contracts in production is crucial:

```python
from datadog import initialize, statsd

class ContractMonitoring:
    def track_usage(self, contract_name: str, version: str):
        """Tracks usage of different versions"""
        statsd.increment(
            'data_contract.usage',
            tags=[f'contract:{contract_name}', f'version:{version}']
        )
        
    def track_quality(self, validation_result):
        """Measures data quality"""
        statsd.gauge(
            'data_contract.quality',
            validation_result.score,
            tags=[
                f'contract:{validation_result.contract}',
                f'rule:{validation_result.rule}'
            ]
        )
        
    def track_sla_compliance(self, latency_ms: float):
        """Checks SLA compliance"""
        statsd.histogram(
            'data_contract.latency',
            latency_ms
        )
```

## Best Practices and Lessons Learned

1. **Maximum Automation**
   - Automate contract validation
   - Integrate tests into your CI/CD
   - Automate documentation generation

2. **Proactive Monitoring**
   - Monitor contract usage
   - Measure data quality
   - Alert on SLA violations

3. **Change Management**
   - Establish a clear review process
   - Communicate changes in advance
   - Maintain a transition period

4. **Living Documentation**
   - Generate documentation from contracts
   - Include practical examples
   - Maintain a detailed changelog

## Conclusion

Successful implementation of data contracts requires a combination of technical tools and organizational processes. Investment in good infrastructure and solid practices quickly pays off in terms of data quality and team productivity.

In the next article, we will explore governance aspects and organization-wide adoption of data contracts.

## Reference Implementation

The implementation code is available in:

- [Scripts](../../../scripts/generate_sample_data.py) - Data generation
- [Validation](../../../validation/contract_tests.py) - Testing framework
- [Contracts API](../../../contracts/api/customer_api.yaml) - REST API example
- [Monitoring](../../../sql/monitoring/version_monitoring.sql) - Observability

## Associated Services

Implementing a data contract requires several services:

```python
class ContractEcosystem:
    def __init__(self):
        self.quality_service = QualityService()
        self.schema_registry = SchemaRegistry()
        self.monitoring = MonitoringService()
        
    def deploy_contract(self, contract_def):
        """Complete deployment with associated services"""
        contract = self.validate_and_register(contract_def)
        self.setup_quality_monitoring(contract)
        self.configure_schema_validation(contract)
        return contract
```