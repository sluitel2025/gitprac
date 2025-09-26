def get_column(table, header, col):
    col_idx = header.index(col)
    column = []
    for row in table:
        val = row[col_idx]
        column.append(val)
    return column

def get_frequencies(table, header, col):
    col = get_column(table, header, col)
    unique_val = list(set(col))
    count = []
    for val in unique_val:
        count.append(col.count(val))
    return unique_val, count