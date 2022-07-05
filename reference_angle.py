def radians_to_degrees():
    # This is to change from radians to degrees
    print('Type the angle in terms of π: (however do not type the pi, ex: pi/2, type 0.5)')
    angle = float(input())
    angle_degrees = (angle/2)*(360)
    return angle_degrees

def degrees_to_radians():
    # This is to change from degrees to radians
    print('Type the angle:')
    angle = float(input())
    angle_radians = angle/180
    return angle_radians

while True:
    print('What would you like to do?')
    print('1: Change degrees to reference angle')
    print('2: Change degrees to radians')
    print('3: Change radians to degrees')
    print('4: Determine if an angle is coterminal to another')
    print('exit: Exit program')

    x = input()

    print(x, 'has been selected!')
    if(x == '1'):
        # This is to change degrees to reference angle
        print('Angle in degrees:')
        angle = float(input())
        if angle == 180.0 or angle == 360.0:
            print('Degrees: ', 0, '°')
            zero = True
        else:
            zero = False
        while angle > 90:
            angle = angle - 90
        if zero == False:
            print('Degrees: ', angle, '°')
    if(x == '2'):
        print('Radians: ', degrees_to_radians(), 'π')
    if(x == '3'):
        print('Degrees: ', radians_to_degrees(), '°')
    if(x == '4'):
        # This is to determine if an angle is coterminal
        for i in range(2):
            print('1: Angle is in radians')
            print('2: Angle is in degrees')
            r_or_d = input()
            r_or_d = int(r_or_d)
            if r_or_d == 1 and i == 0:
                print('Angle 1')
                angle1 = radians_to_degrees()
            elif r_or_d == 1 and i == 1:
                print('Angle 2')
                angle2 = radians_to_degrees()
            elif r_or_d == 2 and i == 0:
                print('Angle 1')
                angle1 = float(input())
            elif r_or_d == 2 and i == 1:
                print('Angle 2')
                angle2 = float(input())
            
        while angle1 >= 360:
            angle1 - 360
        while angle2 >= 360:
            angle2 - 360
        if angle1 == angle2:
            print('These angles are coterminal!')
        else:
            print('These angles are NOT coterminal!')
    if(x == 'exit'):
        break