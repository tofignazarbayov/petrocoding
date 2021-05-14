def func(v_pore, v_bulk):
    """
    Input:
    v_pore --> pore volume
    v_bulk --> bulk volume

    Output:
    porosity --> porosity
    """
    porosity = v_pore / v_bulk
    return porosity