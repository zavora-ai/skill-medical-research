# Evidence Summary Template

Use this structure when presenting medical research findings.

---

## 🔬 {research_topic}

**Query:** {search_query} | **Sources Reviewed:** {source_count} | **Date:** {report_date}

### Evidence Overview

| Study | Design | Sample | Outcome | Quality |
|-------|--------|--------|---------|---------|
| {study_name} | {study_design} | n={sample_size} | {primary_outcome} | {quality_rating} |

### Key Findings

| Finding | Evidence Level | Confidence |
|---------|---------------|------------|
| {finding_summary} | {evidence_level} | {confidence_emoji} {confidence} |

{confidence_emoji mapping: high=✅, moderate=⚠️, low=❓}

### Clinical Relevance

| Factor | Assessment |
|--------|-----------|
| Applicability | {applicability} |
| Effect Size | {effect_size} |
| NNT/NNH | {nnt_nnh} |
| Recommendation | {recommendation_grade} |

{if evidence_level == "Level I": "✅ Strong evidence — supports clinical decision"}
{if quality_rating == "Low": "⚠️ Low-quality evidence — interpret with caution"}

---

*Generated from mcp-medical | {timestamp}*
