class ProductOfNumbers:
    def __init__(self):
        self.nums = []
        self.prods = {}
        self.zero_idx = -1

    def add(self, num: int) -> None:
        self.nums.append(num)

        length = len(self.nums)

        if num == 0:
            self.zero_idx = length - 1

        if self.prods:
            limit = length - 1
            self.prods = {
                k: prod // self.nums[limit - k] * num
                for k, prod in self.prods.items()
                if self.nums[limit - k] != 0
            }

    def _getProductHelper(self, k: int, idx: int) -> int:
        length = len(self.nums)

        if k in self.prods:
            return self.prods[k]

        if self.zero_idx != -1 and k >= length - self.zero_idx:
            self.prods[k] = 0
            return 0

        if idx >= length:
            return 1

        if k == 1:
            val = self.nums[idx]
            self.prods[k] = val
            return val

        prod = self._getProductHelper(k - 1, idx + 1) * self.nums[idx]
        self.prods[k] = prod
        return prod

    def getProduct(self, k: int) -> int:
        idx = len(self.nums) - k
        return self._getProductHelper(k, idx)


if __name__ == "__main__":
    ops = [
        "ProductOfNumbers",
        "add",
        "add",
        "add",
        "add",
        "add",
        "getProduct",
        "getProduct",
        "getProduct",
        "add",
        "getProduct",
    ]
    inputs = [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]

    p_n = ProductOfNumbers()

    for op, ips in zip(ops[1:], inputs[1:]):
        method = getattr(p_n, op)
        print(method(*ips))

    ops = [
        "ProductOfNumbers",
        "add",
        "add",
        "add",
        "add",
        "getProduct",
        "add",
        "getProduct",
    ]
    inputs = [[], [3], [0], [2], [5], [3], [8], [3]]

    p_n = ProductOfNumbers()

    for op, ips in zip(ops[1:], inputs[1:]):
        method = getattr(p_n, op)
        print(method(*ips))
