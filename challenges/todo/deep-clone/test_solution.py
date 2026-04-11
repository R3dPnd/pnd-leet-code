import unittest
from solution import deep_clone


class TestDeepClone(unittest.TestCase):

    # --- primitives ---

    def test_int(self):
        self.assertEqual(deep_clone(42), 42)

    def test_string(self):
        self.assertEqual(deep_clone("hello"), "hello")

    def test_none(self):
        self.assertIsNone(deep_clone(None))

    def test_bool(self):
        self.assertEqual(deep_clone(True), True)

    # --- list ---

    def test_list_is_new_object(self):
        original = [1, 2, 3]
        clone = deep_clone(original)
        self.assertEqual(clone, original)
        self.assertIsNot(clone, original)

    def test_nested_list(self):
        original = [1, [2, [3]]]
        clone = deep_clone(original)
        clone[1][1][0] = 99
        self.assertEqual(original[1][1][0], 3)

    # --- dict ---

    def test_dict_is_new_object(self):
        original = {"a": 1, "b": 2}
        clone = deep_clone(original)
        self.assertEqual(clone, original)
        self.assertIsNot(clone, original)

    def test_nested_dict(self):
        original = {"x": {"y": {"z": 0}}}
        clone = deep_clone(original)
        clone["x"]["y"]["z"] = 99
        self.assertEqual(original["x"]["y"]["z"], 0)

    def test_dict_with_list_value(self):
        original = {"nums": [1, 2, 3]}
        clone = deep_clone(original)
        clone["nums"].append(4)
        self.assertEqual(original["nums"], [1, 2, 3])

    # --- set ---

    def test_set_is_new_object(self):
        original = {1, 2, 3}
        clone = deep_clone(original)
        self.assertEqual(clone, original)
        self.assertIsNot(clone, original)

    # --- tuple ---

    def test_tuple_contents_are_cloned(self):
        inner = [1, 2]
        original = (inner,)
        clone = deep_clone(original)
        self.assertIsInstance(clone, tuple)
        self.assertIsNot(clone[0], inner)

    # --- circular references ---

    def test_circular_list(self):
        a = [1, 2]
        a.append(a)  # circular
        clone = deep_clone(a)
        self.assertIsNot(clone, a)
        self.assertIs(clone[2], clone)  # clone points to itself

    def test_circular_dict(self):
        d = {"val": 1}
        d["self"] = d
        clone = deep_clone(d)
        self.assertIsNot(clone, d)
        self.assertIs(clone["self"], clone)

    def test_shared_reference_preserved(self):
        inner = [1, 2, 3]
        original = {"a": inner, "b": inner}
        clone = deep_clone(original)
        # both keys should point to the SAME cloned list
        self.assertIs(clone["a"], clone["b"])
        # but not the original
        self.assertIsNot(clone["a"], inner)


if __name__ == "__main__":
    unittest.main()
