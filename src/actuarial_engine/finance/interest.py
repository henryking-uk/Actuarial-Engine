class Interest:
    def __init__(self, rate):
        self.rate = rate

        if self.rate <= -1:
            raise ValueError("Interest rate must be greater than -1")

    def discount_factor(self, t):
        """Present value factor for a payment t years in the future."""
        return 1/(1+ self.rate)**t

    def accumulation_factor(self, t):
        """Accumulation factor for an investment held for t years."""
        return (1+ self.rate)**t
    
    def discount_rate(self):
        """Effective annual discount rate corresponding to the interest rate."""
        return self.rate/(1 + self.rate)