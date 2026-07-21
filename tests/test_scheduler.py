from datetime import datetime
import pytest
from app.scheduler import Scheduler, ScheduleConflictError

DAY = datetime(2026, 8, 3)


def test_double_booking_rejected():
    s = Scheduler()
    s.book("P1", "DR1", DAY.replace(hour=10))
    with pytest.raises(ScheduleConflictError):
        s.book("P2", "DR1", DAY.replace(hour=10))


def test_outside_hours_rejected():
    s = Scheduler()
    with pytest.raises(ValueError):
        s.book("P1", "DR1", DAY.replace(hour=20))
