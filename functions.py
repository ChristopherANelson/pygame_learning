def volume_cylinder(rad, height):
    pi = 3.1415
    volume = pi * rad **2 * height
    return volume

six_pack_volume = volume_cylinder(2.5,5) * 6
print(six_pack_volume)
