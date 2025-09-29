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

    
# practice question solution from Discretization 
def compute_equal_width_cutoffs(values, num_bins):
    values_range = max(values) - min(values)
    bin_width = values_range / num_bins

    # generate cutoffs
    cutoffs = [min(values) + i*bin_width for i in range(num_bins)]
    # append the maximum value
    cutoffs.append(max(values))
    # optionally, round
    cutoffs = [round(cutoff,2) for cutoff in cutoffs]
    return cutoffs

def compute_bin_frequencies(values, cutoffs):
    freqs = [0 for _ in range(len(cutoffs) - 1)] # because N + 1 cutoffs

    for value in values:
        if value == max(values):
            freqs[-1] += 1 # add one to the last bin count
        else:
            for i in range(len(cutoffs) - 1):
                if cutoffs[i] <= value < cutoffs[i + 1]:
                    freqs[i] += 1  # add one to this bin defined by [cutoffs[i], cutoffs[i+1])
    return freqs

def group_by(table, header, group_by_col_name):
    dict = {}
    col_index = header.index(group_by_col_name)
    for row in table:
        key = row[col_index]
        if key not in dict:
            dict[key] = []
        dict[key].append(row)
    return dict