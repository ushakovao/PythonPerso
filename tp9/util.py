


import  numpy as np



def uint8clipRound(a):
        return np.uint8(np.clip(np.round(a),0,255))