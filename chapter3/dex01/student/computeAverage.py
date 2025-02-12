def mix_colors(color1, color2):
    primary_colors = ["red", "blue", "yellow"]  # Changed to a list for ordered comparison
    secondary_colors = {
        ("red", "blue"): "purple",
        ("red", "yellow"): "orange",
        ("blue", "yellow"): "green"
    }

    if color1 not in primary_colors or color2 not in primary_colors:
        return "Error: Please enter valid primary colors (red, blue, yellow)."
    
    # Ensure color1 is always the first in the tuple
    if primary_colors.index(color1) > primary_colors.index(color2):
        color1, color2 = color2, color1

    return secondary_colors.get((color1, color2), "Error: Invalid color combination.")

color1 = input("Enter the first primary color (red, blue, yellow): ").strip().lower()
color2 = input("Enter the second primary color (red, blue, yellow): ").strip().lower()

result = mix_colors(color1, color2)
print(result)