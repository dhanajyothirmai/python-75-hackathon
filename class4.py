class box:
    shape = 'square'
    def __init__(colour,size):
        colour.size= size
    def set(colour,shade):
        colour.shade = shade
    def get(colour):
        return colour.shade, colour.size, colour.shape
    a = box(10)
    a.set("black, blue")
    print(a.get())
