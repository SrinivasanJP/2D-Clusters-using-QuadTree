class Quadtree:
    def __init__(self, bounds, depth=0, max_depth=4):
        self.bounds = bounds  # [xmin, ymin, xmax, ymax]
        self.children = []
        self.points = []
        self.depth = depth
        self.max_depth = max_depth

    def insert(self, point):
        if self.depth < self.max_depth:
            if not self.children:
                self.subdivide()
            for child in self.children:
                if child.contains(point):
                    child.insert(point)
                    return
        self.points.append(point)

    def contains(self, point):
        x, y = point
        xmin, ymin, xmax, ymax = self.bounds
        return xmin <= x < xmax and ymin <= y < ymax

    def subdivide(self):
        xmin, ymin, xmax, ymax = self.bounds
        midx = (xmin + xmax) / 2
        midy = (ymin + ymax) / 2
        self.children = [
            Quadtree([xmin, ymin, midx, midy], self.depth + 1, self.max_depth),
            Quadtree([midx, ymin, xmax, midy], self.depth + 1, self.max_depth),
            Quadtree([xmin, midy, midx, ymax], self.depth + 1, self.max_depth),
            Quadtree([midx, midy, xmax, ymax], self.depth + 1, self.max_depth),
        ]

    def draw(self, ax):
        xmin, ymin, xmax, ymax = self.bounds
        line_width = 2 if self.depth == 1 else 0.5  # Thicker line for root square
        ax.plot([xmin, xmax], [ymin, ymin], 'k-', lw=line_width)  # Bottom
        ax.plot([xmin, xmax], [ymax, ymax], 'k-', lw=line_width)  # Top
        ax.plot([xmin, xmin], [ymin, ymax], 'k-', lw=line_width)  # Left
        ax.plot([xmax, xmax], [ymin, ymax], 'k-', lw=line_width)  # Right
        for child in self.children:
            child.draw(ax)
