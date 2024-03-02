class Data:

    def __init__(self,**kwargs):
        self.data = kwargs.items()
        for key,value in self.data:
            setattr(self,key,value)

    def __str__(self):
        return f"data({', '.join([f'{key}={repr(value)}' for key, value in self.data])})"
