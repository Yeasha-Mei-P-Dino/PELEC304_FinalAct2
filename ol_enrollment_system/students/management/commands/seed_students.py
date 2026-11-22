from datetime import date
from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = "Seeds sample students into ol_enrollment_system"

    def handle(self, *args, **options):
        samples = [
            {
                "student_id": "STU-2026-001",
                "program": "BS Information Technology",
                "year_level": "1st Year",
                "enrollment_status": "Enrolled",
                "first_name": "Camille",
                "middle_name": "Reyes",
                "last_name": "Santos",
                "date_of_birth": date(2007, 4, 15),
                "gender": "Female",
                "email": "camille.santos@example.edu",
                "phone_number": "0917-555-0142",
                "address": "12 Quezon Ave, Lucena City, Quezon",
                "previous_school": "Quezon National High School",
                "graduation_year": "2026",
                "guardian_name": "Roberto Santos",
                "guardian_relationship": "Father",
                "guardian_contact": "0918-555-0199",
            },
            {
                "student_id": "STU-2026-002",
                "program": "BS Accountancy",
                "year_level": "2nd Year",
                "enrollment_status": "Pending",
                "first_name": "Marco",
                "middle_name": "Dizon",
                "last_name": "Bautista",
                "date_of_birth": date(2006, 9, 22),
                "gender": "Male",
                "email": "marco.bautista@example.edu",
                "phone_number": "0920-555-0178",
                "address": "48 Rizal St, Lucena City, Quezon",
                "previous_school": "Maryhill College",
                "graduation_year": "2025",
                "guardian_name": "Elena Bautista",
                "guardian_relationship": "Mother",
                "guardian_contact": "0921-555-0184",
            },
            {
                "student_id": "STU-2026-003",
                "program": "BS Civil Engineering",
                "year_level": "1st Year",
                "enrollment_status": "For Review",
                "first_name": "Hannah",
                "middle_name": "Lopez",
                "last_name": "Mendoza",
                "date_of_birth": date(2007, 1, 8),
                "gender": "Female",
                "email": "hannah.mendoza@example.edu",
                "phone_number": "0915-555-0130",
                "address": "7 Mabini Ext, Lucena City, Quezon",
                "previous_school": "Sacred Heart College",
                "graduation_year": "2026",
                "guardian_name": "Danilo Mendoza",
                "guardian_relationship": "Father",
                "guardian_contact": "0916-555-0161",
            },
        ]

        created_count = 0
        for item in samples:
            _, created = Student.objects.get_or_create(
                student_id=item["student_id"],
                defaults=item,
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Seed complete. Added {created_count} new student(s).")
        )