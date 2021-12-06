import os
import os.path
import time
import cv2
import yaml
import face_recognize.face_distance as face_distance
def setting():
    f = open('./config.yaml',encoding='UTF-8')
    dict = yaml.full_load(f)

    cheak_file=dict['cheak_file']
    work_path=dict['work_path']
    run_timesleep=dict['run_timesleep']
    camera_timesleep=dict['camera_timesleep']

    return cheak_file,work_path,run_timesleep,camera_timesleep

def file_exit(cheak_file):
    get_file_exit = os.path.isfile(cheak_file)
    return get_file_exit


def camera():
    localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)
    f, frame = cap.read()  # 此刻拍照
    cv2.imwrite("{}.png".format(localtime),frame)  # 将拍摄内容保存为png图片
    cap.release()  # 关闭调用的摄像头
    cv2.destroyAllWindows()

def isRight():
    face_distances_available =face_distance()
    print (face_distances_available)
    pass

if __name__ == '__main__':
    # setting()
    # setting=setting()
    # os.chdir(setting[1])
    # get_file_exit=file_exit(setting[0])
    # # print(get_file_exit)
    # time.sleep(setting[2])
    # while True:
    #     # fileexit = file_exit(path)
    #     if get_file_exit == False:
    #         camera()
    #         time.sleep(setting[3])
    #     else:
    #         break
    for i in range(5):
        camera()
    isRight()


