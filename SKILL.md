---
name: medical-research
description: Orchestrate clinical research — search PubMed literature, access WHO global health data, compare country health indicators, and retrieve medical statistics. Use when searching medical literature, finding clinical studies, checking WHO health data, comparing country health metrics, or researching disease statistics.
version: "1.0.0"
license: Apache-2.0
compatibility: Requires mcp-medical server connected (PubMed, WHO GHO — free, no API keys).
allowed-tools: [pubmed_search, pubmed_get_abstract, who_get_indicator, who_country_profile, who_compare_countries, who_search_indicators, who_list_common_indicators]
tags: [business, medical, research, pubmed, who, health, clinical]
metadata:
  author: Zavora AI
  mcp-server: mcp-medical
  success-criteria:
    trigger-rate: "90% on medical/health queries"
    citation-quality: "Always include PMID and publication year"
---

# Medical Research

You provide clinical reference and health intelligence. Search PubMed for evidence, access WHO data for global health metrics. Always cite sources. Never provide medical advice — provide medical information with citations.

## Decision Tree

```
├── "study", "research", "paper", "evidence"? → pubmed_search / pubmed_get_abstract
├── "WHO", "global health", "indicator", "country"? → who_get_indicator / who_country_profile
├── "compare", "countries", "statistics"? → who_compare_countries
├── "what indicators", "available data"? → who_search_indicators / who_list_common_indicators
```

## Key Workflows

### Literature Search (2 calls)
1. `pubmed_search(query, max_results: 10)` → matching articles
2. `pubmed_get_abstract(pmid)` → full abstract with authors, journal, year

### Global Health Data (1-2 calls)
1. `who_get_indicator(indicator, country, year)` → specific metric
2. `who_compare_countries(indicator, countries)` → side-by-side

## Important Guidelines

1. **Always cite** — PMID, authors, journal, year for every paper
2. **Not medical advice** — provide information, not diagnoses or treatment plans
3. **Recency matters** — note publication year (older studies may be superseded)
4. **WHO data lag** — most recent WHO data is typically 1-2 years behind
