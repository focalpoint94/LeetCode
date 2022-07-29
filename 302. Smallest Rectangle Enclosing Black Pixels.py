class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        # swap
        y, x = x, y
        # search ymin
        ymin = y
        l, r = 0, y
        while l <= r:
            mid = (l + r) // 2
            if '1' in image[mid]:
                ymin = min(ymin, mid)
                r = mid - 1
            else:
                l = mid + 1
        # search ymax
        ymax = y
        l, r = y, m - 1
        while l <= r:
            mid = (l + r) // 2
            if '1' in image[mid]:
                ymax = max(ymax, mid)
                l = mid + 1
            else:
                r = mid - 1
        # search xmin
        xmin = x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if '1' in [image[i][mid] for i in range(m)]:
                xmin = min(xmin, mid)
                r = mid - 1
            else:
                l = mid + 1
        # search xmax
        xmax = x
        l, r = x, n - 1
        while l <= r:
            mid = (l + r) // 2
            if '1' in [image[i][mid] for i in range(m)]:
                xmax = max(xmax, mid)
                l = mid + 1
            else:
                r = mid - 1
        return (ymax - ymin + 1) * (xmax - xmin + 1)
