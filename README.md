<h1>Cats & Dogs</h1>
Cats & Dogs is a program that decides if .wav (sound) file sounds more like a dog or cat.
csv_creator.py fills data_cats and data_dogs with converted to floats data, every line contains amplitudes of the highest average amplitude of spectrum in each sound.
Lines don't have this same length because of different frequency. (more float numbers in line = bigger frequency).
To make a classifier we used self made KNN.
Mews and barks are simplified to one sound. Example of this one sound is presented on this graph:
<p align="center">
  <img src="https://github.com/mryt66/cats-dogs-classifier/assets/64143856/81e3d9fe-8406-4f06-aee2-d54189bf52b0" />
  <br />
  Spectrum plot
</p>

<p align="center">
  <img src="https://github.com/mryt66/cats-dogs-classifier/assets/64143856/9847169e-ab30-426d-aacf-7c2f469c9ba3" />
  <br />
  Example how does classifier prepare data
</p>

To know if your .wav file sounds more like a cat or dog, put into src folder file named 'Your_file.wav'.

With 98 different records for each dog and cat classifier has approximately 83% accuracy

Data included in Cats&Dogs .wav, cut and based on:
https://www.kaggle.com/code/gauravduttakiit/yamnet-audio-cats-and-dogs
