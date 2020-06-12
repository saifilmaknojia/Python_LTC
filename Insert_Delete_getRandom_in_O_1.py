import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tracker_map = {}
        self.tracker_list = []
        # self.idx_tracker = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.tracker_map:
            return False
        else:
            self.tracker_map[val] = len(self.tracker_list)
            self.tracker_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # print("remove ", val, self.tracker_map)
        if val not in self.tracker_map:
            return False

        present_at_idx = self.tracker_map.get(val)
        last_idx = len(self.tracker_list) - 1
        if present_at_idx == last_idx:
            self.tracker_list.pop()
            self.tracker_map.pop(val)
        else:
            # print(self.tracker_map)
            last_element = self.tracker_list[last_idx]
            self.tracker_list[present_at_idx] = last_element
            self.tracker_map[last_element] = present_at_idx
            self.tracker_list.pop()
            self.tracker_map.pop(val)
            # print(self.tracker_list)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # print(self.tracker_list)
        last_idx = len(self.tracker_list) - 1
        return self.tracker_list[random.randint(0, last_idx)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
