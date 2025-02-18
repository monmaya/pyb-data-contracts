# Lifecycle: Beyond Simple YAML

It's midnight, and an alert sounds: a critical data contract has just been modified without following the established process. This situation, unfortunately common, illustrates the crucial importance of understanding and properly managing the lifecycle of data contracts. A data contract isn't a static document - it's a living organism that evolves with your organization and requires rigorous management throughout its existence.

## The Phases of the Lifecycle

The lifecycle of a data contract follows a well-defined path, from its conception to its end of life. This natural progression begins with a design phase where needs are identified and the contract is elaborated. This initial step is crucial as it lays the foundation for everything that follows. The contract then goes through a rigorous validation phase before entering production.

```mermaid
stateDiagram-v2
    [*] --> Design
    Design --> Validation
    Validation --> Production
    Production --> Evolution
    Evolution --> Deprecation
    Deprecation --> [*]

    state Design {
        [*] --> Draft
        Draft --> Review
        Review --> [*]
    }

    state Production {
        [*] --> Active
        Active --> Maintenance
        Maintenance --> [*]
    }

    state Evolution {
        [*] --> MinorChanges
        MinorChanges --> MajorChanges
        MajorChanges --> [*]
    }
```

Once in production, the contract enters a phase of continuous evolution, where it adapts to the organization's changing needs. This evolution must be carefully orchestrated to maintain data consistency and quality. Finally, when the contract is no longer relevant, it enters a deprecation phase that leads to its end of life.

## The Structure of an Evolving Contract

To support this lifecycle, the contract itself must be structured to capture its evolution. Here's how such a contract might be structured:

```yaml
apiVersion: v3.0.0
kind: DataContract
id: urn:datacontract:user:preferences
domain: user-domain
tenant: UserExperience
name: User Preferences
version: 3.0.0
status: active

description:
  purpose: "Manage user preferences and settings"
  usage: "Personalization and user experience optimization"
  limitations: "Personal data subject to GDPR"
  dataGranularityDescription: "One record per user"
  lifecycle:
    currentPhase: "active"
    phases:
      - name: "draft"
        startDate: "2023-09-01"
        endDate: "2023-10-01"
        activities: ["initial design", "stakeholder review"]
      - name: "beta"
        startDate: "2023-10-01"
        endDate: "2023-12-01"
        activities: ["limited production testing", "performance optimization"]
      - name: "active"
        startDate: "2024-01-01"
        activities: ["full production use", "monitoring"]
    deprecationPlan:
      scheduledDate: "2025-01-01"
      migrationPath: "v4.0.0"
      notificationPeriod: "6 months"

schema:
  - name: UserPreference
    physicalName: user_preferences
    physicalType: table
    description: "User preference settings"
    tags: ["user", "preferences", "settings"]
    properties:
      - name: user_id
        logicalType: string
        physicalType: text
        description: "Unique user identifier"
        isNullable: false
        isUnique: true
        criticalDataElement: true
        examples: ["USER-001"]
      - name: theme
        logicalType: string
        physicalType: text
        description: "UI theme preference"
        isNullable: false
        allowedValues: ["light", "dark", "system"]
        addedInVersion: "2.0.0"
        examples: ["dark"]
      - name: notifications
        logicalType: object
        physicalType: json
        description: "Notification preferences"
        isNullable: false
        addedInVersion: "3.0.0"
        schema:
          type: object
          properties:
            email:
              type: boolean
              description: "Email notifications enabled"
            push:
              type: boolean
              description: "Push notifications enabled"
            frequency:
              type: string
              enum: ["real-time", "daily", "weekly"]
        examples: [{"email": true, "push": false, "frequency": "daily"}]

quality:
  - rule: validTheme
    description: "Theme must be one of the allowed values"
    dimension: validity
    severity: error
    businessImpact: operational
  - rule: validNotifications
    description: "Notification preferences must be valid JSON"
    dimension: validity
    severity: error
    businessImpact: operational

team:
  - username: agarcia
    role: Data Product Owner
    dateIn: "2023-09-01"
  - username: lzhang
    role: Data Steward
    dateIn: "2023-09-01"

support:
  - channel: "#user-preferences"
    tool: slack
    url: https://company.slack.com/user-preferences
  - channel: user-prefs@company.com
    tool: email
    url: mailto:user-prefs@company.com

servers:
  - server: prod
    type: postgresql
    format: sql
    url: postgresql://user-prefs.prod.company.com:5432/preferences
    description: "Production preferences database"

slaProperties:
  - property: latency
    value: 1
    unit: s
  - property: retention
    value: 5
    unit: y
  - property: frequency
    value: 1
    unit: s

tags:
  - user
  - preferences
  - settings
  - personalization

customProperties:
  - property: dataDomain
    value: user
  - property: criticality
    value: high
  - property: personalData
    value: true
  - property: gdprRelevant
    value: true
```

## Managing Transitions

The transition phase between contract versions is particularly delicate. It requires careful orchestration to avoid any disruption to production systems. This orchestration begins with a dual-write period, where data is written simultaneously to both the old and new versions of the contract. This approach allows validating the new version while maintaining existing system stability.

```mermaid
sequenceDiagram
    participant Owner as Contract Owner
    participant Registry as Contract Registry
    participant Prod as Production
    participant Consumers as Consumers

    rect rgb(200, 220, 250)
        Note over Owner,Consumers: Phase 1: Preparation
        Owner->>Registry: Publication v2
        Registry->>Consumers: Change notification
    end

    rect rgb(200, 250, 220)
        Note over Owner,Consumers: Phase 2: Dual Writing
        Owner->>Registry: Activation v1 + v2
        Registry->>Prod: Dual writing
        Note over Prod: 14 days validation
    end

    rect rgb(250, 220, 200)
        Note over Owner,Consumers: Phase 3: Progressive Migration
        Registry->>Consumers: 10% traffic v2
        Note over Consumers: 24h validation
        Registry->>Consumers: 50% traffic v2
        Note over Consumers: 48h validation
        Registry->>Consumers: 100% traffic v2
    end

    rect rgb(220, 220, 250)
        Note over Owner,Consumers: Phase 4: Cleanup
        Owner->>Registry: Deactivation v1
        Registry->>Consumers: v1 end notification
    end
```

### Phase 1: Preparation
This phase is crucial as it lays the groundwork for a successful transition:
- The Contract Owner publishes the new version (v2) in the Registry
- Consumers are automatically notified via the subscription system
- Teams can begin studying the changes and planning their migration
- Migration documentation is validated and published

### Phase 2: Dual Writing
This security phase allows validating the new version under real conditions:
- Data is written simultaneously to v1 and v2 versions
- Teams can compare results between both versions
- A 14-day period covers all business cases (month-end, weekends, etc.)
- Anomalies can be detected without production impact

### Phase 3: Progressive Migration
The switch is done in stages to minimize risks:
- 10% of traffic is directed to v2, allowing quick problem detection
- A 24h validation confirms proper functioning at this first stage
- Traffic is increased to 50% if no problems are detected
- After 48 additional hours of validation, the complete switch is made

### Phase 4: Cleanup
This final phase is often neglected but essential:
- V1 is officially deprecated in the Registry
- A final notification is sent to consumers
- V1 resources are cleaned up (storage, monitoring, etc.)
- Documentation is updated to reflect v1's end of life

This methodical approach to transition allows:
- Minimizing operational risks
- Giving visibility to all stakeholders
- Ensuring a controlled and reversible migration
- Maintaining service quality during transition

## Contract End of Life

The end of life of a contract must be managed with as much care as its creation. This phase begins with a deprecation period where consumers are progressively migrated to alternatives. Once all consumers are migrated, the contract can be archived, but its metadata and history must be preserved to maintain traceability and regulatory compliance.

## Conclusion

Managing the lifecycle of data contracts is a fundamental aspect of any data governance strategy. It requires a systematic approach and constant attention to the needs of data producers and consumers. Good lifecycle management not only ensures data quality and reliability but also facilitates system evolution while maintaining user trust.

In the next article, we'll explore how these lifecycle management practices integrate into a broader data governance strategy, and how they contribute to creating a mature data culture within the organization.