# Sign Language Recognition System  

The overall goal of this project is to build a word recognizer for American Sign Language video sequences, demonstrating the power of probabalistic models. In particular, this project employs hidden Markov models (HMM's) to analyze a series of measurements taken from videos of American Sign Language (ASL) collected for research (see the RWTH-BOSTON-104 Database). In this video, the right-hand x and y locations are plotted as the speaker signs the sentence.  

The raw data, train, and test sets are pre-defined. A variety of feature sets are derived, and three different model selection criterion are implemented to determine the optimal number of hidden states for each word model. The recognizer is implemented and the effects the different combinations of feature sets and model selection criteria are compared.  

### Install

This project requires **Python 3** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [SciPy](https://www.scipy.org/)
- [scikit-learn](http://scikit-learn.org/0.17/install.html)
- [pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [jupyter](http://ipython.org/notebook.html)
- [hmmlearn](http://hmmlearn.readthedocs.io/en/latest/)

*For `hmmlearn` insatllation, run*  
```sh
pip install git+https://github.com/hmmlearn/hmmlearn.git
```

### Data 

The data in the `asl_recognizer/data/` directory was derived from 
the [RWTH-BOSTON-104 Database](http://www-i6.informatik.rwth-aachen.de/~dreuw/database-rwth-boston-104.php). 
The handpositions (`hand_condensed.csv`) are pulled directly from 
the database [boston104.handpositions.rybach-forster-dreuw-2009-09-25.full.xml](boston104.handpositions.rybach-forster-dreuw-2009-09-25.full.xml). The three markers are:

*   0  speaker's left hand
*   1  speaker's right hand
*   2  speaker's nose
*   X and Y values of the video frame increase left to right and top to bottom.

A sample [ASL recognizer video](http://www-i6.informatik.rwth-aachen.de/~dreuw/download/021.avi) is available to see how the hand locations are tracked. 

The videos are sentences with translations provided in the database. For purposes of this project, the sentences have been pre-segmented into words based on slow motion examination of the files. These segments are in the `train_words.csv` and `test_words.csv` file in the form of start and end frames (inclusive).

The videos in the corpus include recordings from three different ASL speakers. The mappings for the three speakers to video are included in the `speaker.csv` file.
