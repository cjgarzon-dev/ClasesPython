from model.model import Store
from controller.controller import ControllerStore
from view.view import ViewStore

model = Store()
model.add_products(1, 'Manzana', 1, 100)
model.add_products(1, 'Pera', 2, 100)
model.add_products(1, 'Mango', 3, 100)

controller = ControllerStore(model, None)

view = ViewStore(controller)