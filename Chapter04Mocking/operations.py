class multiply:
    def __init__(self, *operands):
        self.operands = operands

    def evaluate(self, bindings):
        vals = [x.evaluate(bindings) for x in self.operands]

        if len(vals) < 2:
            raise ValueError('multiply without at least two ' + \
                                'operands is meaningless')

        result = 1.0

        for val in vals:
            result *= val

        return result
    # whatever just trying to get this to work.
    # making a change here on my home pc to see if I can get this to push