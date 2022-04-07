# bili_remove_code
decode the video downloaded from the uwp client of bilibili, which can only be played in the app
works on v2.14.76.0

module required: sys
usage: 
```python biliDecode.py [filename]```

or drag the video file into the .exe

P.S. In case of the large file size, the program reads 10MB at most each time. You can change it by editing  ```block_size``` 
