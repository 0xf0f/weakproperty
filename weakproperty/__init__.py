import weakref


class weakproperty:
    def __get__(self, instance, owner):
        return getattr(
            instance,
            f'{id(self)}_ref',
            lambda: None
        )()

    def __set__(self, instance, value):
        setattr(
            instance,
            f'{id(self)}_ref',
            weakref.ref(value)
        )
