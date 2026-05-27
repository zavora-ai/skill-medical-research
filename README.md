# Medical Research Skill

> Clinical reference and global health intelligence for AI agents — PubMed literature search, WHO health indicators, country comparisons, and medical statistics. Free, no API keys required.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--medical-green)](https://github.com/zavora-ai/mcp-medical)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Literature Search | 2 | Find studies + get abstracts with citations |
| Global Health Data | 1-2 | WHO indicators by country |
| Country Comparison | 1 | Side-by-side health metrics |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-medical-research.git ~/.skills/skills/medical-research
```

## Requirements

**Required:** `mcp-medical` (7 tools — PubMed + WHO GHO, free, no API keys)

## Success Criteria

| Metric | Target |
|--------|--------|
| Citation quality | Always include PMID + year |
| Not medical advice | Information only, with sources |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
