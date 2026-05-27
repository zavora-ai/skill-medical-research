# Medical Examples

## Example 1: "Find recent studies on malaria vaccines"
```
pubmed_search(query: "malaria vaccine efficacy 2024", max_results: 5)
→ [{pmid: "39123456", title: "RTS,S/AS01 vaccine efficacy in African children...", year: 2024}]
pubmed_get_abstract(pmid: "39123456") → full abstract
```
Response: "Found 5 recent studies. Top result: 'RTS,S/AS01 vaccine efficacy...' (2024, PMID: 39123456). Shows 36% efficacy over 4 years in children 5-17 months."

## Example 2: "Compare life expectancy: Kenya vs Nigeria vs South Africa"
```
who_compare_countries(indicator: "life_expectancy", countries: ["KE", "NG", "ZA"])
→ {KE: 67.5, NG: 54.7, ZA: 65.3}
```
Response: "Life expectancy: Kenya 67.5, South Africa 65.3, Nigeria 54.7 years (WHO, latest available)."
