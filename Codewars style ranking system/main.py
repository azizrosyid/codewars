class User():
    rankTier = [x for x in range(-8, 9) if x != 0]

    def __init__(self):
        self.rankIndex = 0
        self.rank = self.rankTier[self.rankIndex]
        self.progress = 0

    def inc_progress(self, increment):
        tierIncrement = self.rankTier.index(increment)
        if tierIncrement == self.rankIndex:
            self.progress += 3
        elif tierIncrement == self.rankIndex - 1:
            self.progress += 1
        elif tierIncrement > self.rankIndex:
            self.progress += ((tierIncrement-self.rankIndex))**2 * 10
        if self.progress >= 100:
            rankUp, self.progress = divmod(self.progress, 100)
            self.rankIndex += rankUp
            if self.rankIndex >= 15:
                self.rankIndex = 15
            self.rank = self.rankTier[self.rankIndex]
        if self.rank == 8:
            self.progress = 0
            