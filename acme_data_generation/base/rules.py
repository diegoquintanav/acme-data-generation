from collections import defaultdict
from functools import partial


data_modifier = lambda: None

# empty placeholder for now. It will return False for any rule passed to the dict
# False means that the rule is not enforced.
# e.g. rules['R13'] == False
mapping = defaultdict(lambda: False)

# fmt: off
m = {
    "R1": {"desc" : "workPackageID is an identifier of WorkPackage.", "data_modifier": data_modifier},
    "R2": {"desc" : "workOrderID is an identifier of WorkOrders/ForecastedOrders/TechnicalLogBookOrders.", "data_modifier": data_modifier},
    "R3": {"desc" : "maintenanceID is an identifier of MaintenanceEvents/OperationInterruption.", "data_modifier": data_modifier},
    "R4": {"desc" : "file is an identifier of Attachments.", "data_modifier": data_modifier},
    "R5": {"desc" : "event of an Attachement is a reference to maintenanceID of MaintenanceEvents.", "data_modifier": data_modifier},
    "R6": {"desc" : "subsystem of MaintenanceEvents should be a 4 digits ATA code. See ATA codes for commercial aircrafts in <https://en.wikipedia.org/wiki/ATA_100>", "data_modifier": data_modifier},
    "R7": {"desc" : "delayCode of OperationInterruption should be a 2 digits IATA code. See <https://en.wikipedia.org/wiki/IATA_delay_codes>", "data_modifier": data_modifier},
    "R8": {"desc" : "workPackageID/workOrderID/maintenanceID should be simply SERIAL numbers generated by an autoincrement mechanism. See <https://www.postgresql.org/docs/9.1/datatype-numeric.html#DATATYPE-NUMERIC-TABLE> for details.", "data_modifier": data_modifier},
    "R9": {"desc" : "ReportKind values “PIREP” and “MAREP” refer to pilot and maintenance personnel as reporters, respectively.", "data_modifier": data_modifier},
    "R10": {"desc" : "MELCathegory values A,B,C,D refer to 3,10,30,120 days of allowed delay in the repairing of the problem in the aircraft, respectively.", "data_modifier": data_modifier},
    "R11": {"desc" : "airport in MaintenanceEvents must have a value.", "data_modifier": data_modifier},
    "R12": {"desc" : "In OperationInterruption, departure must coincide with the date of the flightID (see bellow how it is composed).", "data_modifier": data_modifier},
    "R13": {"desc" : "The flight registered in OperationInterruption, must exist in the Flights of AIMS database, and be marked as “delayed” (i.e., delayCode is not null) with the same IATA delay code.", "data_modifier": data_modifier},
    "R14": {"desc" : "In MaintenanceEvents, the events of kind Maintenance that correspond to a Revision, are those of the same aircraft whose interval is completely included in that of the Revision. For all of them, the airport must be the same. o In MaintenanceEvents, the events of kind Maintenance cannot partially intersect that of a Revision of the same aircraft.", "data_modifier": data_modifier},
    "R15": {"desc" : "In MaintenanceEvents, maintenance duration must have the expected length according to the kind of maintenance:", "data_modifier": data_modifier},
    "R15-A": {"desc" : "Delay – minutes", "data_modifier": data_modifier},
    "R15-B": {"desc" : "Safety – undetermined/unlimited,", "data_modifier": data_modifier},
    "R15-C": {"desc" : "AircraftOnGround – hours", "data_modifier": data_modifier},
    "R15-D": {"desc" : "Maintenance – hours to max 1 day", "data_modifier": data_modifier},
    "R15-E": {"desc" : "Revision – days to 1 month", "data_modifier": data_modifier},
    "R16": {"desc" : "flightID is an identifier of Flights.", "data_modifier": data_modifier},
    "R17": {"desc" : "flightID is derived by concatenating the following values: Date-Origin-Destination-FlightNumber-AircraftRegistration (lengths: 6+1+3+1+3+1+4+1+6=26).", "data_modifier": data_modifier},
    "R18": {"desc" : "delayCode in OperationInterruption is a 2 digits IATA code 2", "data_modifier": data_modifier},
    "R19": {"desc" : "In a Slot, scheduledArrival must be posterior to the scheduledDeparture.", "data_modifier": data_modifier},
    "R20": {"desc" : "Two Slots of the same aircraft cannot overlap.", "data_modifier": data_modifier},
    "R21": {"desc" : "In Flights, departure and arrival airports must be those in the flightID (unless this flight has been diverted).", "data_modifier": data_modifier},
    "R22": {"desc" : "In a Flight, actualArrival is posterior to actualDeparture.", "data_modifier": data_modifier},
    "R23": {"desc" : "In a Maintenance, the corresponding events must exist in AMOS inside the corresponding time interval."}, "data_modifier": data_modifier,}

for rule, dikt in m.items():
    mapping[rule] = dikt


def data_modifier(rule=None, prob=1):
    return None
