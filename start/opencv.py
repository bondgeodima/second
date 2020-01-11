import cv2
vidcap = cv2.VideoCapture('D:/TEMP/_deeplearning/road_signs/__video/VID_20200111_102822.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("D:/TEMP/_deeplearning/road_signs/__video/out/%05d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1