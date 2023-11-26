class SimplifiedEnum(type):
    def __new__(cls, name, bases, attrs):
        if '__keys' in attrs:
            keys = attrs['__keys']
            new_attrs = {key: key for key in keys}
            attrs.update(new_attrs)
        return super().__new__(cls, name, bases, attrs)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    def __getattr__(self, name):
        return name


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")

    def __getattr__(self, name):
        return name


sizes_enum = SizesEnum()
colors_enum = ColorsEnum()

assert colors_enum.RED == "RED"
assert sizes_enum.XL == "XL"
