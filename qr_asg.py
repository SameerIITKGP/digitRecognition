import qrtools
import pygame.camera, pygame.image

myCode = qrtools.QR()
i=0

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])

while (i < 1):

	myCode.decode_webcam()
	data = myCode.data
	data_type = myCode.data_type
	data_string = myCode.data_to_string()
	print data_string
		
	cam.start()
	image = cam.get_image()
	pygame.image.save(image, "capture" + str(i+1) + ".jpg")
	cam.stop()
	
	i+=1
	
pygame.camera.quit()

# fo = open("foo.txt", "wb")
# fo.write(data_string);
# fo.close()