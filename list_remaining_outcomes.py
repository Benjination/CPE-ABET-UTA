#!/usr/bin/env python3
import json
import sys


with open("course_abet_mapping.json", "r") as file:
    mapping_data = json.load(file)

with open("abet_organized.json", "r") as file:
    abet_data = json.load(file)

mapped_outcomes = set(mapping_data["abet_to_course"].keys())
requested_areas = sys.argv[1:] if len(sys.argv) > 1 else sorted(abet_data.keys())

for area_code in requested_areas:
    if area_code not in abet_data:
        continue

    area = abet_data[area_code]
    print(f"== {area_code} {area['name']} ==")
    count = 0

    for category, tiers in area["categories"].items():
        for tier, outcomes in tiers.items():
            for outcome in outcomes:
                outcome_id = f"{area_code}.{category}.{tier}.{outcome['id']}"
                if outcome_id not in mapped_outcomes:
                    count += 1
                    text = " ".join(outcome["outcome"].split())
                    print(f"{outcome_id} | {text}")

    print(f"TOTAL {count}\n")