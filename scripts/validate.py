#!/usr/bin/env python3
"""Classify evidence level of a medical study based on study design."""
import json, sys

def classify_evidence(data):
    study_type = data.get("study_type", "").lower()
    sample_size = data.get("sample_size", 0)
    peer_reviewed = data.get("peer_reviewed", False)

    levels = {
        "systematic review": 1, "meta-analysis": 1,
        "rct": 2, "randomized controlled trial": 2,
        "cohort": 3, "prospective cohort": 3,
        "case-control": 4, "cross-sectional": 4,
        "case series": 5, "case report": 5, "expert opinion": 6,
    }
    level = levels.get(study_type, 6)
    confidence = "high" if level <= 2 and sample_size > 100 else "moderate" if level <= 4 else "low"

    return {
        "evidence_level": level,
        "study_type": study_type,
        "confidence": confidence,
        "peer_reviewed": peer_reviewed,
        "note": "Not peer-reviewed — treat with caution" if not peer_reviewed else None
    }

if __name__ == "__main__":
    print(json.dumps(classify_evidence(json.loads(sys.argv[1])), indent=2))
