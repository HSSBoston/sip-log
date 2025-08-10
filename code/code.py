import board, mpu6886, time, math
import display, kintone

SUB_DOMAIN  = "jxsboston"
APP_ID      = "21"
API_TOKEN   = "TZiC2n9KnPzozt7EUsZHuPIYvysGMSGK0bMqnAhv"

DEMO_MODE = True
ACCEL_SENSING_INTERVAL = 1    # in seconds
ALERT_INTERVAL         = 1200 # in seconds

i2c = board.I2C()
mpu = mpu6886.MPU6886(i2c)
accelSensingCount = 0

# Take X, Y, and Z acceleration values in m/s^2.
# Return the pitch angle (in radian) between the ground surface
#   and the positive (right) side of the Y axis.
#
def calcPitch(x, y, z):
    accelMagnitude = math.sqrt(x**2 + y**2 + z**2)
    yNormalized = y/accelMagnitude
    if z >= 0:
        pitchY = math.asin(-yNormalized)
    else:
        pitchY = math.acos(-yNormalized) + math.pi/2
    return pitchY

if DEMO_MODE:
    display.init()
    time.sleep(3)
else:
    display.init(demoMode=False)

while True:
    accel = mpu.acceleration
    x = accel[0]
    y = accel[1]
    z = accel[2]

    pitchRadian  = calcPitch(x, y, z)
    pitchDegrees = round( math.degrees(pitchRadian) )
    print("Pitch (degrees):", pitchDegrees)
    if DEMO_MODE:
        display.resetText("Pitch:" + str(pitchDegrees))
    accelSensingCount += 1
    print(accelSensingCount)

    if pitchDegrees >= 45:
        kintone.uploadSipLog(SUB_DOMAIN, APP_ID, API_TOKEN,
                             pitchDegrees)
        accelSensingCount = 0
        print(accelSensingCount)
    
    if accelSensingCount > int(ALERT_INTERVAL/ACCEL_SENSING_INTERVAL):
        alertText =f"No water intake for {int(ALERT_INTERVAL/60)} mins"
        print("ALERT", alertText)
        kintone.uploadAlert(SUB_DOMAIN, APP_ID, API_TOKEN,
                            alertText)        
        accelSensingCount = 0
    
    time.sleep(ACCEL_SENSING_INTERVAL)
