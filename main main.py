from importlib import import_module


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"""Книга "{self.name}\""""

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == "__main__":
    obj = Book(1, "test_name_1", 200)
    obj_1 = Book(2, "test_name_2", 400)

    print(Book.__str__(obj))
    print(Book.__str__(obj_1))
    print(f"[{Book.__repr__(obj)}, {Book.__repr__(obj_1)}]")
