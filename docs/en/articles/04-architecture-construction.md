# Building a Data Contract: From Design to Deployment

When discussing data contracts, we often focus on their role in production: how they regulate data exchanges, integrate into the information system, and ensure pipeline reliability. Their impact also plays out upstream, from their initial design. However, I've observed that this decisive phase often remains in the shadows. It's a bit like admiring a building for its architecture without ever discussing the construction site that gave birth to it. Yet it's during construction that decisions are made that ensure the solidity and longevity of the whole.

In this article, I invite you to explore the backstage of data contract creation within a multidisciplinary team. Discover the architecture, product, and engineering methods that transform a simple idea into a robust contract, from conception to first deployment.

## The Collaborative Product Approach to Contracts

At the heart of data contract construction lies a product approach.

- Who are the users of my product and what are their needs (user-centered)?
- What needs do I want to address (vision) for what benefits (impact)?
- How can I test and collect improvement perspectives (feedback)?
- How do they ensure effective collaboration between different stakeholders (interoperability)?
- Are they designed to evolve and adapt to future needs (scalability)?

```mermaid
graph TD
    subgraph "Product Approach to Contract Design"
        P[Producers] -->|Propose| A[Contract Workshop]
        C[Consumers] -->|Require| A
        A -->|Produces| D[Contract Draft]
        D -->|Review| R[Review Process]
        R -->|Feedback| D
        R -->|Approves| F[Final Contract]
        G[Domain Experts] -->|Validate| R
        H[Data Governance] -->|Supervises| R
    end

    classDef producer fill:#e6ffe6;
    classDef consumer fill:#e6f3ff;
    classDef governance fill:#ffe6e6;
    class P producer;
    class C consumer;
    class H governance;
```

In the context of contracts, this approach relies particularly on five principles:

1. **Multidisciplinary Participation**  
   An effective data contract requires the active participation of several complementary profiles:
   - **Data producers** bring their knowledge of source systems, technical constraints, and extraction possibilities
   - **End users** express their needs, use cases, and quality requirements
   - **Business experts** ensure the contract accurately reflects business reality and domain semantics
   - **Data governance** ensures alignment with company policies, security, and regulatory compliance

The contract addresses everyone, meaning all these profiles as **data consumers** in their daily work. The sum of contracts becomes a scalable way to enable the discovery of the data assets.

Forgetting any of these profiles leads to unbalanced contracts, either too technical and disconnected from real needs, or unrealistic in terms of implementation.

2. **Rapid Iteration**  
   Unlike the "big design upfront" approach, the product approach favors short, iterative cycles. For contracts, this translates in two ways.
   The first, traditionally:
   - Start with a minimalist version of the contract that meets essential needs
   - Gather feedback quickly before committing to costly developments
   - Adjust and enrich the contract progressively
   - Validate each iteration with stakeholders
  The second, cross-cutting and strategic:
   - Identify the data maturity of actors who will be your early adopters, choosing only those for whom implementation doesn't represent a high cost
   - Determine if you want to test the impact across the entire value chain (for example, if your data quality issues are a major concern) or in a particular area (for example, if you have significant functional and technical debt, and need to highlight the quality of one data product compared to others)
   
   This approach significantly reduces the risk of spending weeks designing a contract that ultimately proves unsuitable. Provided users are available for feedback, iterations of 1 to 2 weeks maximum are preferable, with frequent synchronization points.

3. **Contextual Documentation**  
   Beyond the data structure, the contract must capture the "why" behind each decision:
   - Document the alternatives considered and the reasons for choices made
   - Explain accepted trade-offs (for example between performance and completeness)
   - Record key discussions that led to decisions
   - Reference business or technical constraints that influenced the design
   
   This contextual documentation proves invaluable when new members join the team or when the contract needs to be revisited months later. It transforms the contract from a simple technical document into a shared knowledge repository.

4. **Test-Driven Validation**  
   The contract is not just a description - it's a promise that must be verifiable:
   - Define tests that validate compliance with the contract even before its implementation
   - Make sure to formulate these tests functionally to allow all users to understand what is being tested
   - Create example datasets that illustrate typical and extreme use cases
   - Automate verification to enable continuous integration
   - Include negative tests that clearly demonstrate what is not acceptable
   
   This approach, inspired by TDD (Test-Driven Development), helps clarify expectations and avoid misinterpretations. Tests become the executable definition of the contract, complementary to its formal description.

5. **Domain-Driven Approach**  
   The contract must speak the language of the business, not that of underlying systems:
   - Use business domain terminology, not technical jargon (this is all too often the case, resulting in contracts that are not readable by non-technical people)
   - Structure data according to the business vision, even if it requires transformation from source systems (and this is a real issue, as sources will often refuse to adapt to the business vision)
   - Include business rules and constraints that give meaning to the data
   - Only reveal the specifics of underlying technical systems if it adds value to the user (for example, if it helps clarify operational complexity)
   
   This approach, inspired by Domain-Driven Design, ensures that the contract remains relevant even if underlying technologies evolve. It creates a common language between technical and business teams, significantly reducing misunderstandings.

### The Process Supporting the Product Approach to Contracts

The typical process includes the following steps:

1. **Needs Discovery**: Collaborative session where producers and consumers define their needs
2. **Strategy Development**: Assessment of maturity, choice of actors and approach
3. **Draft Creation**: Development of a first version of the contract
4. **Refinement**: Verification of technical feasibility and consistency, validation by domain experts, verification of compliance with standards and policies
5. **Finalization**: Consolidation of feedback and final validation
6. **Success Indicators**: Design of indicators to evaluate the success of this iteration
7. **Feedback Loop**: Collection of user feedback

One of the key advantages of this method is that it allows early identification of incompatibilities and implementation challenges, thereby reducing later correction costs.

## Practical Guide: Creating a Data Contract from A to Z

Now that the framework is established, let's see concretely how to create a data contract, step by step, from its conception to its deployment. I'll guide you through the complete process with an example that you can adapt to your context.

### Step 1: Initialize Your First Data Contract

Let's start by creating a simple contract. Here's how to proceed:

1. **Create a dedicated repository** in your version control system (GitHub, GitLab, etc.)

2. **Initialize a data contract file** at the root, for example `customer_profile.datacontract.yaml`:

```yaml
# customer_profile.datacontract.yaml
dataContractSpecification: 0.9.2
id: customer_profile
info:
  title: Customer Profile
  version: 0.1.0
  description: >
    Data contract for customer profiles,
    used by the marketing team for behavioral analysis.
  owner: customer-data-team
  contact:
    name: Customer Data Team
    url: https://wiki.example.com/data-team
    email: data-team@example.com
```

3. **Add stakeholder information**:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
contractedService:
  provider:
    name: CRM System
    team: CRM Team
    contact: alice@example.com
  consumer:
    - name: Marketing Application
      team: Marketing Team
      contact: bob@example.com
    - name: Analytics Dashboard
      team: Data Team
      contact: charlie@example.com
  termsOfService: https://wiki.example.com/terms-of-service
```

4. **Commit these initial elements** to your repository with a clear message:

```bash
git add customer_profile.datacontract.yaml
git commit -m "Initial: creation of customer profile data contract"
git push
```

### Step 2: Define the Data Structure

Now, let's add the data structure to the contract. This is the step where you concretely define what will be exchanged:

1. **Add the models section** that describes the data structure:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
models:
  Customer:
    description: Customer information
    type: object
    required:
      - customer_id
      - first_name
      - last_name
      - email
    properties:
      customer_id:
        type: string
        description: Unique customer identifier
        pattern: "^CUS[0-9]{6}$"
        example: "CUS123456"
      
      first_name:
        type: string
        description: Customer's first name
        maxLength: 50
        example: "Marie"
      
      last_name:
        type: string
        description: Customer's last name
        maxLength: 50
        example: "Dupont"
      
      email:
        type: string
        format: email
        description: Customer's email address
        example: "marie.dupont@example.com"
      
      phone:
        type: string
        description: Phone number (international format)
        pattern: "^\\+[0-9]{1,3} [0-9 ]{5,15}$"
        example: "+33 6 12 34 56 78"
```

2. **Define data access interfaces**:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
interfaces:
  customerProfile:
    description: Interface to access customer profiles
    serving:
      server: https://api.example.com
      security:
        - type: oauth2
          description: OAuth2 authentication required
      endpoints:
        getCustomerProfile:
          path: /customers/{customerId}
          method: GET
          description: Retrieve a specific customer's profile
          parameters:
            - name: customerId
              in: path
              required: true
              schema:
                type: string
                pattern: "^CUS[0-9]{6}$"
              description: Unique customer identifier
          response:
            type: object
            $ref: "#/models/Customer"
```

3. **Add important business rules** that are not captured by the schema:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
quality:
  rules:
    - name: email_verification
      description: The email address must be verified before being included in the contract
      rationale: Avoid propagation of invalid addresses in systems
    
    - name: minor_identification
      description: Minor clients (-18 years) must be identified with a specific flag
      rationale: Specific GDPR legal obligations for minors
```

4. **Commit these additions** with a descriptive message:

```bash
git commit -am "Add: customer profile data structure"
```

### Step 3: Define Examples and Tests

Examples and tests are essential to clarify the contract's usage:

1. **Add complete examples**:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
examples:
  - name: standard_client
    description: Example of a standard client with all information
    interface: customerProfile
    endpoint: getCustomerProfile
    parameters:
      customerId: "CUS123456"
    response:
      customer_id: "CUS123456"
      first_name: "Marie"
      last_name: "Dupont"
      email: "marie.dupont@example.com"
      phone: "+33 6 12 34 56 78"
      
  - name: minimal_client
    description: Example with only mandatory fields
    interface: customerProfile
    endpoint: getCustomerProfile
    parameters:
      customerId: "CUS654321"
    response:
      customer_id: "CUS654321"
      first_name: "Jean"
      last_name: "Martin"
      email: "jean.martin@example.com"
```

2. **Configure quality and test aspects**:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
quality:
  tests:
    - name: validation_client_id
      description: Verify that the client ID meets the expected format
      test:
        interface: customerProfile
        endpoint: getCustomerProfile
        parameters:
          customerId: "CUS123456"
        assertions:
          - jsonPath: "$.customer_id"
            expected: "CUS123456"
    
    - name: validation_email_format
      description: Verify that the email is in the correct format
      test:
        interface: customerProfile
        endpoint: getCustomerProfile
        parameters:
          customerId: "CUS123456"
        assertions:
          - jsonPath: "$.email"
            matchesRegex: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
```

3. **Commit these additions**:

```bash
git commit -am "Add: examples and validation tests"
```

### Step 4: Document Technical Aspects

To facilitate adoption, document implementation aspects:

1. **Specify access and SLA details**:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
slo:
  availability:
    description: Availability of the Customer Profile API
    target: 99.9%
    period: 30d
    
  latency:
    description: Response time for API requests
    target: 200ms
    period: 30d
    percentile: 95
    
  errorRate:
    description: Maximum error rate 
    target: 0.1%
    period: 30d
```

2. **Document error codes**:

```yaml
# Continuation of the customer_profile.datacontract.yaml file
interfaces:
  customerProfile:
    # ... [existing content] ...
    errors:
      - status: 404
        description: Client not found
        resolution: "Check client identifier"
        
      - status: 403
        description: Unauthorized access
        resolution: "Check access rights and authentication"
```

3. **Commit these technical details**:

```bash
git commit -am "Add: technical details and SLA"
```

### Step 5: Establish Versioning Strategy

The ODCS standard integrates versioning into its metadata. Complete the `info` section:

```yaml
# Update of the info section
info:
  title: Customer Profile
  version: 0.1.0
  description: >
    Data contract for customer profiles,
    used by the marketing team for behavioral analysis.
  versioningPolicy:
    compatibleChanges:
      - "Addition of optional fields"
      - "Enumeration extension"
      - "Constraint relaxation"
    breakingChanges:
      - "Field removal"
      - "Field renaming"
      - "Data type modification"
      - "Addition of mandatory fields"
  deprecationPolicy:
    deprecationNotice: "3 months"
    supportPeriod: "6 months after deprecation"
```

### Step 6: Validate Data and Publish Your Contract

This crucial step ensures that your contract is both technically correct and usable by various stakeholders.

#### 6.1 The datacontract-cli Tool

To work efficiently with data contracts, the reference tool is `datacontract-cli`. It's an open-source command-line tool that offers numerous features to validate, test, generate, and publish your data contracts. You now even have an API at https://cli.datacontract.com/API.

Let's start by installing it:

```bash
# Installation via pip
pip install 'datacontract-cli[all]'

# Verify installation
datacontract --version
```

Here are the main available commands:

| Command | Description | Usage Example |
|----------|-------------|----------------------|
| `init` | Creates a new data contract from a template | `datacontract init datacontract.yaml` |
| `lint` | Validates the syntax and structure of the data contract | `datacontract lint datacontract.yaml` |
| `test` | Runs schema and quality tests on configured servers | `datacontract test --server production datacontract.yaml` |
| `export` | Converts the data contract to different formats (SQL, HTML, JSON Schema, etc.) | `datacontract export --format html --output doc.html datacontract.yaml` |
| `import` | Creates a data contract from an existing source (SQL, Avro, etc.) | `datacontract import --format sql --source schema.sql --dialect postgres` |
| `diff` | Displays differences between two versions of data contracts | `datacontract diff v1.yaml v2.yaml` |
| `breaking` | Identifies breaking changes | `datacontract breaking v1.yaml v2.yaml` |
| `changelog` | Generates a changelog between two versions | `datacontract changelog v1.yaml v2.yaml` |
| `publish` | Publishes the data contract to a registry | `datacontract publish datacontract.yaml --registry https://registry.example.com` |
| `catalog` | Creates an HTML catalog of data contracts | `datacontract catalog --files "*.yaml" --output "./catalog"` |
| `api` | Starts a web server with a REST API to interact with datacontract-cli | `datacontract api --port 4242` |

#### 6.2 Using GitHub Actions for Validation and Publication

GitHub Actions offers an accessible solution to automate the lifecycle of your data contracts. Create a `.github/workflows/validate-datacontract.yml` file in your repository:

```yaml
name: Validate Data Contract

on:
  push:
    paths:
      - '*.datacontract.yaml'
  pull_request:
    paths:
      - '*.datacontract.yaml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install datacontract-cli
      - name: Validate contract
        run: datacontract lint *.datacontract.yaml
      - name: Run tests
        run: datacontract test *.datacontract.yaml
      
  publish:
    needs: validate
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install datacontract-cli
      - name: Publish contract
        run: |
          datacontract publish *.datacontract.yaml \
            --registry ${{ secrets.REGISTRY_URL }} \
            --token ${{ secrets.REGISTRY_TOKEN }}
```

This GitHub Actions configuration automates:
- Syntax validation of the contract with each modification
- Execution of tests defined in the contract
- Publication of the contract to a central registry after validation

#### 6.3 Develop Validation Tools for Your Consumers

Provide your consumers with tools that allow them to easily validate data against your contract:

```python
# validation_lib.py - to be shared with your teams
import json
import jsonschema
import requests
import subprocess

def extract_schema(contract_path, model_name):
    """Extracts the JSON schema of a model from an ODCS contract"""
    result = subprocess.run(
        ["datacontract", "schema-extract", contract_path, "--model", model_name],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

def validate_data(data, schema):
    """Validates data against a schema"""
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, None
    except jsonschema.exceptions.ValidationError as e:
        return False, str(e)

def fetch_and_validate(api_url, contract_path, model_name, auth_token=None):
    """Fetches data from an API and validates it"""
    headers = {"Authorization": f"Bearer {auth_token}"} if auth_token else {}
    response = requests.get(api_url, headers=headers)
    data = response.json()
    schema = extract_schema(contract_path, model_name)
    return validate_data(data, schema)
```

#### 6.4 Prepare Your Contract for Publication

Before officially publishing your contract, ensure that:
- All validation errors have been corrected (`datacontract lint`)
- Tests pass successfully (`datacontract test`)
- Examples are correct and functional
- Documentation is complete and clear

Then, publish your contract with explicit versioning:

```bash
# Create a Git tag for the version
git tag -a v0.1.0 -m "First version of the customer profile contract"
git push --tags

# Publish to your contract registry
datacontract publish customer_profile.datacontract.yaml \
  --registry https://registry.example.com \
  --token $REGISTRY_TOKEN
```


### Step 7: Drive Adoption

To maximize data contract adoption, focus on these key actions:

1. **Indicators**, indicators, indicators: a product team ensures the collection of quantitative and qualitative feedback
2. **Practical documentation** - Create a clear usage guide with concrete examples:
   ```markdown
   # Customer Profile Contract Usage Guide
   
   ## API Access
   Request your credentials from the CRM team via the self-service portal.
   
   ## Example Request
   curl -X GET "https://api.example.com/customers/CUS123456" -H "Authorization: Bearer TOKEN"
   ```

3. **Developer resources** - Provide code samples in languages used by your teams

4. **Support channels** - Set up a dedicated Slack channel and regular office hours

5. **Feedback loop** - Implement simple metrics to track usage and gather improvement ideas

6. **Knowledge sharing** - Run focused workshops and create demo videos

By keeping support practical and targeted, you'll transform your data contract from simple documentation into an integral part of your data operations.


## The Contract Registry: An Essential Element

A contract registry is a fundamental component of your data infrastructure. It is not just a "nice to have" but an **essential element** for industrializing and governing your data contracts.

### Why a Registry is Indispensable

The contract registry fulfills several critical functions:

1. **Single Source of Truth**: It centralizes all your contracts in an official location
2. **Discoverability**: It allows teams to easily find available contracts
3. **Governance**: It facilitates the application of policies and standards
4. **Traceability**: It keeps the history of changes and versions
5. **Automation**: It integrates into your pipelines for validation and artifact generation

Without a registry, you will quickly find yourself with scattered contracts, contradictory versions, and general confusion about what is official.

### The Logical Progression: From GitHub Actions to Centralized Registry

1. **Beginner Level: GitHub Actions + Git**
   - Use GitHub Actions to validate and publish contracts
   - Store contracts in Git repositories
   - **Advantages**: Easy to set up, no additional infrastructure
   - **Limitations**: Contract dispersion, lack of overview, manual governance

2. **Intermediate Level: GitHub Actions + Central Registry**
   - Continue using GitHub Actions for CI/CD
   - Systematically publish validated contracts to a central registry
   - **Advantages**: Centralized view while preserving existing workflows
   - **Configuration Example**:
   ```yaml
   # Publication to a central registry from GitHub Actions
   - name: Publish to central registry
     run: |
       datacontract publish *.datacontract.yaml \
         --registry https://registry.example.com \
         --metadata '{"source_repo": "${{ github.repository }}", "commit": "${{ github.sha }}"}'
   ```

3. **Advanced Level: Integrated Contract Management Platform**
   - Use a specialized platform that manages the entire lifecycle
   - Integrate validation, publication, visualization, and governance
   - **Advantages**: Optimized workflow, less friction, better adoption
   - **Key Features**: Advanced search, contract dependencies, impact alerts, usage metrics

### Types of Registries: Choosing the solution adapted to your maturity

Choosing a contract registry is not a trivial decision and must correspond to your organization's maturity regarding data contracts. A solution that's too complex risks being underutilized, while an approach that's too basic could quickly show its limitations when facing a growing number of contracts. Honestly evaluate your current maturity level and anticipate your medium-term needs before choosing among these options:

1. **Basic Solution**: A dedicated Git repository with a documented structure
   - **Advantages**: Easy to set up, integrated versioning
   - **Limitations**: Limited search capabilities, no user-friendly interface

2. **Intermediate Solution**: Enterprise wiki or documentation portal
   - **Advantages**: Better UX, integration with your existing ecosystem
   - **Limitations**: Lack of contract-specific features

3. **Advanced Solution**: Specialized tool (DataHub, Amundsen, ODCS registry)
   - **Advantages**: Rich features, automated integration, advanced governance
   - **Limitations**: Greater installation and maintenance effort

### Essential Features of a Good Contract Registry

Regardless of the solution chosen, certain features are crucial to ensure the long-term effectiveness of your registry. These capabilities constitute the minimal foundation that you should require or plan to develop progressively:

1. **Search and Discovery Interface**:
   - Search by metadata (owner, domain, version)
   - Visualization of contract relationships
   - Usage and health statistics

2. **Version and Compatibility Management**:
   - Automatic detection of breaking changes
   - Alert consumers in case of major updates
   - Retain complete change history

3. **Integration with Your Ecosystem**:
   - API for automation and integration
   - Hooks for notifications and workflow execution
   - Automatic artifact generation (documentation, client code)

Ultimately, the contract registry you choose should evolve with your organization. Perhaps start with a simple solution, but keep in mind that investing in a robust registry will pay considerable dividends in terms of team productivity and quality of exchanged data. The time saved in searching for contracts, resolving misunderstandings, and reconciling divergent versions will amply justify the initial effort.

## Conclusion

Building a data contract is an iterative process that relies on collaboration and gradual evolution. By following this structured approach, you will create contracts that are both relevant to the business and technically sound.

The journey we have taken together, from collaborative design to technical validation, through versioning and documentation, illustrates the richness of this approach. The importance of the contract registry, as the cornerstone of your infrastructure, should not be underestimated.

Remember that the contract itself is just a means and not an end - its goal is to facilitate mutual understanding and ensure the quality of data exchanges. The true success of a data contract is measured by its ability to improve collaboration between teams and ensure the integrity of data flowing through your organization. 