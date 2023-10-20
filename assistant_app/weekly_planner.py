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


def upcoming(d: str, threshold: int) -> bool:
        today = date.today()
        
        month = int(d.split('-')[0])
        day = int(d.split('-')[1])
        year = today.year if (month >= today.month) else today.year + 1
        event_date = date(year, month, day)
        
        difference = event_date - today
        if 0 <= difference.days <= threshold:
            return True
        else:
            return False


def find_upcoming_dates(category: str) -> list[str]:
    thresholds = {"appointments": 10, "tasks": 10, "events": 20}
    dates: dict = planner_data[category]
    upcoming_dates = [f"{thing}: {date_time}" for thing, date_time in dates.items() \
                      if upcoming(date_time.split()[0], thresholds[category])]
    
    return upcoming_dates


def format_calendar() -> str:
    upcoming_appointments = find_upcoming_dates("appointments")
    upcoming_tasks = find_upcoming_dates("tasks")
    upcoming_events = find_upcoming_dates("events")

    calendar = f"## Calendar\n" + "**Appointments**\n" + "\n".join(upcoming_appointments) 
    calendar += "\n\n**Tasks**\n" + "\n".join(upcoming_tasks)
    calendar += "\n\n**Events**\n" + "\n".join(upcoming_events)
    return calendar


def format_maintenance() -> str:
    def section_to_string(section: str) -> str:
        s_list: list = planner_data['maintenance'][section]
        s: str = f"**{section.capitalize()}**\n" + "- [ ] " + "\n- [ ] ".join(s_list) + "\n\n"
        return s

    chores: str = section_to_string('chores')
    physical_exercises: str = section_to_string('physical exercise')
    creative_exercises: str = section_to_string('creative exercise')
    social_interaction: str = section_to_string('social interaction')

    output: str = "## Maintenance\n\n" 
    output += (chores + physical_exercises + creative_exercises + social_interaction)
    return output



def create_note() -> None:
    maintenance: str = format_maintenance()
    calendar: str = format_calendar()
    output: str = "\n" + calendar + "\n" + maintenance
    #print(output)
    with open(notebook_path + "Weekly Planner.md", 'w') as planner_note_file:
        planner_note_file.write(f"Weekly Planner for the week of {date.today()}:\n\n" + output)


def main():
    create_note()


if __name__ == "__main__":
    main()