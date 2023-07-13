import pyfpng
import cv2
import numpy as np


image = np.random.randint(0, 255, (2000, 2000, 3), dtype=np.uint8)
success, image_bytes = pyfpng.encode_image_to_memory(image)
assert success
success, parsed = pyfpng.decode_memory(image_bytes)
assert success == 0

def decode():
    success, parsed = pyfpng.decode_memory(image_bytes)
    assert success == 0


from concurrent.futures import ThreadPoolExecutor, wait
import time

def do_test(workers=10):
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for _ in range(10):
            futures.append(executor.submit(decode))
        wait(futures)
    t1 = time.time()
    print(f"Finished in {t1-t0} seconds with {workers} worker threads")


for i in range(1, 11):
    do_test(i)