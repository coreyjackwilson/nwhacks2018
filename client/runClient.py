import cv2
import numpy as np
import time
from ernn.emotion_recognition import EmotionRecognition
from ernn.constants import *
from ernn.poc import format_image
from client.client_manager import ClientHelper
from ernn.dataset_loader import DatasetLoader


def run():
#Vars
    #load = DatasetLoader()
    #load.load_from_save()

    config = ClientHelper()

    network = EmotionRecognition()
    network.load_saved_dataset()
    network.build_network()

    video_capture = cv2.VideoCapture(0)

    #print("reading Image")
    #img = cv2.imread('test3.jpg', 0)


    #print("my butthole is ready")
    #print("my butthole is really ready")
    #print("my butthole is really really ready")

    while True:
        time.sleep(.9)
        ret, frame = video_capture.read()
        #analyze image for separate faces

        result = network.predict(format_image(frame))
        print("checkin 1")
    #if not result:
    #    print("result faileds")
        for feeling in result:
            #print(feeling)
            for emotion in feeling:
                if emotion >= config.trigger_threshold:
                    config.emergency_update(result, frame)
            if config.time_since_update == config.update_frequency:
                config.update(result)
            else:
                config.increment_time()
    print("finished execution")

run()