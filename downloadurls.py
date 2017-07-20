import urllib.request
import os


# urllib.request.urlretrieve("http://www.example.com/songs/mp3.mp3", "mp3.mp3")


def store_raw_images():
    neg_images_link = open('motorcycle_urls.txt', 'rb')
    print(neg_images_link)
    neg_image_urls = neg_images_link.read().decode('utf-8')
    print(neg_image_urls)
    neg_images_link.close()
    pic_num = 772

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
    #         # img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
    #         # # should be larger than samples / pos pic (so we can place our image on it)
    #         # # resized_image = cv2.resize(img, (100, 100))
    #         # cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1
    #
        except Exception as e:
            print(str(e))

store_raw_images()