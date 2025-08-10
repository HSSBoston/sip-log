import board, mpu6886, time, math

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = mpu6886.MPU6886(i2c)

# Take X, Y, and Z acceleration values in m/s^2
# Return pitch angle (in radian) bertween the ground surface and
# the positive side of the Y axis
#
def pitch(x, y, z):
    accelMagnitude = math.sqrt(x**2 + y**2 + z**2)
    xNormalized = x/accelMagnitude
    yNormalized = y/accelMagnitude
    if z >= 0:
        pitchY = math.asin(-yNormalized)
    else:
        pitchY = math.acos(-yNormalized) + math.pi/2
    return pitchY

while True:
    accel = mpu.acceleration
    x = accel[0]
    y = accel[1]
    z = accel[2]
    print(f"Acceleration: X:{x:.2f}, Y:{y:.2f}, Z:{z:.2f} m/s^2")
    pitchY = pitch(x, y, z)
    print("radian:", pitchY)
    print("degrees:", math.degrees(pitchY))           
    time.sleep(1)
