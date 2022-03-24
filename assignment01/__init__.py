def print_matrices(a: list) -> None:
    if a:
        print(f'Type: {len(a)}x{len(a[0])}')
        for row in a:
            print(row)
