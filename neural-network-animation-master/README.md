# Neural Network Animation
Watch a neural network think. Written in Python.

Requires the FFMPEG codec. To install use the command "brew install ffmpeg".

In the video, the synapses are represented by lines. A thickening of a line represents the synaptic connection between
two neurons growing stronger. As the thickeness of the lines change, you can see the neural network learning. Flashes of
light represent neural activity.

To run the program use the command "python main.py". It will generate a mp4 file in the same folder.

You can read more about it and watch the video here:
https://medium.com/@miloharper/how-to-generate-a-video-of-a-neural-network-learning-in-python-62f5c520e85c



||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  
||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  
||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  
\/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  

""""""""

The problem was that the guy included the stupid "matplotlib" Library Folder - 

- which he did to help people avoid having to do find it and install it themselves -

but SublimeText 3 with Anaconda (the thing we use to edit the code) imports libraries automatically - thats why I chose it.

so delete the stupid matplotlip folder 

then go to the main.py file and hit CMB+B
"""""""""""