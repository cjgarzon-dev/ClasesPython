# Creacion de DB
CREATE DATABASE store_Dev;

# Se selecciona la base de datos
USE store_Dev;

# Creacion de tablas
CREATE TABLE clients(
	id_client INT PRIMARY KEY AUTO_INCREMENT,
    name_client VARCHAR(100),
    email_client VARCHAR(100),
    cellphone_client VARCHAR(20)
);

CREATE TABLE products(
	id_product INT PRIMARY KEY AUTO_INCREMENT,
    name_product VARCHAR(100),
    price_product DOUBLE,
    stock_product INT
);

CREATE TABLE sales(
	id_sale INT PRIMARY KEY AUTO_INCREMENT,
    cant_sale INT,
    date_sale VARCHAR(20),
    total_sale DOUBLE,
    id_client INT,
    FOREIGN KEY (id_client) REFERENCES clients(id_client),
    id_product INT,
    FOREIGN KEY (id_product) REFERENCES products(id_product)
);

# Insertar datos a las tablas
INSERT INTO clients(name_client, email_client, cellphone_client) VALUES
	('Ana Torres', 'ana.torres@example.com', '3001234567'),
	('Luis Gómez', 'luis.gomez@example.com', '3012345678'),
	('María Ríos', 'maria.rios@example.com', '3023456789'),
	('Carlos Pérez', 'carlos.perez@example.com', '3034567890'),
	('Laura Díaz', 'laura.diaz@example.com', '3045678901'),
	('Jorge Ramírez', 'jorge.ramirez@example.com', '3056789012'),
	('Sofía Herrera', 'sofia.herrera@example.com', '3067890123'),
	('Andrés Molina', 'andres.molina@example.com', '3078901234'),
	('Valentina Cruz', 'valentina.cruz@example.com', '3089012345'),
	('Mateo Salazar', 'mateo.salazar@example.com', '3090123456');

INSERT INTO products (name_product, price_product, stock_product) VALUES
	('Laptop Lenovo', 2500.00, 15),
	('Mouse Inalámbrico', 45.99, 100),
	('Teclado Mecánico', 120.50, 50),
	('Monitor 24"', 300.00, 30),
	('Disco Duro 1TB', 85.75, 40),
	('Memoria USB 64GB', 20.00, 200),
	('Impresora HP', 150.00, 25),
	('Tablet Samsung', 600.00, 20),
	('Auriculares Bluetooth', 75.00, 60),
	('Cámara Web HD', 55.00, 35);

INSERT INTO sales (cant_sale, date_sale, total_sale, id_client, id_product) VALUES
	(1, '2025-05-01', 2500.00, 1, 1),
	(2, '2025-05-02', 91.98, 2, 2),
	(1, '2025-05-03', 120.50, 3, 3),
	(1, '2025-05-04', 300.00, 4, 4),
	(3, '2025-05-05', 257.25, 5, 5),
	(5, '2025-05-06', 100.00, 6, 6),
	(1, '2025-05-07', 150.00, 7, 7),
	(2, '2025-05-08', 1200.00, 8, 8),
	(2, '2025-05-09', 150.00, 9, 9),
	(1, '2025-05-10', 55.00, 10, 10);

# Realizar consulta con JOIN (consulta general)
SELECT *
FROM sales AS s
JOIN clients ON s.id_client = clients.id_client
JOIN products AS p ON s.id_product = p.id_product;

# Realizar consulta con JOIN (consulta específica)
SELECT c.name_client AS Cliente, p.name_product AS Producto, s.cant_sale AS Cantidad, p.price_product AS PrecioUni, s.total_sale AS PrecioTotal 
FROM sales AS s
JOIN clients AS c ON s.id_client = c.id_client
JOIN products AS p ON s.id_product = p.id_product;