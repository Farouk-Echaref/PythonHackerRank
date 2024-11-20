# resource:

* https://realpython.com/python-json/#deserializing-json

# notes:

* Deserialization is not the exact reverse of the serialization process. The reason for this is that JSON keys are always strings, and not all Python data types can be converted to JSON data types. This discrepancy means that certain Python objects may not retain their original type when serialized and then deserialized.