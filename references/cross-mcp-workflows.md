# Medical Cross-MCP Workflows

## Medical + Knowledge Base: Evidence → Article
```
MEDICAL: pubmed_search(query: "diabetes management guidelines 2024")
MEDICAL: pubmed_get_abstract(pmid) → key findings
KB: create_draft(title: "Latest Diabetes Guidelines (2024)", body: summary_with_citations)
```
