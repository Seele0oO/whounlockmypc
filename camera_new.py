import os
import os.path
import time
import cv2
import yaml
import face_recognize.face_distance as face_distance
import root
def setting():
    f = open('./config.yaml',encoding='UTF-8')
    dict = yaml.full_load(f)

    cheak_file=dict['cheak_file']
    work_path=dict['work_path']
    run_timesleep=dict['run_timesleep']
    camera_timesleep=dict['camera_timesleep']

    return cheak_file,work_path,run_timesleep,camera_timesleep

def file_exit(cheak_file):
    ## out of date
    get_file_exit = os.path.isfile(cheak_file)
    return get_file_exit




def camera():

    localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    while ret:
        resize = cv2.resize(frame, (1280,720), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(str(localtime)+'.jpg', resize)
        time.sleep(0.5)
        ret, frame = cap.read()


        cap.release()
        cv2.destroyAllWindows()
    return 0 


def isRight(getImage):
    face_distances_available =face_distance.face_distance(getImage)
    sum = 0
    for i in face_distances_available:
        sum = sum+i
    sum = sum/5
    print (str(getImage)+"的不相似度为"+str(sum))
    return sum


def continue_camera():
    os.chdir(root+"/Intruder")
    camera()
    pass

if __name__ == '__main__':
    root = root.cwd()
    # global Intruder
    Intruder = False

    os.chdir(root+"/face_recognize/getImage")
    for i in range(5):
        camera()
        pass
    # try:
    os.chdir(root)
    print(os.getcwd())
    for getImage in os.listdir(root+"/face_recognize/getImage"):
        getImage = root+"/face_recognize/getImage/"+getImage
        # print(getImage)
        try:
            isright = isRight(getImage)
            print(isright)
            if isright > 0.5:
                Intruder = True
                # print("Intruder!!!!!!!!!!!",Intruder)
            else:
                # print("NoIntruder",Intruder)
                pass
        except IndexError:
            print("无人脸数据")
        # global isright
        # isright = isRight(getImage)
        # if isright > 0.4:
        #     continue_camera()
        # else:
        #     pass
    # except IndexError:
    #     pass
    print(Intruder)
    if Intruder == False:
        os.chdir(root)
        filepath = "./face_recognize/getImage"
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
        pass
    else:
        while True:
            continue_camera()


