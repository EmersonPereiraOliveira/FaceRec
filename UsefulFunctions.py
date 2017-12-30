import cv2
class UsefulFunctions(object):
    def __init__(self):
        pass

    def verify_ret(self, ret):
        if ret == False:
            print("Turn on your camera!")
            return ret

    def verify_key(self, k):
        print(k)
        if k == 27:
            print("27")
        elif k == ord('q'):
            print("Q")



