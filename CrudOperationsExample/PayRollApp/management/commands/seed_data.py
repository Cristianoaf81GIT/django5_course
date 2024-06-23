import random
from django.core.management.base import BaseCommand

from PayRollApp.models import Employee, Department, Country

from faker import Faker
from faker.providers import company, address, person, misc, profile, date_time


class Command(BaseCommand):
    help: str = "Seed Employee/Department and Country tables"
    _faker: Faker = Faker()

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "num",
            type=int,
            help="Number of seed (Employee/Department/Country) to create!",
        )

    def handle(self, *_, **options) -> None:
        num = int(options["num"])
        self._faker.add_provider(company)
        self._faker.add_provider(address)
        self._faker.add_provider(person)
        self._faker.add_provider(misc)
        self._faker.add_provider(profile)
        self._faker.add_provider(date_time)

        if not num:
            raise Exception("num is mandatory")

        self.stdout.write(
            self.style.SUCCESS(  # pyright: ignore
                "Seeding database tables [Department, Country and Employee] ..."
            )
        )

        for _ in range(num):
            dept = Department(
                dept_name=self._faker.catch_phrase(), location_name=self._faker.city()
            )
            dept.save()

            country = Country(country_name=self._faker.country())
            country.save()

            emp_profile = self._faker.profile()

            employee = Employee(
                first_name=self._faker.first_name(),
                last_name=self._faker.last_name(),
                title_name=self._faker.prefix(),
                has_passport=self._faker.boolean(),
                salary=random.uniform(3000.0, 25000.999),
                birth_date=emp_profile.get("birthdate"),
                hire_date=self._faker.past_datetime(),
                notes=emp_profile.get("job"),
                email=emp_profile.get("mail"),
                phone_number=emp_profile.get("ssn"),
                emp_department=dept,
                emp_country=country,
            )
            employee.save()
        self.stdout.write(self.style.SUCCESS("Database seeding completed."))  # pyright: ignore
