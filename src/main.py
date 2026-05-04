"""
Hospital Bed Availability Decision System
EEE120 Digital Design Fundamentals - Final Project
========================================================
This program simulates the combinational logic circuit for
hospital patient admission decisions.

Boolean Logic:
  ADMIT        = BED AND DOCTOR AND (EMERGENCY OR PAYMENT)
  WAITLIST     = BED AND DOCTOR AND NOT(EMERGENCY OR PAYMENT)
               OR BED AND NOT(DOCTOR) AND EMERGENCY
  REJECT_REFER = NOT(BED) AND NOT(EMERGENCY)
               OR NOT(BED) AND NOT(DOCTOR)

Simplified:
  ADMIT        = B AND D AND (E OR P)
  WAITLIST     = (B AND D AND NOT E AND NOT P)
               OR (B AND NOT D AND E)
  REJECT_REFER = NOT ADMIT AND NOT WAITLIST
"""

def admission_decision(bed: bool, emergency: bool, doctor: bool, payment: bool):
    """
    Evaluates admission status using combinational logic.
    
    Inputs:
        bed       (B) - Hospital bed is available
        emergency (E) - Patient is an emergency case
        doctor    (D) - Doctor has given approval
        payment   (P) - Insurance/payment is cleared

    Returns:
        tuple: (admit: bool, waitlist: bool, reject: bool)
    """
    admit    = bed and doctor and (emergency or payment)
    waitlist = (bed and doctor and not emergency and not payment) \
             or (bed and not doctor and emergency)
    reject   = not admit and not waitlist

    return admit, waitlist, reject


def get_status_label(admit, waitlist, reject):
    if admit:
        return "✅ ADMIT PATIENT"
    elif waitlist:
        return "⏳ WAITLIST PATIENT"
    else:
        return "❌ REJECT / REFER PATIENT"


def get_bool_input(prompt: str) -> bool:
    """Helper to get a Yes/No boolean from the user."""
    while True:
        val = input(f"  {prompt} (y/n): ").strip().lower()
        if val in ("y", "yes", "1", "true"):
            return True
        if val in ("n", "no", "0", "false"):
            return False
        print("  ⚠  Please enter y or n.")


def print_separator(char="─", width=55):
    print(char * width)


def print_header():
    print_separator("═")
    print("  🏥  HOSPITAL BED AVAILABILITY DECISION SYSTEM")
    print("  EEE120 Digital Design Fundamentals")
    print_separator("═")


def run_manual_check():
    """Interactive single patient admission check."""
    print("\n  Enter patient details:\n")
    bed       = get_bool_input("Bed available?              ")
    emergency = get_bool_input("Emergency case?             ")
    doctor    = get_bool_input("Doctor approval?            ")
    payment   = get_bool_input("Insurance/payment cleared?  ")

    admit, waitlist, reject = admission_decision(bed, emergency, doctor, payment)
    status = get_status_label(admit, waitlist, reject)

    print()
    print_separator()
    print("  INPUTS SUMMARY")
    print_separator()
    print(f"  Bed Available (B)       : {'YES' if bed       else 'NO'}")
    print(f"  Emergency Case (E)      : {'YES' if emergency else 'NO'}")
    print(f"  Doctor Approval (D)     : {'YES' if doctor    else 'NO'}")
    print(f"  Payment Cleared (P)     : {'YES' if payment   else 'NO'}")
    print_separator()
    print(f"  DECISION  →  {status}")
    print_separator()

    # Show active logic path
    print("\n  LOGIC TRACE")
    print(f"  ADMIT    = B·D·(E+P) = {int(bed)}·{int(doctor)}·({int(emergency)}+{int(payment)}) = {int(admit)}")
    print(f"  WAITLIST = B·D·E'·P' OR B·D'·E")
    wl1 = bed and doctor and not emergency and not payment
    wl2 = bed and not doctor and emergency
    print(f"           = {int(bed)}·{int(doctor)}·{int(not emergency)}·{int(not payment)} OR "
          f"{int(bed)}·{int(not doctor)}·{int(emergency)} = {int(wl1)} OR {int(wl2)} = {int(waitlist)}")
    print(f"  REJECT   = NOT ADMIT AND NOT WAITLIST = {int(reject)}")
    print()


def run_truth_table():
    """Prints the full 16-row truth table for all input combinations."""
    print()
    print_separator()
    print("  FULL TRUTH TABLE  (B=Bed, E=Emergency, D=Doctor, P=Payment)")
    print_separator()
    print(f"  {'B':>2} {'E':>2} {'D':>2} {'P':>2}  │  {'ADMIT':>5}  {'WAIT':>4}  {'REJECT':>6}  │  Decision")
    print_separator()

    outcomes = {"ADMIT": 0, "WAITLIST": 0, "REJECT": 0}

    for i in range(16):
        b = bool((i >> 3) & 1)
        e = bool((i >> 2) & 1)
        d = bool((i >> 1) & 1)
        p = bool(i & 1)

        admit, waitlist, reject = admission_decision(b, e, d, p)

        if admit:
            label = "ADMIT"
            outcomes["ADMIT"] += 1
        elif waitlist:
            label = "WAITLIST"
            outcomes["WAITLIST"] += 1
        else:
            label = "REJECT"
            outcomes["REJECT"] += 1

        print(f"  {int(b):>2} {int(e):>2} {int(d):>2} {int(p):>2}  │  "
              f"{int(admit):>5}  {int(waitlist):>4}  {int(reject):>6}  │  {label}")

    print_separator()
    print(f"  Summary → ADMIT: {outcomes['ADMIT']}  WAITLIST: {outcomes['WAITLIST']}  REJECT: {outcomes['REJECT']}")
    print()


def run_batch_test():
    """Runs predefined test cases to verify the logic."""
    test_cases = [
        # (bed, emergency, doctor, payment, expected)
        (True,  True,  True,  True,  "ADMIT"),
        (True,  True,  True,  False, "ADMIT"),
        (True,  False, True,  True,  "ADMIT"),
        (True,  False, True,  False, "WAITLIST"),
        (True,  True,  False, True,  "WAITLIST"),
        (True,  True,  False, False, "WAITLIST"),
        (True,  False, False, True,  "REJECT"),
        (True,  False, False, False, "REJECT"),
        (False, True,  True,  True,  "REJECT"),
        (False, False, True,  True,  "REJECT"),
        (False, False, False, False, "REJECT"),
    ]

    print()
    print_separator()
    print("  AUTOMATED TEST CASES")
    print_separator()
    print(f"  {'B':>2} {'E':>2} {'D':>2} {'P':>2}  │  Expected    │  Got         │  Status")
    print_separator()

    passed = 0
    for b, e, d, p, expected in test_cases:
        admit, waitlist, reject = admission_decision(b, e, d, p)
        if admit:
            got = "ADMIT"
        elif waitlist:
            got = "WAITLIST"
        else:
            got = "REJECT"

        ok = got == expected
        status_icon = "✅ PASS" if ok else "❌ FAIL"
        if ok:
            passed += 1

        print(f"  {int(b):>2} {int(e):>2} {int(d):>2} {int(p):>2}  │  {expected:<12}│  {got:<12}│  {status_icon}")

    print_separator()
    print(f"  Results: {passed}/{len(test_cases)} tests passed")
    print()


def main():
    print_header()

    while True:
        print("\n  MAIN MENU")
        print_separator()
        print("  1. Check single patient admission")
        print("  2. View full truth table")
        print("  3. Run automated test cases")
        print("  4. Exit")
        print_separator()
        choice = input("  Select option (1–4): ").strip()

        if choice == "1":
            run_manual_check()
        elif choice == "2":
            run_truth_table()
        elif choice == "3":
            run_batch_test()
        elif choice == "4":
            print("\n  Goodbye. Stay healthy! 🏥\n")
            break
        else:
            print("  ⚠  Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
