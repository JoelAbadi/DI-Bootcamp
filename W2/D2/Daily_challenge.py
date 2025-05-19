import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if not isinstance(page_num, int):
            raise TypeError("Page number must be an integer.")
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return '\n'.join(str(item) for item in self.get_visible_items())
    
    # Create a list of the alphabet
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# Create a Pagination object with 4 items per page
p = Pagination(alphabetList, 4)

# Step-by-step test cases

# ✅ 1. Get visible items on the first page
print(p.get_visible_items())
# Output: ['a', 'b', 'c', 'd']

# ✅ 2. Move to next page and print visible items
p.next_page()
print(p.get_visible_items())
# Output: ['e', 'f', 'g', 'h']

# ✅ 3. Move to last page and print visible items
p.last_page()
print(p.get_visible_items())
# Output: ['y', 'z']

# ✅ 4. Go to page 7 (the last page) and print current index
p.go_to_page(7)
print(p.current_idx + 1)
# Output: 7

# ✅ 5. Attempt to go to page 0 — should raise ValueError
try:
    p.go_to_page(0)
except ValueError as e:
    print("Caught error:", e)
# Output: Caught error: Page number out of range.

# ✅ 6. Print the current page items using __str__()
print(str(p.first_page()))
# Output:
# a
# b
# c
# d

