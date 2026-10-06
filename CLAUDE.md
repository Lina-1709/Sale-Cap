# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Sale-Cap is a workspace for a Sales Capability Team Leader in E-logistics / last-mile delivery. It holds analysis of Sales (BD) capability/assessment data, training and coaching materials, and project/communication content. There is no application build; work is mostly Python (pandas/openpyxl) analysis of Excel/CSV data and written deliverables.

## Setup

- Dependencies: `pip install -r requirements.txt` (installed automatically in cloud sessions by `.claude/hooks/session-start.sh`).
- No build, lint, or test commands are defined yet. Add them here when code is introduced.

## Working conventions

- Default language: Vietnamese; keep common Sales terms in English (BD, Seller, ADO, Lead, Pipeline, Conversion, KPI, ICP, CRM).
- Problem diagnosis flow: Business problem → Performance gap → Behavior gap → Capability gap → Root cause → Intervention → Manager reinforcement → Business impact. Do not jump from "performance is low" to "training"; first rule out lead quality, process, tool, incentive, coaching and policy causes.
- Capability architecture (use only the parts relevant): Lead Quality, Sales Conversion, Seller Growth, Sales Execution, Sales Leadership.
- Data analysis: clean → segment (team, level, G1/G2/G3, region, tenure, manager, capability group) → diagnose → recommend. Always check missing data, duplicates, sample size, outliers; state the denominator for every percentage; separate Observation / Interpretation / Recommendation; never claim causality from correlation.
- Never invent data, policy, or KPI definitions; label items as Known / Assumed / To be validated.
- Any training design must follow Learn → Practice → Apply → Coach → Measure → Reinforce and state what the frontline manager does to sustain it; link KPIs across Learning → Behavior → Business levels.
- Spreadsheet formulas: give the final copyable formula first, then a brief explanation and assumptions.
