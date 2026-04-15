from datetime import datetime
from typing import List
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False
        for member in self.crew:
            if member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                has_leader = True
                break

        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experience_count = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            if experience_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need at least 50% experienced crew"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 6, 15, 8, 0, 0),
        duration_days=900,
        crew=[
            {
                "member_id": "CM001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 42,
                "specialization": "Mission Command",
                "years_experience": 15,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 8,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 6,
                "is_active": True,
            },
        ],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )

    print("=" * 41)

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime(2024, 7, 1, 10, 0, 0),
            duration_days=100,
            crew=[
                {
                    "member_id": "CM010",
                    "name": "Bob Lee",
                    "rank": "officer",
                    "age": 29,
                    "specialization": "Engineering",
                    "years_experience": 4,
                    "is_active": True,
                }
            ],
            budget_millions=500.0,
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
