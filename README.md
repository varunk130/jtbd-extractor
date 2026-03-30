# 🎯 JTBD Extractor

> Turn raw research into Jobs-to-be-Done statements showing what users are really trying to accomplish — reframing feature requests as underlying needs and uncovering innovation opportunities.

![JTBD Extractor Overview](assets/jtbd-overview.png)

[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-blueviolet)](#installation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What It Does

The JTBD Extractor is a Claude Code skill that transforms unstructured research data (interviews, surveys, support tickets, feedback) into structured Jobs-to-be-Done analysis.

### Output Includes

| Component | Description |
|---|---|
| **JTBD Statements** | Properly formatted "When [situation], I want to [action], so I can [outcome]" |
| **Job Categories** | Separated into Functional, Emotional, and Social jobs |
| **Opportunity Scores** | `Importance + (Importance - Satisfaction)` to show where to focus |
| **Evidence Tracking** | Direct quotes and behavior supporting each job |
| **Feature Translation** | Mapping what users asked for → what they actually need |
| **Top Opportunities** | Ranked list of underserved jobs worth solving |

---

## Installation

### Claude Code Desktop
1. Clone or download this repo
2. Copy the folder to `~/.claude/skills/jtbd-extractor`
3. Restart Claude Code Desktop

### Claude Code Terminal
```bash
git clone https://github.com/varunk130/jtbd-extractor.git ~/.claude/skills/jtbd-extractor
```

### Project-Specific Use
Place in `.claude/skills/` within your project folder instead of the global location.

---

## Usage

In any Claude Code chat, type:

```
/jtbd-extractor
```

Claude will walk you through the process step-by-step:

1. **Reviews your context** — checks existing personas, product docs, and prior research
2. **Requests research data** — interview transcripts, surveys, support tickets, or feedback
3. **Identifies jobs** — extracts what users are really trying to accomplish
4. **Formats as JTBD** — structures each job as `When / I want to / So I can`
5. **Categorizes** — sorts into Functional, Emotional, and Social jobs
6. **Scores opportunities** — rates importance vs. satisfaction to find gaps

---

## Example Output

```markdown
### Functional Jobs
| Job Statement | Importance | Satisfaction | Opportunity | Evidence |
|---|---|---|---|---|
| When preparing for a quarterly review, I want to see my team's progress at a glance, so I can present confidently without manual data gathering | 8/10 | 4/10 | 12 | "I spend 3 hours every quarter pulling numbers from 5 different tools" |

### Feature Request Translation
| Request (What They Said) | Job (What They Need) |
|---|---|
| "Add a dashboard" | "Know if I'm on track without manual checking" |
| "Export to PDF" | "Share progress with stakeholders who don't have access" |
```

---

## When to Use

- **Reframing feature requests** into underlying needs
- **Finding innovation opportunities** in saturated markets
- **Training your team** to think in jobs, not features
- **Post-interview synthesis** to extract structured insights
- **Competitive analysis** to find underserved jobs in the market

---

## What You'll Need

- Interview transcripts, survey responses, or customer feedback
- Context on your product/market (optional but recommended)

---

## Framework Reference

**Jobs-to-be-Done**:
- People don't buy products — they hire them to do a job
- Jobs are stable; solutions change
- **Opportunity = Importance + (Importance - Satisfaction)**

---

## Tips for Best Results

1. **Keep personas.md updated** — the skill connects new jobs to existing personas
2. **Focus on jobs, not solutions** — "I need a hole" not "Hire a drill"
3. **Look for emotional and social jobs** — they often drive decisions more than functional ones
4. **Validate scores quantitatively** — low-confidence scores from small samples need survey validation

---

## File Structure

```
jtbd-extractor/
├── README.md       # This file
└── SKILL.md        # Claude Code skill definition
```

Output is saved to: `discovery/outputs/jtbd-[persona]-[YYYY-MM-DD].md`

---

## License

MIT — use it however you want.

---

Built by [varunk130](https://github.com/varunk130)
