from cv2.cv import *
capture = CaptureFromCAM(3)
if capture:
    NamedWindow("cam test", CV_WINDOW_AUTOSIZE)
    f = QueryFrame(capture)
    if f:
        ShowImage("cam test", f)
        WaitKey(0)
DestroyWindow("cam test")
