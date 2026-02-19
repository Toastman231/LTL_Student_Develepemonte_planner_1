import uuid
from datetime import datetime
from data.store import load_data, save_data


def list_students():
    data = load_data()
    return data.get("students", [])


def add_student(first, last, grade="", school="", student_class=""):
    data = load_data()
    students = data.setdefault("students", [])

    student = {
        "id": str(uuid.uuid4()),
        "first_name": first.strip(),
        "last_name": last.strip(),
        "grade": grade.strip(),
        "school": school.strip(),
        "class": student_class.strip(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }

    students.append(student)
    save_data(data)
    return student["id"]
