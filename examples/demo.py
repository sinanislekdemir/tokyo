from tokyo import TokyoGrid

grid = TokyoGrid()
grid.put_pixel(1, 1, 4)  # Red
grid.put_pixel(2, 2, 3)  # Cyan
grid.put_pixel(3, 3, 14)  # Yellow
grid.put_pixel(4, 4, 15)  # White
grid.render()
grid.run_until_closed()
