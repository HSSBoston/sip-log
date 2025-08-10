import board, mpu6886

i2c = board.I2C()
mpu = mpu6886.MPU6886(i2c)

accel = mpu.acceleration
print(accel)
