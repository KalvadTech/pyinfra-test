from pyinfra import host
from pyinfra.facts.server import OsRelease
from pyinfra.operations import apt, postgres

os_release = host.get_fact(OsRelease)
if os_release["name"] == "Ubuntu":
    apt.packages(
        name="Install PostgreSQL",
        packages=["postgresql", "postgresql-contrib"],
        _sudo=True,
    )
    postgres.role(
        name="Create the pyinfra PostgreSQL role",
        role="pyinfra",
        password="somepassword3",
        superuser=True,
        createdb=True,
        login=True,
        _sudo=True,
        _sudo_user="postgres",
    )
