"""
"""

import os, sys, yaml, random
from datetime import datetime
from datetime import timedelta
from datetime import date

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = script_dir + '/data/'


with open(data_dir + "weekly_planner_data.yaml", 'r') as planner_file:
    planner_data: dict = yaml.safe_load(planner_file)

notebook_path: str = planner_data['notebook_path']


def format_appointments_and_events() -> str:
    def upcoming(d: str) -> bool:
        today = date.today()
        
        month = int(d.split('-')[0])
        day = int(d.split('-')[1])
        year = today.year if (month >= today.month) else today.year + 1
        event_date = date(year, month, day)
        
        difference = event_date - today
        # print(month, day, year, difference)
        if 0 <= difference.days <= 14:
            return True
        else:
            return False
    
    appointments: dict = planner_data['appointments']
    upcoming_appointments = [f"{key}: {appointments[key]}" for key in appointments.keys() if upcoming(appointments[key].split()[0])]

    events: dict = planner_data['events']
    upcoming_events = [f"{key}: {events[key]}" for key in events.keys() if upcoming(events[key])]

    output = f"## Calendar\n" + "**Appointments**\n" + "\n".join(upcoming_appointments) + "\n\n**Events**\n" + "\n".join(upcoming_events)
    return output



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
    calendar: str = format_appointments_and_events()
    output: str = "\n" + calendar + "\n" + maintenance
    #print(output)
    with open(notebook_path + "Weekly Planner.md", 'w') as planner_note_file:
        planner_note_file.write(f"Weekly Planner for the week of {date.today()}:\n\n" + output)


def main():
    create_note()


if __name__ == "__main__":
    main()