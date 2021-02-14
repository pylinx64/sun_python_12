from mcpi.minecraft import Minecraft
import time, random
mc = Minecraft.create()

while True:
	x = random.randint(-100, 100)
	y = random.randint(100, 200)
	z = random.randint(-100, 100)
	time.sleep(10)
	mc.player.setTilePos(x, y, z)
	
