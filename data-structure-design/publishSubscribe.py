class EventBus:
    def __init__(self):
        self.events = []

    def publish(self):
        for observer in self.events:
            observer.update()

    def subscribe(self, observer):
        self.events.append(observer)


class Observer:
    def __init__(self, number):
        self.number = number

    def update(self):
        print(f'adding: {self.number}')


class FireDispatch(Observer):
    def update(self):
        print(f'adding fire dispatch: fire {self.number}')


class PoliceDispatch(Observer):
    def update(self):
        print(f'adding police dispatch: police {self.number}')


if __name__ == '__main__':
    eb = EventBus()

    obs1 = FireDispatch('817-555-1234')
    obs2 = PoliceDispatch('817-555-4321')
    obs3 = FireDispatch('214-555-2121')

    eb.subscribe(obs1)
    eb.subscribe(obs2)
    eb.subscribe(obs3)

    # notify all subscribers
    eb.publish()