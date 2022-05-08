import bisect


class SORTracker:
    def __init__(self):
        self.data = []
        self.i = -1

    def add(self, name, score):
         bisect.insort(self.data, (-score, name))

    def get(self):
        self.i += 1
        return self.data[self.i][1]


if __name__ == '__main__':
    st = SORTracker()
    st.add('bradford', 2)
    st.add('branford', 3)
    print(st.get()) # branford
    st.add('alps', 2)
    print(st.get()) # alps