class C2dv:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return (f'{self.icap}i + {self.jcap}j')


class C3dv(C2dv):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return (f'{self.icap}i + {self.jcap}j + {self.kcap}k')


v2d = C2dv(1, 2)
v3d = C3dv(1, 2, 3)
print(v2d)
print(v3d)
