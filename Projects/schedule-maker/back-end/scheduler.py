# ---------------------------------------
# Main Execution
# ---------------------------------------


def __main__():
    # Example scenario with multiple areas:
    shifts = [
        # Mainline
        {"name": "Veronica", "start": "06:00", "end": "15:00", "area": "mainline"},
        {"name": "Merlin", "start": "17:30", "end": "21:30", "area": "mainline"},
        {"name": "Jerra", "start": "13:00", "end": "18:00", "area": "mainline"},
        {"name": "Katrina", "start": "08:00", "end": "13:00", "area": "mainline"},
        {"name": "Lynda", "start": "15:00", "end": "20:00", "area": "mainline"},
        # Garden
        {"name": "Rose", "start": "09:00", "end": "14:00", "area": "garden"},
        {"name": "Brittany", "start": "14:00", "end": "19:00", "area": "garden"},
        # Lumber
        {"name": "Glen", "start": "12:30", "end": "21:30", "area": "lumber"},
        {"name": "Nancy", "start": "06:00", "end": "14:30", "area": "lumber"},
        # Customer Service
        {
            "name": "Judith",
            "start": "06:00",
            "end": "15:00",
            "area": "customer service",
        },
        {"name": "Max", "start": "06:00", "end": "15:00", "area": "customer service"},
        {
            "name": "Campbell",
            "start": "15:00",
            "end": "21:00",
            "area": "customer service",
        },
        # Headcashiers
        {"name": "Evan", "start": "06:00", "end": "14:00", "area": "headcashiers"},
        {"name": "May", "start": "13:30", "end": "21:00", "area": "headcashiers"},
    ]


if __name__ == "__main__":
    __main__()
