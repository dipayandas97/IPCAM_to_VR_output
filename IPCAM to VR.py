import requests 
import cv2
import numpy as np
import screeninfo


url = "http://192.168.137.137:8080/shot.jpg"


try:
    img_resp = requests.get(url)
except Exception as e:
    ip = input('Ip_cam_address(ip:port): ')
    url = 'http://'+ip+'/shot.jpg'

print('Connected to ip_cam : ',url,'\n')


while True:

    img_resp = requests.get(url)
    
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    screen_id = 0
    screen = screeninfo.get_monitors()[screen_id]
    width, height = screen.width, screen.height
    
    img = cv2.resize(img, (int(width/2),height))
    frame = np.hstack((img,img))

    window = cv2.namedWindow('VR', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('VR', (width,height))
    
    print('frame shape:',frame.shape)
    cv2.imshow("VR", frame)
   
    if cv2.waitKey(1) == ord('q'):
        break
       
