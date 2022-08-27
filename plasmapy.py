#!/usr/bin/python

def absolute_distance_mode():
    return "G90\n"

def millimetre_unit():
    return "G71\n"

def end():
    return "M30\n"

def init():
    return \
        absolute_distance_mode() + \
        millimetre_unit()

def plasma_off():
    return "M5\n"

def plasma_on():
    return "M3\n"

def pierce_delay(sec):
    return f"G4 P{sec}\n"

def goto_zero(speed):
    if speed == 0:
        return f"G0 X0 Y0 Z0 F{speed}\n"
    else:
        return f"G1 X0 Y0 Z0 F{speed}\n"

def xyzspeed(x = None, y = None, z = None, speed = None):
    code = ""
    if x != None:
        code += f"X{x} "
    if y != None:
        code += f"Y{y} "
    if z != None:
        code += f"Z{z} "
    if speed != None:
        code += f"F{speed} "
    return code

def set_temporary_work_coordinates(x = None, y = None, z = None):
    return "G92 " + xyzspeed(x,y,z,None) + "\n"

def probe_straight(x = None, y = None, z = None, speed = None):
    return "G31 " + xyzspeed(x,y,z,speed) + "\n"

def goto(x = None, y = None, z = None, speed = None):
    return "G1 " + xyzspeed(x,y,z,speed) + "\n"

def goto_rapid(x = None, y = None, z = None):
    return "G0 " + xyzspeed(x,y,z,None) + "\n"

def main() -> int:
    cut_length = 700

    cut_speed = 2000
    lead_in_speed = cut_speed * 0.75

    code = ""
    code += init()
    code += goto_zero(speed=0)
    code += probe_straight(z=-100, speed=400)
    code += set_temporary_work_coordinates(z=-0.2)
    code += goto(z=3.8)
    code += plasma_on()
    code += pierce_delay(0.3)
    code += goto(z=1.5, speed=lead_in_speed)

    code += goto(x=cut_length, speed=cut_speed)

    code += plasma_off()


    code += "\n"
    code += goto_rapid(z=100)
    code += init()
    code += end()

    print(code)

if __name__ == '__main__':
    main()
