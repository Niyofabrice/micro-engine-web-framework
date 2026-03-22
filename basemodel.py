
class ModelMetaClass(type):
    def __new__(cls, name, bases, dict):
        fields = {k: v for k, v in dict.items() if not k.startswith("__")}
        new_class = super().__new__(cls, name, bases, dict)
        new_class._fields = fields
        new_class._table_name = name.lower() + "s"
        return new_class

class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
         for k, v in kwargs.items():
              setattr(self, k, v)

    def save(self):
        columns = []
        values = []

        for field_name in self._fields:
            columns.append(field_name)
            val = getattr(self, field_name, None)
            values.append(f"'{val}'" if isinstance(val, str) else str(val))
        sql = f"INSERT INTO {self._table_name}({', '.join(columns)}) VALUES({', '.join(values)});"
        print(f"EXECUTING SQL: {sql}")
