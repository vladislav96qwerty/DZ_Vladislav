def difference(*args):
    if not args:
        return 0

    min_val = min(args)
    max_val = max(args)

    result = max_val - min_val
    return round(result, 2) if isinstance(result, float) else result
