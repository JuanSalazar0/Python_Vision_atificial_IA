import cv2 as cv
import numpy as np


def Temma(img,temp):
        y_template, x_template = temp.shape[:2]
        y_img, x_img = img.shape[:2]

        centro_ytemp = int(y_template/2)  #determinar el centro del template 
        centro_xtemp = int(x_template/2)
         #print("cx:",centro_ytemp)
         #print("cy:",centro_xtemp)
        res = np.zeros((y_img-y_template+1,x_img-x_template+1))
        y_res = range(0,res.shape[0]).__iter__()

        for y in range(centro_ytemp, y_img-(y_template-centro_ytemp-1)):  #recorrer el template teniendo en cuenta las dimensiones
            x_res = range(0,res.shape[1]).__iter__()
            yr = next(y_res)
           
            for x in range(centro_xtemp, x_img-(x_template-centro_xtemp-1)):
                xr = next(x_res)
                sum = 0
                centro_ytemp = int(temp.shape[0]/2)
                centro_xtemp = int(temp.shape[1]/2)
                y_yp = range(y-centro_ytemp,y+centro_ytemp).__iter__()
                for yp in range(0,temp.shape[0]):
                 x_xp = range(x-centro_xtemp,x+centro_xtemp).__iter__()
                 y_img = next(y_yp)

                 for xp in range(0,temp.shape[1]):
                    sum += (float(temp[yp,xp])-float(img[y_img,next(x_xp)]))**2
                    res[yr,xr]=sum
    
        return res

if __name__ == "__main__":
    img = cv.imread('busca.jpg',0) # El 0 convierte a escala de grises
    temp = cv.imread('busca3.jpg',0)

    alto, largo = temp.shape[:2]
    #print("alto:",alto)
    #print("largo",largo)

    res = Temma(img,temp)
    v_min, v_max, l_min, l_max = cv.minMaxLoc(res)
    ubi = l_min

    img2 = cv.imread("busca.jpg")
    temp = cv.imread("busca3.jpg")

    esq_dinf = (ubi[0] + largo, ubi[1] + alto)
    cv.rectangle(img2, ubi, esq_dinf, (255, 135, 20), 5)

    cv.imshow('Imagen', img2)
    cv.imshow('Template', temp)
    cv.waitKey(0)
                
    cv.destroyAllWindows()