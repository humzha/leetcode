class StockSpanner:
    """Monotonic stack-based stock span calculator.

    Collects daily price quotes and returns the span (number of consecutive
    days the price was <= today's price going backward) for each day's price.
    """

    def __init__(self):
        # Your implementation here
        self.stack = []
        pass

    def next(self, price: int) -> int:
        # Your implementation here
        # 100, 80 price = 60
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, 1))
        # 100, 80, price = 80, 81
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, popped_span = self.stack.pop()
            span += popped_span
        self.stack.append(price, span)
        return self.stack[-1][1]