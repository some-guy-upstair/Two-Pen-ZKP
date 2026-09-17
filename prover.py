class Prover:
    def __init__(self, pen1_color, pen2_color):
        self.pen1_color = pen1_color
        self.pen2_color = pen2_color

    def observe(self, pen1, pen2):
        '''
        The current colors at each position
        '''
        self.position1_color = pen1
        self.position2_color = pen2

    def answer(self, pen1, pen2):
        '''
        Determine whether the pens were switched
        
        If the color at position 1 changed, that means the pens were switched
        '''
        if pen1 == self.position1_color and pen2 == self.position2_color:
            return False
        elif pen1 == self.position2_color and pen2 == self.position1_color:
            return True