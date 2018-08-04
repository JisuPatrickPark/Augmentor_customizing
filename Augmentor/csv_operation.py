import csv
import numpy as np
import Augmentor


list_obo = []
list_st =[]

def one_by_one(dir):
    list = []
    
    with open(dir,newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for op in reader:
            list.append(op)
    
    list = np.array(list)
    result = list[1:,:]
    num_op = result[:,0].size
        
    for i in range(0,num_op):
            operation = result[i,0]            
            
            if 'frg' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                max_left = np.array(result[i,4],dtype=int)
                max_right = np.array(result[i,5],dtype=int)
                filter_size = np.array(result[i,6],dtype=int)
                filter = (filter_size,filter_size)
                FRG = Augmentor.Pipeline(input_dir,output_dir)
                FRG.frg(prob,max_left,max_right,filter)
                FRG.status()
                list = np.append(list, ['FRG'])
                
            elif 'gaussian_blur' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)        
                ksize = result[i,4]
                
                if ksize == 'Random':
                    ksize = "Random"
                else:
                    filter_size = np.array(result[i,4],dtype=int)
                ksize = (filter_size,filter_size)            
                min = np.array(result[i,5],dtype=float)
                max = np.array(result[i,6],dtype=float)
                GB = Augmentor.Pipeline(input_dir,output_dir)
                GB.gaussian_blur(prob,ksize,min,max)
                GB.status()
                list = np.append(list, ['GB'])
                
            elif 'zoom_random' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                area = np.array(result[i,4],dtype=float)
                r = result[i,5]
                print(r)
                
                if r == 'TRUE':
                    r = True
                elif r == 'FALSE':
                    r = False
                print(r)
                ZR = Augmentor.Pipeline(input_dir,output_dir)
                ZR.zoom_random(prob,area,r)
                ZR.status()
                list = np.append(list, ['ZR'])
                
            elif 'zoom' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                min = np.array(result[i,4],dtype=float)
                max = np.array(result[i,5],dtype=float)
                Z = Augmentor.Pipeline(input_dir,output_dir)
                Z.zoom(prob,min,max)
                Z.status()
                list = np.append(list, ['Z'])
                
            elif 'flip_rotate' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                min = np.array(result[i,4],dtype=float)
                max = np.array(result[i,5],dtype=float)
                r = result[i,5]
                if r == 'TRUE':
                    r = True
                elif r == 'FALSE':
                    r = False
                FR = Augmentor.Pipeline(input_dir,output_dir)
                FR.flip_rotate(prob,min,max,r)
                FR.status()
                list = np.append(list, ['FR'])
                
                
            elif 'random_contrast' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                min = np.array(result[i,4],dtype=float)
                max = np.array(result[i,5],dtype=float)
                RC = Augmentor.Pipeline(input_dir,output_dir)
                RC.random_contrast(prob,min,max)
                RC.status()
                list = np.append(list, ['RC'])    
            
            return list
        
#Updated in near future
def sample_obo(list = list):
    for i in list:
        print(i)
    

def stack(dir, number_of_sample):    
    list = []
    
    with open(dir,newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for op in reader:
            list.append(op)
            
    list = np.array(list)
    result = list[1:,:]
    num_op = result[:,0].size
        
    for i in range(0,num_op):
            operation = result[i,0]            
            
            if 'frg' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                max_left = np.array(result[i,4],dtype=int)
                max_right = np.array(result[i,5],dtype=int)
                filter_size = np.array(result[i,6],dtype=int)
                filter = (filter_size,filter_size)
                ST = Augmentor.Pipeline(input_dir,output_dir)
                ST.frg(prob,max_left,max_right,filter)
                ST.status()
                
            elif 'gaussian_blur' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)        
                ksize = result[i,4]
                
                if ksize == 'Random':
                    ksize = "Random"
                else:
                    filter_size = np.array(result[i,4],dtype=int)
                ksize = (filter_size,filter_size)            
                min = np.array(result[i,5],dtype=float)
                max = np.array(result[i,6],dtype=float)
                ST = Augmentor.Pipeline(input_dir,output_dir)
                ST.gaussian_blur(prob,ksize,min,max)
                ST.status()
                
            elif 'zoom_random' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                area = np.array(result[i,4],dtype=float)
                r = result[i,5]
                print(r)
                
                if r == 'TRUE':
                    r = True
                elif r == 'FALSE':
                    r = False
                print(r)
                ST = Augmentor.Pipeline(input_dir,output_dir)
                ST.zoom_random(prob,area,r)
                ST.status()
                
            elif 'zoom' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                min = np.array(result[i,4],dtype=float)
                max = np.array(result[i,5],dtype=float)
                ST = Augmentor.Pipeline(input_dir,output_dir)
                ST.zoom(prob,min,max)
                ST.status()
                
            elif 'flip_rotate' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                min = np.array(result[i,4],dtype=float)
                max = np.array(result[i,5],dtype=float)
                r = result[i,5]
                if r == 'TRUE':
                    r = True
                elif r == 'FALSE':
                    r = False
                ST = Augmentor.Pipeline(input_dir,output_dir)
                ST.flip_rotate(prob,min,max,r)
                ST.status()
                
                
            elif 'random_contrast' in operation:
                input_dir = result[i,1]
                output_dir = result[i,2]
                prob = np.array(result[i,3],dtype=float)
                min = np.array(result[i,4],dtype=float)
                max = np.array(result[i,5],dtype=float)
                RC = Augmentor.Pipeline(input_dir,output_dir)
                RC.random_contrast(prob,min,max)
                ST.status()
            
    ST.sample(number_of_sample)
            

