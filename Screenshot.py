import cv2
import numpy as np
def GetIamge(image1,image2,question_no,path):
    # Load the two images
    image1 = cv2.imread("image1.png")
    image2 = cv2.imread("image2.png")

    # Check if the images have the same height and width
    if image1.shape[0] != image2.shape[0] or image1.shape[1] != image2.shape[1]:
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Create a new image that is twice the height of the original images
    new_image = np.zeros((image1.shape[0] * 2, image1.shape[1], 3), np.uint8)

    # Copy the first image to the top half of the new image
    new_image[0:image1.shape[0], :, :] = image1

    # Copy the second image to the bottom half of the new image
    new_image[image1.shape[0]:, :, :] = image2

    # Display the new image
    cv2.imshow("Merged Image", question_no)
    cv2.waitKey(0)
    # Save the new image
    cv2.imwrite(f"{path}.jpg", question_no)