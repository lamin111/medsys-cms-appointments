from dataclasses import dataclass
from datetime import datetime, timedelta

CLINIC_OPEN, CLINIC_CLOSE, SLOT_MINUTES = 9, 17, 30

@dataclass
class Appointment:
    patient_id: str
    doctor_id: str
    start: datetime

class ScheduleConflictError(Exception):
    pass

class Scheduler:
    def __init__(self):
        self._appointments = []

    def book(self, patient_id, doctor_id, start):
        if not (CLINIC_OPEN <= start.hour < CLINIC_CLOSE):
            raise ValueError("Outside clinic hours.")
        if start.minute % SLOT_MINUTES != 0:
            raise ValueError("Must start on a 30-minute boundary.")
        for a in self._appointments:
            if a.doctor_id == doctor_id and a.start == start:
                raise ScheduleConflictError(f"{doctor_id} already booked at {start}.")
        appt = Appointment(patient_id, doctor_id, start)
        self._appointments.append(appt)
        return appt
