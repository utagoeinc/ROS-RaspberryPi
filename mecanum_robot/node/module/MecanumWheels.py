def __calcParam(direction, speed):
    a = 0
    b = 0
    d = direction * 4
    if direction > -0.5 and direction <= 0: # Right Forward
        a = d + 1
        b = 1
    elif direction > -1 and direction <= -0.5: # Right Backward
        a = -1
        b = d + 3
    elif direction > 0 and direction <= 0.5: # Left Forward
        a = 1
        b = -d + 1
    elif direction > 0.5 and direction <= 1: # Left Backward
        a = -d + 3
        b = -1
    else:
        print('direction value range must be (-1, 1]')

    a = a * speed
    b = b * speed
    return a, b

def normalMove(direciton=0, speed=1):
    a, b = __calcParam(direciton, speed)
    return [a, a, b, b]


def parallelMove(direciton=0, speed=1):
    a, b = __calcParam(direciton, speed)
    return [a, b, b, a]

def stop():
    return [0, 0, 0, 0]

def forward(speed=1):
    ls_drc = [1, 1, 1, 1] 
    return [n * speed for n in ls_drc]

def backward(speed=1):
    ls_drc = [-1, -1, -1, -1] 
    return [n * speed for n in ls_drc]

def rotateRight(speed=1):
    ls_drc = [-1, -1, 1, 1] 
    return [n * speed for n in ls_drc]

def rotateLeft(speed=1):
    ls_drc = [1, 1, -1, -1] 
    return [n * speed for n in ls_drc]

def parallelRight(speed=1):
    ls_drc = [-1, 1, 1, -1] 
    return [n * speed for n in ls_drc]

def parallelLeft(speed=1):
    ls_drc = [1, -1, -1, 1] 
    return [n * speed for n in ls_drc]

def parallelForwardRight(speed=1):
    ls_drc = [1, 0, 0, 1] 
    return [n * speed for n in ls_drc]

def parallelBackwardRight(speed=1):
    ls_drc = [-1, 0, 0, -1] 
    return [n * speed for n in ls_drc]

def parallelForwardLeft(speed=1):
    ls_drc = [0, 1, 1, 0] 
    return [n * speed for n in ls_drc]

def parallelBackwardLeft(speed=1):
    ls_drc = [0, -1, -1, 0] 
    return [n * speed for n in ls_drc]

    
