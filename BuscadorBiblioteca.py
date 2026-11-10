dune = {
    'titulo': 'dune',
    'autor': 'Frank herbert',
    'anioPublicacion': 1965,
    'genero': 'ficcion',
    'copiasdisponibles': 1
}

metamorfosis = {
    'titulo': 'metamorfosis',
    'autor': 'franz kafka',
    'anioPublicacion': 1915,
    'genero': 'novela',
    'copiasdisponibles': 4
}

it = {
    'titulo': 'it',
    'autor': 'stephen king',
    'anioPublicacion': 1986,
    'genero': 'terror',
    'copiasdisponibles': 3
}
harry_potter = {
    'titulo': 'harry potter', 
    'autor' : 'J,k rowling',
    'genero': 'ficcion',
    'anioPublicacion': 1997,
    'copiasdisponibles': 5

}

posesion = {
    'titulo': 'posesion',
    'autor': 'George Orwell',
    'anioPublicacion': 1996,
    'genero': 'terror',
    'copiasdisponibles': 0

}

el_senior_de_los_anillos = {
    'titulo': 'el senior de los anillos',
    'autor': 'J.R.R.Tolkien',
    'anioPublicacion': 1954,
    'genero': 'ficcion',
    'copiasdisponibles': 9

}

pedro_paramo = {
    'titulo': 'pedro paramo',
    'autor': 'Juan rulfo',
    'anioPublicacion': 1955,
    'genero': 'novela',
    'copiasdisponibles': 1

}

don_quijote_de_la_mancha = {
    'titulo': 'don quijote de la mancha',
    'autor': 'Miguel de cervantes',
    'anioPublicacion': 1605,
    'genero': 'novela',
    'copiasdisponibles': 5

}

    

inventario = [dune, it, pedro_paramo, el_senior_de_los_anillos, metamorfosis, posesion, don_quijote_de_la_mancha, harry_potter]



while True:
    print("biblioteca")
    print("1. buscar libro por titulo")
    print("2. buscar generos")
    print("3. mostrar libros antiguos (antes del 2000 y no de Ciencia)")
    print("0. salir")

    opcion = input("seleccionar una opcion: ")

    if opcion == "0":
        print("saliendo del sistema")
        break

    elif opcion == "1":
        titulo_buscar = input("cual libro buscas?: ")
        encontrado = False

        for libro in inventario:
            if libro['titulo'] == titulo_buscar:
                encontrado = True
                if libro['copiasdisponibles'] > 0:
                    print(f"El libro '{libro['titulo']}' esta disponible ({libro['copiasdisponibles']} copias).")
                else:
                    print(f"El libro '{libro['titulo']}' esta agotado.")
                break 

        if not encontrado:
            print(f"El libro '{titulo_buscar}' no se encuentra.")

    elif opcion == "2":
        genero_buscar = input("ingrese el genero: ")
        titulos_en_genero = []

        for libro in inventario:
            if libro['genero'] == genero_buscar:
                titulos_en_genero.append(libro['titulo'])

        print(f"Total de libros de {genero_buscar}: {len(titulos_en_genero)}")
        if titulos_en_genero:
            print("titulos encontrados:")
            for titulo in titulos_en_genero:
                print(f"- {titulo}")
        else:
            print("no hay libros de ese genero.")

    elif opcion == "3":
        anio_limite = 2000
        libros_antiguos = []

        for libro in inventario:
            if (libro["anioPublicacion"] < anio_limite) and (libro['genero'] != "ciencia"):
                libros_antiguos.append(libro['titulo'])

        print(f"Libros publicados antes del año {anio_limite} y que no son de ciencia:")
        if libros_antiguos:
            for titulo in libros_antiguos:
                print(f"- {titulo}")
        else:
            print("no se encontraron libros antiguos con esos criterios.")

    else:
        print("opcion no valida.")
