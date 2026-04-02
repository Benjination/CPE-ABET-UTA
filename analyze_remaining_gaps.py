#!/usr/bin/env python3
"""
Analyze remaining unmapped outcomes for Directed Research course fit
"""
import json

# Load current mapping
with open('course_abet_mapping.json', 'r') as f:
    mapping_data = json.load(f)

# Load ABET data
with open('abet_organized.json', 'r') as f:
    abet_data = json.load(f)

mapped_outcomes = set(mapping_data['abet_to_course'].keys())

# Find all unmapped outcomes by area
unmapped_by_area = {}
for area_code, area_data in abet_data.items():
    for category, tiers in area_data['categories'].items():
        for tier, outcomes in tiers.items():
            for outcome in outcomes:
                outcome_id = f"{area_code}.{category}.{tier}.{outcome['id']}"
                if outcome_id not in mapped_outcomes:
                    if area_code not in unmapped_by_area:
                        unmapped_by_area[area_code] = {
                            'name': area_data['name'],
                            'outcomes': []
                        }
                    unmapped_by_area[area_code]['outcomes'].append({
                        'id': outcome_id,
                        'category': category,
                        'text': outcome['outcome']
                    })

# Print breakdown
print('=' * 80)
print('REMAINING 117 UNMAPPED OUTCOMES BY AREA')
print('=' * 80)
print()

for area_code in sorted(unmapped_by_area.keys()):
    area = unmapped_by_area[area_code]
    print(f"{area_code} ({area['name']}): {len(area['outcomes'])} outcomes")
    
    # Show sample outcomes
    print(f"  Sample outcomes:")
    for i, outcome in enumerate(area['outcomes'][:3]):
        text = outcome['text'].strip()
        if len(text) > 90:
            text = text[:90] + "..."
        print(f"    {i+1}. [{outcome['category']}] {text}")
    print()

print('=' * 80)
print('ANALYSIS FOR DIRECTED RESEARCH COURSE FIT')
print('=' * 80)
print()
print("A Directed Research course typically covers:")
print("  - Independent investigation and problem-solving")
print("  - Technical writing and documentation")
print("  - Data collection, analysis, and interpretation")
print("  - Presentation and communication skills")
print("  - Project planning and management")
print("  - Professional/ethical considerations")
print()

# Categories that fit well with research
research_friendly_areas = {
    'CE-PPP': 'Professional Practice',  # Communication, ethics, teamwork
    'CE-SPE': 'Systems and Project Engineering',  # Design, testing, project management
    'CE-SRM': 'Software Requirements',  # Requirements, specifications, documentation
    'CE-SWD': 'Software Development',  # Advanced development topics
}

# Check which unmapped areas align with research
print("Unmapped outcomes that align with Directed Research:")
print()

research_fit_count = 0
for area_code, description in research_friendly_areas.items():
    if area_code in unmapped_by_area:
        count = len(unmapped_by_area[area_code]['outcomes'])
        research_fit_count += count
        print(f"✓ {area_code} ({description}): {count} outcomes")

print()
other_count = 117 - research_fit_count
print(f"Research-friendly outcomes: {research_fit_count}")
print(f"Technical/specialized outcomes: {other_count}")
print()
print(f"Recommendation: A Directed Research course could reasonably cover")
print(f"the {research_fit_count} outcomes from PPP, SPE, SRM, and SWD areas.")
