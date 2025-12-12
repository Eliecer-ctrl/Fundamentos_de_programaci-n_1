def unique_emails(nombre_fichero):
    with open(nombre_fichero, 'r', encoding='utf-8') as f:
        contenido = f.read()
    todos_los_emails = get_emails(contenido)
    emails_unicos_set = set(todos_los_emails)
    emails_unicos_lista = list(emails_unicos_set)

    return emails_unicos_lista