<h1>ConvNet</h1>

<h3>Prerequisites:</h3>
<ul>
  <li>Python 3.6 (packaged in Anaconda 3)</li>
  <li>Anaconda 3: https://www.continuum.io/downloads</li>
  <li>CNTK 2.0: https://docs.microsoft.com/en-us/cognitive-toolkit/setup-windows-python</li>
  <li>PySound: https://pysoundfile.readthedocs.io/en/0.9.0/</li>
  <li>CMU AN4 Database: http://www.speech.cs.cmu.edu/databases/an4/index.html</li>
</ul>

<h3>Instructions for setting up environment on Windows:</h3>
<ol>
  <li>Install Anaconda 3.6 w/ recommended settigs</li>
  <li>Open Anaconda -> Environments tab -> root -> Open Terminal</li>
  <li>Install PySound dependencies: 'conda install cffi numpy'</li>
  <li>Install PySound: 'pip install pysoundfile'</li>
  <li>Install CNTK 2.0 (replace url w/ appropriate url*): 'pip install "url"'</li>
  <li>Verify CNTK install: 'python -c "import cntk; print(cntk.__version__)"'</li>
  <li>Clone repo: 'git clone https://github.com/sschweig/ConvNet.git'</li>
  <li>Navigate to repo root (same file as root.txt) -> Create folder "DATA"</li>
  <li>Navigate to DATA -> Create folders "TEST" and "TRAIN"</li>
  <li>Download AN4 DB at above link</li>
  <li>unpack an4test_clstk to DATA/TEST and an4_clstk to DATA/TRAIN</li>
</ol>

<p>*Correct URL can be found at CNTK 2.0 link above. Go to Python 3.6 and select appropriate version. <b>"If you plan on using a GPU enabled version of CNTK, you will need a CUDA 8 compliant graphics card and up-to-date graphics drivers installed on your system."</b></p>
