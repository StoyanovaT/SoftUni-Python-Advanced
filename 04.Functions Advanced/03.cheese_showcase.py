def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0]),
    )

    result = []

    for name, pieces_counts in sorted_cheeses:
        result.append(name)
        # for piece_count in pieces_counts:
        #     result.append(piece_count)
        result.extend(
            sorted(pieces_counts, reverse=True)
        )

    return '\n'.join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

