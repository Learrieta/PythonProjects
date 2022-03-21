import math


def main():
    name = "#1 Picnic"
    volume = compute_volume(10.16, 6.83) 
    surface = compute_surface_area(10.16, 6.83)
    storage = compute_storage_efficiency(volume,surface)
    cost = compute_cost_efficiency(volume, 0.28)
    print(f'{name} : {storage:.1f}, cost: ${cost:.2f}')

    name = "#1 Tall"
    volume = compute_volume(11.91, 7.78) 
    surface = compute_surface_area(11.91, 7.78)
    storage = compute_storage_efficiency(volume,surface)
    cost = compute_cost_efficiency(volume, 0.43)
    print(f'{name} : {storage:.1f}, cost: ${cost:.2f}')

    name = "#2"
    volume = compute_volume(11.59, 8.73) 
    surface = compute_surface_area(11.59, 8.73)
    storage = compute_storage_efficiency(volume,surface)
    cost = compute_cost_efficiency(volume, 0.45)
    print(f'{name} : {storage:.1f}, cost: ${cost:.2f}')


    name = "#2.5"
    volume = compute_volume(11.91, 10.32) 
    surface = compute_surface_area(11.91, 10.32)
    storage = compute_storage_efficiency(volume,surface)
    cost = compute_cost_efficiency(volume, 0.61)
    print(f'{name} : {storage:.1f}, cost: ${cost:.2f}')


    name = "#3 Cylinder"
    volume = compute_volume(17.78, 10.79) 
    surface = compute_surface_area(17.78, 10.79) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')


    name = "#5"
    volume = compute_volume(14.29, 13.02) 
    surface = compute_surface_area(14.29, 13.02) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')


    name = "#6Z"
    volume = compute_volume(8.89, 5.40) 
    surface = compute_surface_area(8.89, 5.40) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')

    name = "#8Z short"
    volume = compute_volume(7.62, 6.83) 
    surface = compute_surface_area(7.62, 6.83) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')

    name = "#10"
    volume = compute_volume(17.78, 15.72) 
    surface = compute_surface_area(17.78, 15.72) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')

    name = "211"
    volume = compute_volume(12.38, 6.83) 
    surface = compute_surface_area(12.38, 6.83) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')

    name = "#300"
    volume = compute_volume(11.27, 7.62) 
    surface = compute_surface_area(11.27, 7.62) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')

    name = "#303"
    volume = compute_volume(11.11, 8.10) 
    surface = compute_surface_area(11.11, 8.10) 
    storage = compute_storage_efficiency(volume,surface)
    print(f'{name} : {storage:.1f}')

    


def compute_volume (height, radius):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(height, radius):
    surface = 2 * math.pi * radius * (radius + height)
    return surface

def compute_storage_efficiency(volume, surface):
    storage = volume / surface
    return storage

def compute_cost_efficiency(volume, cost):
    cost = volume / cost
    return cost

main()