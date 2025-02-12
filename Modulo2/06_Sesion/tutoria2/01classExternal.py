class External:
    def __init__(self, message):
        self.message = message
        
    class Internal:
        def __init__(self, external):
            self.external = external
            
        def showMessage(self):
            print(f'Mensaje desde la clase externa {self.external.message}')

external = External('Hola desde la clase externa')
internal = External.Internal(external)
internal.showMessage()