def no_empty_lines(texto1, texto2):
    with open(texto1, 'r') as f:
        lines = f.readlines()
    with open(texto2, 'w') as f:
        for line in lines:
            if not line.isspace():
                f.write(line)