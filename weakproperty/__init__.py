from weakref import ref


class weakproperty:
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
            ref(value)
        )

    def __delete__(self, instance):
        try:
            delattr(
                instance,
                self.ref_name
            )

        except AttributeError:
            pass

    def __set_name__(self, owner, name):
        self.ref_name = name

