#!/usr/bin/env python3
import json


MAPPINGS = {
    "CSE3313": [
        "CE-SGP.CORE.10.9",
        "CE-SGP.ELECTIVE.9.4",
    ],
    "CSE4342": [
        "CE-SGP.ELECTIVE.11.3",
        "CE-SGP.ELECTIVE.11.5",
        "CE-ESY.ELECTIVE.5.6",
        "CE-ESY.ELECTIVE.5.7",
    ],
    "CSE3441": [
        "CE-ESY.CORE.8.2",
        "CE-ESY.CORE.8.5",
        "CE-ESY.CORE.10.4",
        "CE-SRM.CORE.3.4",
        "CE-SRM.CORE.3.7",
        "CE-SRM.CORE.4.4",
    ],
    "CSE3320": [
        "CE-CAL.SUPPLEMENTAL.9.1",
    ],
    "CSE3318": [
        "CE-SWD.CORE.5.3",
        "CE-SWD.CORE.6.3",
        "CE-SWD.CORE.6.4",
        "CE-SWD.ELECTIVE.4.7",
    ],
    "CSE2441": [
        "CE-DIG.CORE.3.1",
        "CE-DIG.CORE.3.2",
        "CE-DIG.CORE.3.3",
        "CE-DIG.CORE.7.1",
        "CE-DIG.CORE.7.3",
        "CE-DIG.CORE.7.8",
        "CE-CAL.SUPPLEMENTAL.10.1",
        "CE-DIG.ELECTIVE.10.2",
        "CE-DIG.ELECTIVE.10.6",
    ],
    "CSE2312": [
        "CE-DIG.CORE.3.4",
    ],
    "CSE3442": [
        "CE-CAO.CORE.2.2",
        "CE-CAO.CORE.6.2",
        "CE-CAO.CORE.9.6",
    ],
    "CSE4323": [
        "CE-CAL.CORE.7.3",
        "CE-CAO.CORE.11.3",
        "CE-CAO.ELECTIVE.3.11",
        "CE-CAO.ELECTIVE.6.10",
        "CE-CAO.ELECTIVE.6.11",
        "CE-CAO.ELECTIVE.6.12",
        "CE-CAO.ELECTIVE.6.13",
        "CE-CAO.ELECTIVE.6.14",
        "CE-CAO.ELECTIVE.11.10",
        "CE-DIG.ELECTIVE.8.8",
    ],
    "CSE3323": [
        "CE-CAE.ELECTIVE.4.13",
        "CE-CAE.ELECTIVE.5.8",
        "CE-CAE.ELECTIVE.5.9",
        "CE-CAE.ELECTIVE.5.10",
        "CE-CAE.ELECTIVE.5.14",
        "CE-CAE.ELECTIVE.9.4",
        "CE-CAE.ELECTIVE.9.5",
    ],
    "CSE2440": [
        "CE-CAE.ELECTIVE.3.6",
        "CE-CAE.ELECTIVE.3.7",
        "CE-CAE.ELECTIVE.3.8",
        "CE-CAE.SUPPLEMENTAL.12.1",
    ],
    "CSE4316": [
        "CE-SPE.ELECTIVE.9.7",
        "CE-SPE.ELECTIVE.9.8",
    ],
}


with open("course_abet_mapping.json", "r") as file:
    mapping_data = json.load(file)

added = 0

for course_code, outcome_ids in MAPPINGS.items():
    course_outcomes = mapping_data["course_to_abet"].setdefault(course_code, [])

    for outcome_id in outcome_ids:
        if outcome_id not in course_outcomes:
            course_outcomes.append(outcome_id)

        mapped_courses = mapping_data["abet_to_course"].setdefault(outcome_id, [])
        if course_code not in mapped_courses:
            mapped_courses.append(course_code)
            added += 1

with open("course_abet_mapping.json", "w") as file:
    json.dump(mapping_data, file, indent=2)

print(f"Added {added} course-outcome links across existing courses")
print(f"Total unique mapped outcomes: {len(mapping_data['abet_to_course'])}")
print(f"Coverage: {len(mapping_data['abet_to_course'])}/934 = {len(mapping_data['abet_to_course']) / 934 * 100:.1f}%")