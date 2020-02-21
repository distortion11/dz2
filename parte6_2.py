def resize(self, width=None, height=None):
    if width is None and height is None:
        return False
    if width is None:
        width = self.width
    if height is None:
        height = self.height
    if width >= self.width and height >= self.height:
        self.__width = width
        self.__height = height
        return True
    self.__width = width
    self.__height = height
    for x, y in list(self.__data.keys()):
        if x >= self.width or y >= self.height:
            del self.__data[(x, y)]
    self.__colors = set(self.__data.values()) | {self.__background}
    return True