import face_recognition,os
def face_distance( getimages ):
    # Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
    # You can do that by using the face_distance function.

    # The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
    # be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
    # positive matches at the risk of more false negatives.

    # Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
    # smaller distance are more similar to each other than ones with a larger distance.

    # Load some images to compare against
    os.chdir("./face_recognize/goodImage/")
    myimagelist =[]
    for img in os.listdir("./"):
        imgurl = "./"+img
        myimagelist.append(imgurl)
        print(myimagelist)


    known_face_0 = face_recognition.load_image_file(myimagelist[0])
    known_face_1 = face_recognition.load_image_file(myimagelist[1])
    known_face_2 = face_recognition.load_image_file(myimagelist[2])
    known_face_3 = face_recognition.load_image_file(myimagelist[3])
    known_face_4 = face_recognition.load_image_file(myimagelist[4])
    # known_face_5 = face_recognition.load_image_file(myimagelist[5])
    # known_face_6 = face_recognition.load_image_file(myimagelist[6])
    # known_face_7 = face_recognition.load_image_file(myimagelist[7])
    # known_face_8 = face_recognition.load_image_file(myimagelist[8])
    # known_face_9 = face_recognition.load_image_file(myimagelist[9])



    # Get the face encodings for the known images
    known_face_0_encoding = face_recognition.face_encodings(known_face_0)[0]
    known_face_1_encoding = face_recognition.face_encodings(known_face_1)[0]
    known_face_2_encoding = face_recognition.face_encodings(known_face_2)[0]
    known_face_3_encoding = face_recognition.face_encodings(known_face_3)[0]
    known_face_4_encoding = face_recognition.face_encodings(known_face_4)[0]
    # known_face_5_encoding = face_recognition.face_encodings(known_face_5)[0]
    # known_face_6_encoding = face_recognition.face_encodings(known_face_6)[0]
    # known_face_7_encoding = face_recognition.face_encodings(known_face_7)[0]
    # known_face_8_encoding = face_recognition.face_encodings(known_face_8)[0]
    # known_face_9_encoding = face_recognition.face_encodings(known_face_9)[0]


    known_encodings = [
        known_face_0_encoding,
        known_face_1_encoding,
        known_face_2_encoding,
        known_face_3_encoding,
        known_face_4_encoding,
        # known_face_5_encoding,
        # known_face_6_encoding,
        # known_face_7_encoding,
        # known_face_8_encoding,
        # known_face_9_encoding
    ]

    # Load a test image and get encondings for it
    image_to_test = face_recognition.load_image_file("./myimage/tianlong1.jpg")
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    # See how far apart the test image is from the known faces
    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)


    face_distances_available =[]


    for i, face_distance in enumerate(face_distances):
        # print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
        # print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
        # print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
        # print()
        print("测试图片和已知图片距离为 {:.2} #第{}次测试".format(face_distance, i+1))
        print("- 在正常截止点为0.6的情况下，测试图像是否与已知图像相匹配？ {}".format(face_distance < 0.6))
        print("- 在非常严格的0.5分界线的情况下，测试图像是否与已知图像相匹配？ {}".format(face_distance < 0.5))
        print()
        face_distances_available.append(face_distance)

    return face_distances_available