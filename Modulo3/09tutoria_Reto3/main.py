from Model.model import Store
from Controller.controller import ControllerStore
from View.view import ViewStore

if __name__ == '__main__':
    model = Store()
    model.add_products(1, 'Manzana', 1, 100)
    model.add_products(2, 'Pera', 2, 100)
    model.add_products(3, 'Mango', 3, 100)

    controller = ControllerStore(model, None)

    view = ViewStore(controller)
    
    controller.view = view