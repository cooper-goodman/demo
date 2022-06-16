import folium as fm
from typing import List

# Say hello!
def get_map_of_clt(center: List[float] = [35.22, -80.84], zoom: int = 11) -> fm.Map:
    """
    Creates and returns a folium.Map of Charlotte, NC.

    Args:
        center (List[float]): the lon, lat for the center of the map.
        zoom (int): the starting level of zoom.

    Returns:
        folium.Map showing Charlotte, NC

    Tip:
        Maps are fun!
    """
    m = fm.Map(center, zoom_start=zoom)
    return m