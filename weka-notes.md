# Weka Primer Notes

Notes from [weka primer](http://weka.wikispaces.com/Primer)

A weka dataset is:

- implemented by the Instances class.
- a collection of samples, each an instance of class Instance

Instances are represented externally in ARFF files, which contain:

- a multi-line commented header
- followed by @data
- followed by the data, 1 sample per line

By default, the last attribute is considered to be the class/target variable.
To override, specify the target variable with `-c n`, where `-c 1` specifies the first var as the target var.

<example here?>
<what is the context here we are trying to work in?>

There are a couple of converters for CSV and C45 files:

- Q: what is a C45 file?

- java weka.core.converters.CSVLoader data.csv > data.arff
- java weka.core.converters.C45Loader c45_filestem > data.arff

All learning algorithms are derived from abstract class Classifier

A classifier model is an arbitrarily complex mapping from all-but-one dataset attributes to the class attribute.

        proteus-> pwd
        /Applications/weka-3-6-4
        proteus-> java -classpath /Applications/weka-3-6-4/weka.jar weka.classifiers.rules.ZeroR -t data/weather.arff

this works from inside the weka SimpleCLI:

        java weka.classifiers.rules.ZeroR -t /Applications/weka-3-6-4/data/weather.arff

## weka.filters

classes that transform datasets;  useful for pre-processing

- remove or add attributes
- resample the dataset
- removing examples
- etc

all filters support `-i` and `-o` to name the input and output datasets.
defaults to std{in,out}.
discover other args via -h

filters are organized into supervised and unsupervised, and then again into instance and attribute filtering

weka.filters.supervised

must have a class specified with -c <field_number>

Discretize: map numeric attributes into nominal ones, based on class, via Fayyad and Irani's MDL method, or optionally via Kononeko's MDL method.

