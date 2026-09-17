from protocol import Two_Pen_Protocol

def main():
    print("Two-Pen ZKP")
    print("--------------------\n")
    print("A has two different colored pens. (Prover)")
    print("B does not know their colors. (Verifier)")

    print("\nProtocol: B randomly switches or does not switch the pens, A identifies what happened.")
    print("\nGoal: A want to prove to B that he knows the colors of the pens.")

    protocol = Two_Pen_Protocol(color1="red", color2="blue")

    # Rounds can be set to whatever, the higher it is, the less likely cheating can occur and
    # that A does actually know the colors
    protocol.run(rounds=10) 

if __name__ == "__main__":
    main()