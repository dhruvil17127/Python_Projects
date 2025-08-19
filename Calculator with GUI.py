import calendar
from datetime import datetime
from rich.console import Console
from rich.table import Table

def colorful_month_calendar(year, month):
    console = Console()

    # Get month name & weeks
    month_name = calendar.month_name[month]
    month_weeks = calendar.monthcalendar(year, month)

    # Table title
    table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

    # Weekday headers with colors
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    colors = ["green", "green", "green", "green", "green", "yellow", "red"]

    for day, color in zip(days, colors):
        table.add_column(day, justify="center", style=color)

    # Get today's date
    today = datetime.today()
    is_current_month = (today.year == year and today.month == month)

    # Add weeks
    for week in month_weeks:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            elif is_current_month and day == today.day:
                row.append(f"[bold red]{day}[/bold red]")  # highlight today
            else:
                row.append(str(day))
        table.add_row(*row)

    console.print(table)


# ---------- User Input ----------
try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    if 1 <= month <= 12:
        colorful_month_calendar(year, month)
    else:
        print("❌ Invalid month! Please enter a value between 1 and 12.")
except ValueError:
    print("❌ Please enter valid numbers for year and month.")
