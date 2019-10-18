import weakref


class weakproperty:
    def __init__(self):
        self.ref_name = f'[{id(self)}_ref]'

    def __get__(self, instance, owner):
        return getattr(
            instance,
            self.ref_name,
            lambda: None
        )()

    def __set__(self, instance, value):
        setattr(
            instance,
            self.ref_name,
            weakref.ref(value)
        )
