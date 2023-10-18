"""
"""

import os, sys, yaml, random
from datetime import datetime
from datetime import timedelta

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = script_dir + '/data/'


with open(data_dir + "weekly_planner_data.yaml", 'r') as planner_file:
    planner_data: dict = yaml.safe_load(planner_file)

notebook_path: str = planner_data['notebook_path']


def format_appointments_and_events() -> str:
    appointments: dict = planner_data['appointments']
    today = datetime.today()



def format_maintenance() -> str:
    def section_to_string(section: str) -> str:
        s_list: list = planner_data['maintenance'][section]
        s: str = f"**{section.capitalize()}**\n" + "- [ ] " + "\n- [ ] ".join(s_list) + "\n\n"
        return s

    chores: str = section_to_string('chores')
    physical_exercises: str = section_to_string('physical exercise')
    creative_exercises: str = section_to_string('creative exercise')
    social_interaction: str = section_to_string('social interaction')

    output: str = "## Maintenance\n\n" + chores + physical_exercises + creative_exercises + social_interaction
    return output



def create_note() -> None:
    maintenance: str = format_maintenance()
    print(maintenance)


def main():
    create_note()


if __name__ == "__main__":
    main()