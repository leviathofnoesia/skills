---
name: infra-tagging-standard
description: "Enforce resource tagging for ownership and cost allocation."
---

# Infra-Tagging-Standard

Enforce resource tagging for ownership and cost allocation..

## When to Use

Cloud resources accumulate without ownership; cost attribution and incident response both suffer.

## Workflow

1. Define minimal mandatory tags: owner (team, not person), environment, cost-center, service, data-classification.
2. Keep the set SMALL — every additional tag halves compliance.
3. Enforce at creation: IaC modules embed tags; policy engines block untagged resources.
4. Remediate legacy inventory: bulk-tag by inference (naming patterns, VPC placement), confirm with owners.
5. Report compliance rates; make tagging visible in reviews.

## Pitfalls

Tag taxonomies growing to 20 keys nobody maintains. Person-names as owners (people leave, teams persist). Enforcement only at creation (legacy swamp persists). Tags treated as optional decoration.

## Verification

Compliance dashboard shows >95% tagged; orphaned-resource report returns empty; a cost question gets answered by tag query in seconds.

## Inputs

- Task context: cloud inventory access, org structure

## Outputs

- tag standard + enforcement + remediated inventory

## Related

cost-anomaly-hunt, config-change-journal
