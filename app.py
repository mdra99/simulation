from src import state, funcs
from src.patient import Patient
import src.headers as h

try:
    f = open("log.txt", "w")
    f.close()
except:
    pass

f = open("log.txt", "w")

while True:
    state.FEL = sorted(state.FEL, key=lambda event: event[h.Type])
    state.FEL = sorted(state.FEL, key=lambda event: event[h.Time])
    current_event = state.FEL.pop(0)

    if state.NR + state.NS > 2:
        print(f"NR: {state.NR} NS: {state.NS} at time {current_event[h.Time]}")

    if current_event[h.Time] > state.SimulationEndTime:
        break

    state.TR = sorted(state.TR)

    if current_event[h.Type] == h.Arrival:
        patient = Patient(current_event[h.Time])
        funcs.Arrival(patient, current_event[h.Time])
        f.write(f"{current_event[h.Type]} of {patient} of type {patient.priority} at time {current_event[h.Time]}\n")
        f.write(f"NS: {state.NS}, NR: {state.NR}, Q3: {len(state.Q3)}, Q2: {len(state.Q2)}, Q1: {len(state.Q1)}\n\n")
        continue
    
    elif current_event[h.Type] == h.Departure:
        funcs.Departure(current_event[h.Patient], current_event[h.Time])
        f.write(f"{current_event[h.Type]} of {current_event[h.Patient]} of type {current_event[h.Patient].priority} at time {current_event[h.Time]}\n")
        f.write(f"NS: {state.NS}, NR: {state.NR}, Q3: {len(state.Q3)}, Q2: {len(state.Q2)}, Q1: {len(state.Q1)}\n\n")
        continue
    
    elif current_event[h.Type] == h.RestAlert:
        funcs.RestAlert(current_event[h.Time])
        f.write(f"{current_event[h.Type]} at time {current_event[h.Time]}\n")
        f.write(f"NS: {state.NS}, NR: {state.NR}, Q3: {len(state.Q3)}, Q2: {len(state.Q2)}, Q1: {len(state.Q1)}\n\n")
        continue 
    
    elif current_event[h.Type] == h.SoR:
        funcs.SoR(current_event[h.Time]) 
        f.write(f"{current_event[h.Type]} at time {current_event[h.Time]}\n")
        f.write(f"NS: {state.NS}, NR: {state.NR}, Q3: {len(state.Q3)}, Q2: {len(state.Q2)}, Q1: {len(state.Q1)}\n\n")
        continue
    
    elif current_event[h.Type] == h.EoR:
        funcs.EoR(current_event[h.Time])
        f.write(f"{current_event[h.Type]} at time {current_event[h.Time]}\n")
        f.write(f"NS: {state.NS}, NR: {state.NR}, Q3: {len(state.Q3)}, Q2: {len(state.Q2)}, Q1: {len(state.Q1)}\n\n")
        continue 
    
    else:
        raise Exception(f"Event {current_event} is invalid")

f.close()