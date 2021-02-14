from mcpi.minecraft import Minecraft
import time, random
mc = Minecraft.create()

# клавиша f3
x = 0
y = 0
z = 0
block = 46

for y in range(50, 250):
	mc.setBlock(x, y, z, block)
