'''
多摄像头接入

Author: alex
Created Time: 2020年07月27日 星期一 10时00分42秒
'''
import time
import cv2
import multiprocessing as mp


def queue_img_put(q_put, cap_id, uri):
    cap = cv2.VideoCapture(uri)
    while True:
        time.sleep(1)
        is_opened, frame = cap.read()
        q_put.put((cap_id, frame, time.time())) if is_opened else None
        # q_put.get() if q_put.qsize() > 1 else None


def dosometing(origin_img_q, result_img_q):
    is_opened = True
    while is_opened:
        while origin_img_q.qsize() == 0:
            time.sleep(2)
        print('In dosometing: ', origin_img_q.qsize())
        cap_id, origin_img, in_time = origin_img_q.get()  # one tf model
        print(in_time)
        # do some things
        result_img_q.put((origin_img, cap_id))


def queue_img_get(q_get):
    while True:
        (origin_img, cap_id) = q_get.get()
        print('In get queue: ', cap_id, origin_img.shape)


def run():
    mp.set_start_method(method='spawn')

    origin_img_q = mp.Queue(maxsize=2)
    result_img_q = mp.Queue(maxsize=4)

    # 摄像头配置
    cams = [
        {
            'id': 0,
            # 'uri': 0,
            'uri': 'rtsp://192.168.80.153:8554/live',
            # 'uri': '/device/video0'
        },
        # {
            # 'id': 1,
            # 'uri': 2,
            # 'uri': '/device/video2'
        # },
    ]
    processes = [mp.Process(target=queue_img_put,
                            args=(origin_img_q, cam['id'], cam['uri']))
                 for cam in cams]
    processes += [
        mp.Process(target=dosometing, args=(origin_img_q, result_img_q)),
        mp.Process(target=queue_img_get, args=(result_img_q, )),
    ]
    [setattr(process, "daemon", True) for process in processes]
    [process.start() for process in processes]
    [process.join() for process in processes]


if __name__ == '__main__':
    run()
