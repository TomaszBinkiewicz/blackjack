def validate_pos_int(in_val):
    try:
        ret_val = int(in_val)
        if ret_val <= 0:
            raise ValueError
    except ValueError:
        return False
    except TypeError:
        return False
    else:
        return ret_val
