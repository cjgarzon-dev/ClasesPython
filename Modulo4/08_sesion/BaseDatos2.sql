# Crear tablas con relaciones
CREATE TABLE Cursos(
	id_cursos INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    profesor_id INT,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);

# Llamar los cursos
SELECT * FROM cursos;

# Insertar un curso
INSERT INTO Cursos(nombre, profesor_id) VALUES
('Matematicas', 1),
('Español', 2),
('Historia', 3);