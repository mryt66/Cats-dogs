# cats-dogs-classifier
cats-dogs-classifier is a program that decides if .wav (sound) file sounds more like a dog or cat.
csv_creator.py fills data_cats and data_dogs with converted to floats data, every line contains amplitudes of the highest average amplitude of spectrum in each sound.
Lines doesn't have this same length because of different frequency. (more float numbers in line = bigger frequency)

Mews and barks are simplified to one sound by us. Example of this one sound can be presented on this graph:
<p align="center">
  <img src="https://github.com/mryt66/cats-dogs-classifier/assets/64143856/81e3d9fe-8406-4f06-aee2-d54189bf52b0" alt="Spectrum plot" />
</p>

<p align="center">
  <img src="https://github.com/mryt66/cats-dogs-classifier/assets/64143856/9847169e-ab30-426d-aacf-7c2f469c9ba3" alt="An example how does classifier prepare data" />
</p>

With 25 different records for each dog and cat our classifier had around 90% accuracy

Data included in cats&dogs .wav, cut and based on:
https://www.kaggle.com/code/gauravduttakiit/yamnet-audio-cats-and-dogs
