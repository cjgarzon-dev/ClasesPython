-- Consultas entre tablas (Con JOIN)

-- Mostrar todos los prestamos con información de usuario y libro
-- OPCION 1:
SELECT
	P.id_prestamo AS id_prestamo,
	U.nombre_usuario AS nombre_usuario,
	L.titulo AS titulo_libro,
	P.fecha_prestamo,
	P.fecha_devolucion,
	P.estado,
    CASE
		WHEN P.fecha_devolucion IS NULL THEN 'Libro no ha sido devuelto'
        WHEN P.estado = 'cancelado' THEN 'Prestamo Cancelado'
        ELSE 'Libro devuelto'
	END AS observacion
FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;

-- OPCION 2:
SELECT
	P.id_prestamo AS id_prestamo,
	U.nombre_usuario AS nombre_usuario,
	L.titulo AS titulo_libro,
	P.fecha_prestamo,
	CASE
		WHEN P.fecha_devolucion IS NULL THEN 'Libro no ha sido devuelto'
        WHEN P.estado = 'cancelado' THEN 'Prestamo Cancelado'
        ELSE DATE_FORMAT(P.fecha_devolucion, '%Y-%m-%d')
	END AS fecha_devolucion,
    P.estado
FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;