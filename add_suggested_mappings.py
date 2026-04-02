#!/usr/bin/env python3
"""
Add mappings for suggested courses (Networks and Security)
"""
import json

# Load ABET outcomes
with open('abet_organized.json', 'r') as f:
    abet_data = json.load(f)

# Load current mapping
with open('course_abet_mapping.json', 'r') as f:
    mapping_data = json.load(f)

# Get all outcomes that are NOT yet mapped
mapped_outcomes = set(mapping_data['abet_to_course'].keys())

# Extract all CE-NWK and CE-SEC outcome IDs from ABET data
nwk_outcomes = []
sec_outcomes = []

for area_code, area_data in abet_data.items():
    if area_code == 'CE-NWK':
        for category, tiers in area_data['categories'].items():
            for tier, outcomes in tiers.items():
                for outcome in outcomes:
                    outcome_id = f"{area_code}.{category}.{tier}.{outcome['id']}"
                    if outcome_id not in mapped_outcomes:
                        nwk_outcomes.append(outcome_id)
    elif area_code == 'CE-SEC':
        for category, tiers in area_data['categories'].items():
            for tier, outcomes in tiers.items():
                for outcome in outcomes:
                    outcome_id = f"{area_code}.{category}.{tier}.{outcome['id']}"
                    if outcome_id not in mapped_outcomes:
                        sec_outcomes.append(outcome_id)

print(f"Found {len(nwk_outcomes)} CE-NWK outcomes to map to CSE-NETWORKS")
print(f"Found {len(sec_outcomes)} CE-SEC outcomes to map to CSE-SECURITY")

# Add to course_to_abet
mapping_data['course_to_abet']['CSE-NETWORKS'] = nwk_outcomes
mapping_data['course_to_abet']['CSE-SECURITY'] = sec_outcomes

# Add to abet_to_course
for outcome_id in nwk_outcomes:
    if outcome_id not in mapping_data['abet_to_course']:
        mapping_data['abet_to_course'][outcome_id] = []
    if 'CSE-NETWORKS' not in mapping_data['abet_to_course'][outcome_id]:
        mapping_data['abet_to_course'][outcome_id].append('CSE-NETWORKS')

for outcome_id in sec_outcomes:
    if outcome_id not in mapping_data['abet_to_course']:
        mapping_data['abet_to_course'][outcome_id] = []
    if 'CSE-SECURITY' not in mapping_data['abet_to_course'][outcome_id]:
        mapping_data['abet_to_course'][outcome_id].append('CSE-SECURITY')

# Save the updated mapping
with open('course_abet_mapping.json', 'w') as f:
    json.dump(mapping_data, f, indent=2)

print(f"\n✅ Added mappings successfully!")
print(f"Total mapped outcomes: {len(mapping_data['abet_to_course'])}")
print(f"New coverage: {len(mapping_data['abet_to_course'])}/934 = {(len(mapping_data['abet_to_course'])/934)*100:.1f}%")
