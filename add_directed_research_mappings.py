#!/usr/bin/env python3
import json

COURSE_CODE = "CSE-DIRECTED-RESEARCH"
OUTCOMES = [
    "CE-PPP.CORE.4.8",
    "CE-PPP.CORE.9.1",
    "CE-PPP.CORE.9.2",
    "CE-PPP.CORE.9.5",
    "CE-PPP.CORE.9.6",
    "CE-PPP.ELECTIVE.11.1",
    "CE-PPP.ELECTIVE.11.2",
    "CE-PPP.ELECTIVE.11.3",
    "CE-PPP.ELECTIVE.11.6",
    "CE-SPE.ELECTIVE.3.5",
    "CE-SPE.ELECTIVE.3.7",
    "CE-SPE.ELECTIVE.5.10",
    "CE-SPE.ELECTIVE.5.11",
    "CE-SPE.ELECTIVE.6.8",
    "CE-SPE.ELECTIVE.6.9",
    "CE-SPE.ELECTIVE.7.8",
    "CE-SPE.ELECTIVE.11.8",
    "CE-SRM.CORE.2.1",
    "CE-SRM.ELECTIVE.7.1",
    "CE-SRM.ELECTIVE.7.2",
    "CE-SRM.ELECTIVE.7.3",
    "CE-SRM.ELECTIVE.7.4",
    "CE-SRM.ELECTIVE.7.5",
    "CE-SRM.ELECTIVE.7.6",
    "CE-SWD.CORE.2.4",
    "CE-SWD.CORE.3.2",
    "CE-SWD.CORE.4.1",
    "CE-SWD.CORE.4.6",
    "CE-SWD.CORE.8.2",
    "CE-SWD.CORE.8.4",
    "CE-SWD.CORE.8.7",
    "CE-SWD.ELECTIVE.14.1",
]


with open("course_abet_mapping.json", "r") as file:
    mapping_data = json.load(file)

existing = mapping_data["course_to_abet"].get(COURSE_CODE, [])
mapping_data["course_to_abet"][COURSE_CODE] = list(dict.fromkeys(existing + OUTCOMES))

for outcome_id in OUTCOMES:
    courses = mapping_data["abet_to_course"].setdefault(outcome_id, [])
    if COURSE_CODE not in courses:
        courses.append(COURSE_CODE)

with open("course_abet_mapping.json", "w") as file:
    json.dump(mapping_data, file, indent=2)

print(f"Added {len(OUTCOMES)} mappings to {COURSE_CODE}")
print(f"Total unique mapped outcomes: {len(mapping_data['abet_to_course'])}")
print(f"Coverage: {len(mapping_data['abet_to_course'])}/934 = {len(mapping_data['abet_to_course']) / 934 * 100:.1f}%")