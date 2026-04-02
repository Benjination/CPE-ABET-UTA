#!/usr/bin/env python3
import json


HARDWARE_COURSE = "CSE-ADV-HARDWARE"
SYSTEMS_COURSE = "CSE-RELIABLE-DISTRIBUTED"

HARDWARE_OUTCOMES = [
    "CE-CAE.CORE.10.2",
    "CE-CAE.CORE.6.6",
    "CE-CAE.CORE.7.3",
    "CE-CAE.CORE.8.2",
    "CE-CAE.CORE.8.4",
    "CE-CAE.CORE.8.5",
    "CE-CAE.ELECTIVE.10.6",
    "CE-CAE.ELECTIVE.10.7",
    "CE-CAE.ELECTIVE.10.8",
    "CE-CAE.ELECTIVE.4.11",
    "CE-CAE.ELECTIVE.4.12",
    "CE-CAE.ELECTIVE.4.14",
    "CE-CAE.ELECTIVE.5.11",
    "CE-CAE.ELECTIVE.5.12",
    "CE-CAE.ELECTIVE.5.13",
    "CE-CAE.ELECTIVE.7.4",
    "CE-CAE.ELECTIVE.7.5",
    "CE-CAE.SUPPLEMENTAL.11.1",
    "CE-CAE.SUPPLEMENTAL.11.3",
    "CE-CAE.SUPPLEMENTAL.11.4",
    "CE-CAE.SUPPLEMENTAL.11.5",
    "CE-CAE.SUPPLEMENTAL.11.6",
    "CE-CAE.SUPPLEMENTAL.12.4",
    "CE-DIG.ELECTIVE.10.1",
    "CE-DIG.ELECTIVE.10.4",
    "CE-DIG.ELECTIVE.10.5",
    "CE-DIG.ELECTIVE.10.7",
    "CE-DIG.ELECTIVE.11.4",
    "CE-DIG.ELECTIVE.7.10",
    "CE-DIG.ELECTIVE.7.11",
    "CE-DIG.ELECTIVE.8.7",
    "CE-DIG.ELECTIVE.8.9",
    "CE-ESY.ELECTIVE.13.2",
    "CE-ESY.ELECTIVE.13.3",
    "CE-ESY.ELECTIVE.13.4",
    "CE-SGP.CORE.10.1",
    "CE-SGP.CORE.7.4",
    "CE-SGP.ELECTIVE.11.1",
]

SYSTEMS_OUTCOMES = [
    "CE-CAL.SUPPLEMENTAL.10.2",
    "CE-CAL.SUPPLEMENTAL.10.3",
    "CE-CAL.SUPPLEMENTAL.10.5",
    "CE-CAO.CORE.5.5",
    "CE-CAO.CORE.7.8",
    "CE-CAO.ELECTIVE.11.11",
    "CE-CAO.ELECTIVE.11.7",
    "CE-CAO.ELECTIVE.11.8",
    "CE-CAO.ELECTIVE.11.9",
    "CE-CAO.ELECTIVE.2.4",
    "CE-CAO.ELECTIVE.5.8",
    "CE-CAO.ELECTIVE.5.9",
    "CE-CAO.ELECTIVE.7.9",
    "CE-SPE.ELECTIVE.3.6",
    "CE-SPE.ELECTIVE.4.15",
    "CE-SPE.ELECTIVE.4.16",
    "CE-SPE.ELECTIVE.5.12",
    "CE-SPE.ELECTIVE.5.13",
    "CE-SPE.ELECTIVE.5.14",
    "CE-SPE.ELECTIVE.5.15",
    "CE-SPE.ELECTIVE.8.8",
    "CE-SPE.ELECTIVE.8.9",
    "CE-SRM.ELECTIVE.8.2",
    "CE-SRM.ELECTIVE.8.4",
    "CE-SRM.ELECTIVE.8.5",
    "CE-SWD.CORE.11.1",
    "CE-SWD.ELECTIVE.12.3",
]


with open("courses_organized.json", "r") as file:
    courses_data = json.load(file)

with open("course_abet_mapping.json", "r") as file:
    mapping_data = json.load(file)

suggested_courses = {
    code for code, course in courses_data.items() if course.get("suggested")
}

# Add the two new suggested course mappings first.
for outcome_id in HARDWARE_OUTCOMES:
    mapping_data["abet_to_course"].setdefault(outcome_id, [])
    if HARDWARE_COURSE not in mapping_data["abet_to_course"][outcome_id]:
        mapping_data["abet_to_course"][outcome_id].append(HARDWARE_COURSE)

for outcome_id in SYSTEMS_OUTCOMES:
    mapping_data["abet_to_course"].setdefault(outcome_id, [])
    if SYSTEMS_COURSE not in mapping_data["abet_to_course"][outcome_id]:
        mapping_data["abet_to_course"][outcome_id].append(SYSTEMS_COURSE)

# Enforce rule: if an outcome has any degree-plan course mapping, remove all suggested-course mappings.
clean_abet_to_course = {}
removed_overlaps = 0

for outcome_id, courses in mapping_data["abet_to_course"].items():
    deduped = list(dict.fromkeys(courses))
    has_degree_plan = any(course not in suggested_courses for course in deduped)

    if has_degree_plan:
        filtered = [course for course in deduped if course not in suggested_courses]
        removed_overlaps += len(deduped) - len(filtered)
    else:
        filtered = deduped

    if filtered:
        clean_abet_to_course[outcome_id] = filtered

mapping_data["abet_to_course"] = clean_abet_to_course

# Rebuild course_to_abet from cleaned abet_to_course for consistency.
all_course_codes = set(courses_data.keys())
for course_list in mapping_data["abet_to_course"].values():
    all_course_codes.update(course_list)

rebuilt_course_to_abet = {course_code: [] for course_code in sorted(all_course_codes)}
for outcome_id, course_list in mapping_data["abet_to_course"].items():
    for course_code in course_list:
        rebuilt_course_to_abet[course_code].append(outcome_id)

mapping_data["course_to_abet"] = rebuilt_course_to_abet

with open("course_abet_mapping.json", "w") as file:
    json.dump(mapping_data, file, indent=2)

print("Applied two new suggested courses and overlap pruning.")
print(f"Removed overlapping suggested mappings: {removed_overlaps}")
print(f"Mapped unique outcomes: {len(mapping_data['abet_to_course'])}")
print(f"Coverage: {len(mapping_data['abet_to_course'])}/934 = {len(mapping_data['abet_to_course']) / 934 * 100:.1f}%")

for code in sorted(suggested_courses):
    count = len(mapping_data["course_to_abet"].get(code, []))
    print(f"{code}: {count} outcomes")