MonMaya fork of Pierre-Yves Bonnefoy's data contract repository
===============================================================

# Table of Content (ToC)


# Overview
[This project](https://github.com/monmaya/pyb-data-contracts) is a fork
of Pierre-Yves Bonnefoy's repository, itself featuring a complete set of
training material to learn about data contracts.

The sample data sets and data contracts may be re-used for the
[MonMaya's data-object-related catalog open service](https://github.com/monmaya/specifications).

See also the reference implementation for that catalog service:
https://github.com/monmaya/base-impl

Even though the members of the GitHub organization may be employed by some
companies,
they speak on their personal behalf and do not represent these companies.

# References

## Other MonMaya repositories
* [MonMaya - Data-object-related catalog open service - Specifications](https://github.com/monmaya/specifications)
* [MonMaya - Data-object-related catalog open service - Reference implementation](https://github.com/monmaya/base-impl)

## Cheat sheets
* [Knowledge Sharing - Cheat sheets - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/README.md)
* [Knowledge Sharing - Cheat sheets - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md)
* [Knowledge Sharing - Cheat sheets - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md)
* [Knowledge Sharing - Cheat sheets - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Knowledge Sharing - Cheat sheets - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* [Knowledge Sharing - Cheat sheets - Unity Catalog](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md)
* [Knowledge Sharing - Cheat sheets - Docker](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/docker/README.md)
* [Knowledge Sharing - Cheat sheets - MinIO](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)

## Data products
* Linux Foundation's Open Data Product Specification (ODPS):
  https://opendataproducts.org/
* Innoq's specification for Data Products:
  https://dataproduct-specification.com/
* Open Data Mesh (ODM)'s Data Product Descriptor Specification (DPDS):
  https://github.com/opendatamesh-initiative/odm-specification-dpdescriptor

## Data contracts
* Open Data Contract Specification (ODCS)
  * Reader-friendly, dedicated site:
  https://bitol-io.github.io/open-data-contract-standard/latest/
  * GitHub home page: https://github.com/bitol-io/open-data-contract-standard
* Innoq's Data Contract specification: https://datacontract.com/

## Repositories of Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Cheat sheets](https://github.com/data-engineering-helpers/cheat-sheets)
* [Data Engineering Helpers - Knowledge Sharing - Data products](https://github.com/data-engineering-helpers/data-products)
* [Data Engineering Helpers - Knowledge Sharing - Data contracts](https://github.com/data-engineering-helpers/data-contracts)
* [Data Engineering Helpers - Knowledge Sharing - Data quality](https://github.com/data-engineering-helpers/data-quality)
* [Data Engineering Helpers - Knowledge Sharing - Semantic layer](https://github.com/data-engineering-helpers/semantic-layer)
* [Data Engineering Helpers - Knowledge Sharing - Architecture principles](https://github.com/data-engineering-helpers/architecture-principles)
* [Data Engineering Helpers - Knowledge Sharing - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle)
* [Data Engineering Helpers - Knowledge Sharing - Data management](https://github.com/data-engineering-helpers/data-management)
* [Data Engineering Helpers - Knowledge Sharing - Data lakehouse](https://github.com/data-engineering-helpers/data-lakehouse)
* [Data Engineering Helpers - Knowledge Sharing - Metadata](https://github.com/data-engineering-helpers/metadata)
* [Data Engineering Helpers - Knowledge Sharing - Data pipeline deployment](https://github.com/data-engineering-helpers/data-pipeline-deployment)

# Getting started

## Generate the sample data sets
* Launch the sample data set generation script:
```bash
./scripts/generate_sample_data.py
```

## Check the sample data sets
* Check the `customer_events` dataset:
```bash
parquet meta data/bronze/customer_events.parquet
Row group 0:  count: 10000  65.03 B records  start: 4  total(compressed): 635.017 kB total(uncompressed):832.905 kB
--------------------------------------------------------------------------------
                                        type      encodings count     avg size   nulls   min / max
event_id                                BINARY    S _ R     10000     37.87 B    0       "000034d1-a65c-47e9-8d08-4..." / "ffff44ef-18b6-4721-a6ec-5..."
customer_id                             BINARY    S _ R     10000     4.91 B     0       "004551b2-f7bc-48bf-be40-3..." / "ffac0e4c-36ab-4f0a-9e65-a..."
event_type                              BINARY    S _ R     10000     0.27 B     0       "consent_update" / "profile_update"
event_timestamp                         BINARY    S _ R     10000     17.36 B    0       "2025-03-14T18:25:17.957381" / "2025-04-13T18:22:41.992481"
source_system                           BINARY    S _ R     10000     0.26 B     0       "api" / "web"
event_data.consent_type                 BINARY    S _ R     10000     0.32 B     7572    "analytics" / "marketing"
event_data.device                       BINARY    S _ R     10000     0.32 B     7451    "desktop" / "tablet"
event_data.granted                      BOOLEAN   S   _     10000     0.28 B     7572    "false" / "true"
event_data.location                     BINARY    S _ R     10000     2.06 B     7451    "Adam" / "Étiennedan"
event_data.reason                       BINARY    S _ R     10000     0.33 B     7437    "system_update" / "verification"
event_data.success                      BOOLEAN   S   _     10000     0.28 B     7451    "false" / "true"
event_data.updated_fields.list.element  BINARY    S _ R     12582     0.63 B     7437    "address" / "preferences"
```

* Check the `customer_events` dataset:
```bash
parquet meta data/bronze/customer_profiles.parquet
Row group 0:  count: 1000  92.11 B records  start: 4  total(compressed): 89.954 kB total(uncompressed):126.688 kB
--------------------------------------------------------------------------------
                                        type      encodings count     avg size   nulls   min / max
profile_id                              BINARY    S _ R     1000      37.84 B    0       "004551b2-f7bc-48bf-be40-3..." / "ffac0e4c-36ab-4f0a-9e65-a..."
email                                   BINARY    S _ R     1000      12.23 B    0       "adamlaure@example.com" / "zrousseau@example.com"
email_status                            BINARY    S _ R     1000      0.36 B     0       "invalid" / "verified"
address.city                            BINARY    S _ R     1000      8.75 B     0       "Albert-sur-Jean" / "ÉtienneVille"
address.country                         BINARY    S _ R     1000      0.08 B     0       "France" / "France"
address.geo.lat                         DOUBLE    S _ R     1000      9.35 B     0       "-89.763624" / "89.8002425"
address.geo.lon                         DOUBLE    S _ R     1000      9.35 B     0       "-179.955893" / "179.97228"
address.street                          BINARY    S _ R     1000      13.31 B    0       "1, avenue Agnès Boutin" / "rue Étienne Fleury"
preferences.communication.list.element  BINARY    S _ R     1992      0.43 B     0       "email" / "sms"
```

# Installation

## `uv`

### MacOS
* Install `uv` with HomeBrew:
```bash
brew install uv
```

### Next steps
* Check the Python version for the project in the
  [`.python-version` file](https://github.com/monmaya/pyb-data-contracts/blob/main/.python-version)

* Derive the platform (_e.g._, `macos` on MacOS) and architecture (_e.g._,
  `aarch64` for ARM):
```bash
export platform="$(uname | tr '[:upper:]' '[:lower:]'|sed 's/darwin/macos/')"
export architecture="$(uname -m|sed 's/arm/aarch/')"
```

* Install the specific Python version for the project:
```bash
uv python install cpython-3.11.12-$platform-$architecture-none
```

