
import os
#from memory_profiler import profile
import sys

#@profile
def decode(src_name):
    
    block_size=1024*1024*10
    keyword=bytes([0xff,0xff,0xff])
    ext_name=src_name.split('.')[-1]
    try:
        src_file=open(src_name,"rb")
        if src_file:
            print("\""+src_name+"\" has opened!")
        #read first three bytes
        tmp=src_file.read(3)
        if tmp!=keyword:
            print("can not decode")
            src_file.close()
            return

        #copy bytes without the first 0xffffff
        dst_file=open(src_name+"decoded."+ext_name,"xb")

        while True:
            tmp_data=src_file.read(block_size)
            if not tmp_data:
                src_file.close()
                break
            dst_file.write(tmp_data)
    finally:
        if dst_file or src_file:
            src_file.close()
            dst_file.close()

if __name__ =='__main__':
    if len(sys.argv)>1:
        filename=sys.argv[1]
        decode(filename)
    else :
        #src_name="297961488_1_0.mp4"
        print("please input filename")
    print("exit")
        
    
