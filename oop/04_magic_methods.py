class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Comparison
    def __eq__(self, other):
        return self.title == other.title
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    # Addition
    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.author, self.pages + other.pages)
    
    # Length
    def __len__(self):
        return self.pages
    
    # Callable
    def __call__(self):
        return f"Reading {self.title}"