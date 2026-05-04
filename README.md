# 🏥 Hospital Bed Availability Decision System

## Project Title
**Hospital Bed Availability Decision System**

## Group Members
| Name | | Role |
|------| |------|
| [Dilshod Fayzullayev ] | Logic Designer |
| [Ibroximov Axmadjon] | CircuitVerse Designer |
| [Ibrohim Saidov] | Python Developer |
| [Timur Suyunov] | Documentation Lead |
| [Temur Yangibaev] | Presenter |
## Course
**EEE120 – Digital Design Fundamentals**

## Instructor
[Rajan Tripathi]

---

## Problem Statement
Hospitals often face complex decisions when admitting patients, especially during high-demand periods. Manual decision-making can be inconsistent or slow. This system uses **combinational digital logic** to automate the admission decision based on four key factors, ensuring fast, fair, and consistent outcomes.

---

## Inputs (4 Binary Inputs)

| Symbol | Input Name | Description |
|--------|-----------|-------------|
| **B** | Bed Available | Is a hospital bed currently free? (1=Yes, 0=No) |
| **E** | Emergency Case | Is the patient classified as an emergency? (1=Yes, 0=No) |
| **D** | Doctor Approval | Has a doctor approved the admission? (1=Yes, 0=No) |
| **P** | Payment Cleared | Is insurance or payment confirmed? (1=Yes, 0=No) |

---

## Outputs (3 Outputs)

| Output | Meaning |
|--------|---------|
| **ADMIT** | Patient is assigned a bed immediately |
| **WAITLIST** | Patient is queued and monitored |
| **REJECT/REFER** | Patient is directed to another facility |

---

## Digital Logic Explanation

### Boolean Expressions

```
ADMIT    = B · D · (E + P)

WAITLIST = (B · D · E' · P') + (B · D' · E)

REJECT   = ADMIT' · WAITLIST'
```

### Logic Rules in Plain English

1. **ADMIT** if: a bed is available **AND** doctor approved **AND** (it is an emergency **OR** payment is cleared)
2. **WAITLIST** if: a bed is available AND doctor approved AND neither emergency nor payment (wait for payment), OR bed is available AND no doctor approval yet but it IS an emergency (urgent, awaiting doctor)
3. **REJECT/REFER** everything else — no bed available or insufficient approvals for a non-emergency

### Gate Count
The circuit uses **AND, OR, NOT** gates:
- NOT gates: 2 (for E' and P')
- AND gates: 4
- OR gates: 3
- Total: **≥ 9 logic gates** ✅

---

## Truth Table

| B | E | D | P | ADMIT | WAITLIST | REJECT |
|---|---|---|---|-------|----------|--------|
| 0 | 0 | 0 | 0 |   0   |    0     |   1    |
| 0 | 0 | 0 | 1 |   0   |    0     |   1    |
| 0 | 0 | 1 | 0 |   0   |    0     |   1    |
| 0 | 0 | 1 | 1 |   0   |    0     |   1    |
| 0 | 1 | 0 | 0 |   0   |    0     |   1    |
| 0 | 1 | 0 | 1 |   0   |    0     |   1    |
| 0 | 1 | 1 | 0 |   0   |    0     |   1    |
| 0 | 1 | 1 | 1 |   0   |    0     |   1    |
| 1 | 0 | 0 | 0 |   0   |    0     |   1    |
| 1 | 0 | 0 | 1 |   0   |    0     |   1    |
| 1 | 0 | 1 | 0 |   0   |    1     |   0    |
| 1 | 0 | 1 | 1 |   1   |    0     |   0    |
| 1 | 1 | 0 | 0 |   0   |    1     |   0    |
| 1 | 1 | 0 | 1 |   0   |    1     |   0    |
| 1 | 1 | 1 | 0 |   1   |    0     |   0    |
| 1 | 1 | 1 | 1 |   1   |    0     |   0    |

> **Summary:** 4 ADMIT cases · 3 WAITLIST cases · 9 REJECT cases

---

## CircuitVerse Link
> 🔗 https://circuitverse.org/users/426743/projects/hospital-f7023259-0d82-4910-a167-e43c10679932

### Circuit Design Notes (for CircuitVerse builder)
Build the following subcircuits:
1. **ADMIT gate**: `AND(B, D, OR(E, P))`
2. **WAITLIST gate**: `OR( AND(B,D,NOT(E),NOT(P)), AND(B,NOT(D),E) )`
3. **REJECT gate**: `AND(NOT(ADMIT), NOT(WAITLIST))` — or use NOR/logic complement
4. Label all inputs and outputs clearly
5. Use different wire colors for each output path

---

## Python Program Explanation

`src/main.py` implements the same Boolean logic in Python with three modes:

| Mode | Description |
|------|-------------|
| **Manual Check** | User enters 4 inputs → system outputs the decision + logic trace |
| **Truth Table** | Generates and prints all 16 input combinations |
| **Test Cases** | Runs 11 predefined test cases and reports pass/fail |

The logic functions directly mirror the gate equations:
```python
admit    = bed and doctor and (emergency or payment)
waitlist = (bed and doctor and not emergency and not payment) \
         or (bed and not doctor and emergency)
reject   = not admit and not waitlist
```

---

## How AI/LLM Was Used

| Task | AI Used? | Notes |
|------|----------|-------|
| Deriving Boolean expressions | Partial | AI suggested the ADMIT formula; team verified and extended it for WAITLIST |
| Python code structure | Partial | AI generated initial function skeleton; team added truth table and test cases |
| README template | Yes | AI generated structure; team filled in all project-specific details |
| CircuitVerse circuit | No | Built manually by CircuitVerse Designer |
| Presentation slides | No | Designed by team |

> All AI-assisted code was reviewed, tested, and understood by the group. Each member can explain their section.

---

## How to Run the Python Code

**Requirements:** Python 3.6+

```bash
# Clone the repo
git clone https: https://github.com/fel1xzbeast-art/EEE120_Final_Project_5_HBADSP
cd EEE120_Final_Project

# Run the program
python src/main.py
```

No external libraries required — uses only Python built-ins.

---

## Screenshots

| File | Description |
|------|-------------|
| `screenshots/circuit_design.png` | CircuitVerse circuit screenshot |
| `screenshots/python_output.png` | Python terminal output screenshot |
| `screenshots/truth_table_output.png` | Truth table from Python |

---

## Future Improvements

1. **Priority queue logic** — Add a sequential counter/register to track and order the waitlist
2. **ICU vs. general ward** — Add a second bed-type input to differentiate critical care
3. **GUI interface** — Build a Tkinter or web-based front end for hospital staff
4. **Database integration** — Connect to a real bed-management database
5. **Flip-flop memory** — Add a D flip-flop in CircuitVerse to remember the last 5 admission states
6. **SMS/alert output** — Extend Python to send WhatsApp/email notifications on admission

---

*EEE120 Final Project — Digital Design Fundamentals*
