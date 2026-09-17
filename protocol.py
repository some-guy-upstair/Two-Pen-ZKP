from prover import Prover
from verifier import Verifier


class Two_Pen_Protocol:
    def __init__(self, color1, color2):
        self.prover = Prover(color1, color2)
        self.verifier = Verifier()

    def run_round(self, round_number):
        print(f"\nRound {round_number}")
        print("-" * 20)

        # Initial positions of the pens
        pen1 = self.prover.pen1_color
        pen2 = self.prover.pen2_color

        print("B places the pens.")

        # A observes the initial arrangement
        self.prover.observe(pen1, pen2)

        # B secretly chooses whether to switch
        challenge = self.verifier.choose_challenge()

        # B performs the challenge
        pen1, pen2 = self.verifier.perform_challenge(pen1, pen2)

        # A answers
        answer = self.prover.answer(pen1, pen2)

        # B verifies the answer
        correct = self.verifier.verify(answer)

        if answer:
            answer_text = "switched"
        else:
            answer_text = "did not switch"

        print(f"A: B {answer_text} the pens.")

        if correct:
            print("✓ Correct")
        else:
            print("✗ Incorrect")

        return correct

    def run(self, rounds):
        successful_rounds = 0

        for round_number in range(1, rounds + 1):
            if self.run_round(round_number):
                successful_rounds += 1

        print("\n" + "=" * 30)
        print("Proof complete!")
        print("=" * 30)

        print(
            f"A passed {successful_rounds}/{rounds} rounds."
        )

        return successful_rounds == rounds