import random

class Verifier:
    def __init__(self):
        self.switched = False

    def choose_challenge(self):
        '''
        Randomly decide whether to switch the pens

        False = don't switch
        True = switch
        '''
        self.switched = random.choice([True, False])
        return self.switched

    def perform_challenge(self, pen1, pen2):
        '''
        Perform the chosen action
        '''

        # If the position is switched
        if self.switched:
            return pen2, pen1
        return pen1, pen2 # does not switch

    def verify(self, answer):
        '''
        Check whether the prover correctly identify whether
        the pens were switched
        '''
        return answer == self.switched