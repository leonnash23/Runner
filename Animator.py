class Animator:
    def __init__(self, bitmaps, time=50):
        self.bitmaps = bitmaps
        self.time = time
        self.work_time = 0
        self.skip = 0
        self.frame = 0

    def update(self, dt):
        self.work_time += dt
        self.skip = self.work_time // self.time
        if self.skip > 0:
            self.work_time %= self.time
            self.frame += self.skip
            if self.frame >= len(self.bitmaps):
                self.frame = 0

    def getImg(self):
        return self.bitmaps[self.frame]
